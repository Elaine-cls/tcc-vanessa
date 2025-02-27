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
        
        stage('Setup Docker-in-Docker') {
            steps {
                sh '''
                    # Using Docker CLI from the host (Docker socket)
                    # This assumes your Jenkins container has the Docker socket mounted
                    docker version || echo "Docker not available - make sure /var/run/docker.sock is mounted"
                '''
            }
        }
        
        stage('Install AWS CLI') {
            steps {
                sh '''
                    # Install AWS CLI without sudo
                    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
                    unzip -q awscliv2.zip
                    ./aws/install -i /var/jenkins_home/aws-cli -b /var/jenkins_home/bin
                    export PATH=/var/jenkins_home/bin:$PATH
                    aws --version
                '''
            }
        }
        
        stage('Install kubectl') {
            steps {
                sh '''
                    # Install kubectl without sudo
                    curl -LO "https://dl.k8s.io/release/stable.txt"
                    curl -LO "https://dl.k8s.io/release/$(cat stable.txt)/bin/linux/amd64/kubectl"
                    chmod +x kubectl
                    mkdir -p /var/jenkins_home/bin
                    mv kubectl /var/jenkins_home/bin/
                    export PATH=/var/jenkins_home/bin:$PATH
                    kubectl version --client
                '''
            }
        }
        
        stage('Build and Push Docker Image') {
            steps {
                script {
                    def imageUri = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}"
                    
                    sh '''
                        # Set PATH to include our installed tools
                        export PATH=/var/jenkins_home/bin:$PATH
                        
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
                    # Set PATH to include our installed tools
                    export PATH=/var/jenkins_home/bin:$PATH
                    
                    aws eks update-kubeconfig --region $AWS_REGION --name $CLUSTER_NAME --kubeconfig /var/jenkins_home/.kube/config
                    kubectl version
                '''
            }
        }

        stage('Deploy other Kubernetes resources to EKS') {
            steps {
                script {
                    sh '''
                        # Set PATH to include our installed tools
                        export PATH=/var/jenkins_home/bin:$PATH
                        
                        # Make sure kubernetes directory exists
                        if [ -d ".kubernetes" ]; then
                            for file in .kubernetes/*.yaml; do
                                kubectl apply -f "$file"
                            done
                        else
                            echo "No .kubernetes directory found"
                        fi
                    '''
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
