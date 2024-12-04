pipeline {
    agent any
    environment {
        AWS_REGION = 'us-east-2'
        CLUSTER_NAME = 'k8s-cluster-tcc'
    }
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        stage('Configure EKS Access') {
            steps {
                sh '''
                    aws eks update-kubeconfig --region $AWS_REGION --name $CLUSTER_NAME
                    kubectl version --short
                '''
            }
        }
        stage('Deploy to EKS') {
            steps {
                script {
                    def kubernetesFiles = findFiles(glob: '.kubernetes/*.yml')
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
