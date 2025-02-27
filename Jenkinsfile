pipeline {
    agent any
    
    environment {
        AWS_REGION = 'us-east-2'
        CLUSTER_NAME = 'k8s-cluster-tcc'
        ECR_REPO = 'pet-care-tcc-ads'
        IMAGE_TAG = 'latest'
        AWS_ACCOUNT_ID = '863518437070'
        HOME = '/var/jenkins_home'
        PATH = "/var/jenkins_home/bin:${env.PATH}"
    }
    
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Tools Directory') {
            steps {
                sh '''
                    # Criar diretórios para ferramentas
                    mkdir -p /var/jenkins_home/bin
                    mkdir -p /var/jenkins_home/tools
                    mkdir -p /var/jenkins_home/.kube
                '''
            }
        }
        
        stage('Install Docker CLI') {
            steps {
                sh '''
                    # Verificar se o Docker já está disponível
                    if command -v docker &> /dev/null; then
                        echo "Docker já está instalado"
                        docker --version
                    else
                        echo "Baixando o Docker CLI estático (sem necessidade de instalação)"
                        cd /var/jenkins_home/tools
                        
                        # Baixar binário estático do Docker
                        curl -L https://download.docker.com/linux/static/stable/x86_64/docker-20.10.9.tgz -o docker.tgz
                        tar -xzf docker.tgz
                        cp docker/docker /var/jenkins_home/bin/
                        rm -rf docker.tgz docker
                        
                        # Verificar a instalação
                        docker --version || echo "Instalação do Docker falhou. Talvez o socket precise ser montado."
                    fi
                    
                    # Verificar acesso ao socket do Docker
                    ls -la /var/run/docker.sock || echo "Socket do Docker não encontrado ou sem permissão de acesso"
                '''
            }
        }
        
        stage('Install AWS CLI') {
            steps {
                sh '''
                    # Verificar se AWS CLI já está instalado
                    if command -v aws &> /dev/null; then
                        echo "AWS CLI já está instalado"
                        aws --version
                    else
                        echo "Instalando AWS CLI"
                        cd /var/jenkins_home/tools
                        curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
                        unzip -o awscliv2.zip
                        ./aws/install -i /var/jenkins_home/aws-cli -b /var/jenkins_home/bin
                        rm -rf awscliv2.zip
                        
                        # Verificar instalação
                        aws --version
                    fi
                '''
            }
        }
        
        stage('Install kubectl') {
            steps {
                sh '''
                    # Verificar se kubectl já está instalado
                    if command -v kubectl &> /dev/null; then
                        echo "kubectl já está instalado"
                        kubectl version --client
                    else
                        echo "Instalando kubectl"
                        cd /var/jenkins_home/tools
                        curl -LO "https://dl.k8s.io/release/stable.txt"
                        KUBECTL_VERSION=$(cat stable.txt)
                        curl -LO "https://dl.k8s.io/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl"
                        chmod +x kubectl
                        mv kubectl /var/jenkins_home/bin/
                        rm -f stable.txt
                        
                        # Verificar instalação
                        kubectl version --client
                    fi
                '''
            }
        }
        
        stage('Verify Docker Socket') {
            steps {
                sh '''
                    # Verificar se o socket do Docker está acessível
                    if [ ! -e /var/run/docker.sock ]; then
                        echo "ERRO: Socket do Docker não encontrado em /var/run/docker.sock"
                        echo "Por favor, monte o socket do Docker no contêiner Jenkins usando:"
                        echo "  - Para Docker: -v /var/run/docker.sock:/var/run/docker.sock"
                        echo "  - Para Kubernetes/EKS: adicione um volume hostPath para o socket"
                        exit 1
                    fi
                    
                    if [ ! -r /var/run/docker.sock ]; then
                        echo "ERRO: Sem permissão para ler o socket do Docker"
                        echo "Tente executar: 'chmod 666 /var/run/docker.sock' no host"
                        exit 1
                    fi
                    
                    echo "Socket do Docker está acessível"
                    docker info || echo "Docker não está respondendo. Verifique se o daemon está rodando no host."
                '''
            }
        }
        
        stage('Configure AWS Credentials') {
            steps {
                sh '''
                    mkdir -p ~/.aws
                    
                    # Verificar se AWS está configurado corretamente
                    aws sts get-caller-identity || {
                        echo "AWS credentials não estão configuradas!"
                        echo "Execute o pipeline com credenciais AWS configuradas corretamente."
                        echo "Você pode usar Jenkins Credentials Plugin ou variáveis de ambiente AWS_ACCESS_KEY_ID e AWS_SECRET_ACCESS_KEY."
                        exit 1
                    }
                '''
            }
        }
        
        stage('Build and Push Docker Image') {
            steps {
                script {
                    def imageUri = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}"
                    
                    sh '''
                        # Login no Amazon ECR
                        aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com
                        
                        # Criar repositório se não existir
                        aws ecr describe-repositories --repository-names $ECR_REPO --region $AWS_REGION || aws ecr create-repository --repository-name $ECR_REPO --region $AWS_REGION
                        
                        # Build da imagem Docker
                        docker build -t $ECR_REPO:$IMAGE_TAG .
                        
                        # Tag e push para o ECR
                        docker tag $ECR_REPO:$IMAGE_TAG ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/$ECR_REPO:$IMAGE_TAG
                        docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/$ECR_REPO:$IMAGE_TAG
                    '''
                    env.IMAGE_URI = imageUri
                }
            }
        }
        
        stage('Configure EKS Access') {
            steps {
                sh '''
                    # Configurar acesso ao cluster EKS
                    aws eks update-kubeconfig --region $AWS_REGION --name $CLUSTER_NAME --kubeconfig /var/jenkins_home/.kube/config
                    
                    # Verificar acesso ao cluster
                    kubectl get nodes
                '''
            }
        }
        
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh '''
                        # Verificar e criar namespace se necessário
                        kubectl get namespace petcare || kubectl create namespace petcare
                        
                        # Aplicar configurações Kubernetes
                        if [ -d ".kubernetes" ]; then
                            for file in .kubernetes/*.yaml; do
                                envsubst < "$file" | kubectl apply -f -
                            done
                        elif [ -d "kubernetes" ]; then
                            for file in kubernetes/*.yaml; do
                                envsubst < "$file" | kubectl apply -f -
                            done
                        else
                            echo "Diretório kubernetes não encontrado! Criando deployment básico..."
                            
                            # Criar um deployment básico se não houver arquivos Kubernetes
                            cat <<EOF | kubectl apply -f -
                            apiVersion: apps/v1
                            kind: Deployment
                            metadata:
                              name: $ECR_REPO
                              namespace: petcare
                            spec:
                              replicas: 1
                              selector:
                                matchLabels:
                                  app: $ECR_REPO
                              template:
                                metadata:
                                  labels:
                                    app: $ECR_REPO
                                spec:
                                  containers:
                                  - name: $ECR_REPO
                                    image: ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/$ECR_REPO:$IMAGE_TAG
                                    ports:
                                    - containerPort: 80
                            ---
                            apiVersion: v1
                            kind: Service
                            metadata:
                              name: $ECR_REPO
                              namespace: petcare
                            spec:
                              selector:
                                app: $ECR_REPO
                              ports:
                              - port: 80
                                targetPort: 80
                              type: ClusterIP
                            EOF
                        fi
                        
                        # Verificar status do deployment
                        kubectl rollout status deployment/$ECR_REPO -n petcare
                    '''
                }
            }
        }
    }
    
    post {
        success {
            echo 'Deployment concluído com sucesso!'
        }
        failure {
            echo 'Deployment falhou. Verifique os logs para mais detalhes.'
        }
        always {
            echo 'Limpando recursos temporários...'
            sh '''
                rm -rf /var/jenkins_home/tools/awscliv2.zip /var/jenkins_home/tools/aws /var/jenkins_home/tools/stable.txt || true
            '''
        }
    }
}
