pipeline {
    agent any
    environment {
        AWS_REGION = 'us-east-2'
        CLUSTER_NAME = 'k8s-cluster-tcc'
        ECR_REPO = 'pet-care-tcc-ads'
        IMAGE_TAG = 'latest'
        AWS_ACCOUNT_ID = '863518437070'
    }
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        stage('Build and Push Docker Image') {
            steps {
                withAWS(credentials: 'aws-credentials', region: 'us-east-2', role: 'arn:aws:iam::863518437070:role/oidcsva') {
                    sh '''
                        # Verificar permissões
                        ls -la /var/run/secrets/eks.amazonaws.com/serviceaccount/ || echo "Diretório não existe ou sem permissão"
                        
                        # Login no Amazon ECR
                        aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com
                        
                        # Build da imagem Docker
                        docker build -t $ECR_REPO .
                        
                        # Tag e push para o ECR
                        docker tag $ECR_REPO:latest ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/$ECR_REPO:$IMAGE_TAG
                        docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/$ECR_REPO:$IMAGE_TAG
                    '''
                }
            }
        }
        stage('Configure EKS Access') {
            steps {
                sh '''
                    # Usar credenciais AWS diretas em vez de depender do token do ServiceAccount
                    export AWS_ACCESS_KEY_ID=$(cat /root/.aws/credentials | grep aws_access_key_id | cut -d' ' -f3)
                    export AWS_SECRET_ACCESS_KEY=$(cat /root/.aws/credentials | grep aws_secret_access_key | cut -d' ' -f3)
                    
                    # Atualizar a configuração do Kubernetes
                    aws eks update-kubeconfig --region $AWS_REGION --name $CLUSTER_NAME
                    kubectl version
                '''
            }
        }
        stage('Deploy other Kubernetes resources to EKS') {
            steps {
                script {
                    def kubernetesFiles = sh(script: 'find .kubernetes -name "*.yaml"', returnStdout: true).trim().split("\n")
                    
                    for (file in kubernetesFiles) {
                        sh "kubectl apply -f ${file}"
                    }
                }
            }
        }
    }
    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed.'
        }
    }
}
