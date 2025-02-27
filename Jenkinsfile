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
                container('kaniko') {
                    sh '''
                        /kaniko/executor --context `pwd` \
                        --destination=${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG} \
                        --dockerfile=Dockerfile
                    '''
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
