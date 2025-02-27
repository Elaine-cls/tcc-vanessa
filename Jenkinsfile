pipeline {
    agent any
    
    environment {
        AWS_REGION = 'us-east-2'
        CLUSTER_NAME = 'k8s-cluster-tcc'
        ECR_REPO = 'pet-care-tcc-ads'
        IMAGE_TAG = 'latest'
        AWS_ACCOUNT_ID = '863518437070'
        PATH = "/var/jenkins_home/bin:${env.PATH}"
    }
    
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh '''
                    # Instalar pacotes necessários
                    apt-get update -y
                    apt-get install -y curl unzip apt-transport-https ca-certificates software-properties-common
                '''
            }
        }
        
        stage('Install Docker') {
            steps {
                sh '''
                    # Instalar Docker
                    curl -fsSL https://get.docker.com -o get-docker.sh
                    sh get-docker.sh
                    
                    # Verificar instalação do Docker
                    docker --version
                    
                    # Garantir que o jenkins possa usar o docker
                    usermod -aG docker jenkins || true
                    chmod 666 /var/run/docker.sock || true
                '''
            }
        }
        
        stage('Install AWS CLI') {
            steps {
                sh '''
                    # Criar diretório bin se não existir
                    mkdir -p /var/jenkins_home/bin
                    
                    # Baixar e instalar AWS CLI
                    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
                    unzip -o awscliv2.zip
                    ./aws/install -i /var/jenkins_home/aws-cli -b /var/jenkins_home/bin
                    
                    # Verificar instalação
                    aws --version
                '''
            }
        }
        
        stage('Install kubectl') {
            steps {
                sh '''
                    # Baixar e instalar kubectl
                    curl -LO "https://dl.k8s.io/release/stable.txt"
                    KUBECTL_VERSION=$(cat stable.txt)
                    curl -LO "https://dl.k8s.io/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl"
                    chmod +x kubectl
                    mv kubectl /var/jenkins_home/bin/
                    
                    # Verificar instalação
                    kubectl version --client
                '''
            }
        }
        
        stage('Configure AWS Credentials') {
            steps {
                sh '''
                    # Opcional: Configurar credenciais da AWS se necessário
                    # Caso você esteja usando o Jenkins Credentials Plugin, considere usar withCredentials no lugar
                    mkdir -p ~/.aws
                    
                    # Verifique se as credenciais já estão configuradas via assumirRole do pod ou variáveis de ambiente
                    aws sts get-caller-identity || echo "AWS credentials need to be configured"
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
                    # Criar diretório .kube se não existir
                    mkdir -p /var/jenkins_home/.kube
                    
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
                rm -rf awscliv2.zip aws stable.txt get-docker.sh || true
            '''
        }
    }
}
