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
        stage('Configure EKS Access and Deploy Resources') {
            steps {
                withAWS(credentials: 'aws-credentials', region: 'us-east-2') {
                    script {
                        // Atualizar a configuração do Kubernetes com as credenciais do Jenkins
                        sh 'aws eks update-kubeconfig --region $AWS_REGION --name $CLUSTER_NAME'
                        
                        // Verificar a versão do kubectl
                        sh 'kubectl version --short'
                        
                        // Deploy de recursos Kubernetes
                        def kubernetesFiles = findFiles(glob: '.kubernetes/*.yaml')
                        for (file in kubernetesFiles) {
                            sh "kubectl apply -f ${file.path}"
                        }
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
