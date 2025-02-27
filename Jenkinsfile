pipeline {
    agent any  // Using any available agent since your Jenkins server doesn't seem to have Docker plugin properly configured
    
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
        
        stage('Install Dependencies') {
            steps {
                sh '''
                    # Install AWS CLI if not present
                    if ! command -v aws &> /dev/null; then
                        echo "Installing AWS CLI..."
                        curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
                        unzip awscliv2.zip
                        sudo ./aws/install
                    fi
                    
                    # Install Docker if not present
                    if ! command -v docker &> /dev/null; then
                        echo "Installing Docker..."
                        sudo apt-get update
                        sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
                        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
                        sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
                        sudo apt-get update
                        sudo apt-get install -y docker-ce
                        sudo usermod -aG docker jenkins
                    fi
                    
                    # Install kubectl if not present
                    if ! command -v kubectl &> /dev/null; then
                        echo "Installing kubectl..."
                        curl -LO "https://dl.k8s.io/release/stable.txt"
                        curl -LO "https://dl.k8s.io/release/$(cat stable.txt)/bin/linux/amd64/kubectl"
                        chmod +x kubectl
                        sudo mv kubectl /usr/local/bin/
                    fi
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

                        # Build da imagem Docker
                        docker build -t $ECR_REPO .

                        # Tag e push para o ECR
                        docker tag $ECR_REPO:latest ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/$ECR_REPO:$IMAGE_TAG
                        docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/$ECR_REPO:$IMAGE_TAG
                    '''
                    env.IMAGE_URI = imageUri
                }
            }
        }

        stage('Configure EKS Access') {
            steps {
                sh '''
                    aws eks update-kubeconfig --region $AWS_REGION --name $CLUSTER_NAME
                    kubectl version
                '''
            }
        }

        stage('Deploy other Kubernetes resources to EKS') {
            steps {
                script {
                    def kubernetesFiles = findFiles(glob: '.kubernetes/*.yaml')
                    
                    for (file in kubernetesFiles) {
                        sh "kubectl apply -f ${file.path}"
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
