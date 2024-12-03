pipeline {
    agent any
    tools {
        maven 'Maven3'
    }
    environment {
        registry = "863518437070.dkr.ecr.us-east-2.amazonaws.com/pet-care-tcc-ads"
        region = "us-east-2"
        githubRepo = 'https://github.com/Elaine-cls/tcc-vanessa.git'
        dockerImageTag = "latest"
    }
    stages {
        stage('Clone Git Repository') {
            steps {
                checkout scm: [
                    $class: 'GitSCM',
                    branches: [[name: '*/develop']],
                    userRemoteConfigs: [[
                        url: githubRepo
                    ]]
                ]
            }
        }
        stage('Build Application') {
            steps {
                sh 'mvn clean install'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImageTag = "${BUILD_NUMBER}"
                    dockerImage = docker.build("${registry}:${dockerImageTag}")
                }
            }
        }
        stage('Push Docker Image to ECR') {
            steps {
                script {
                    sh """
                    aws ecr get-login-password --region $region | docker login --username AWS --password-stdin $registry
                    docker push ${registry}:${dockerImageTag}
                    """
                }
            }
        }
       stage('Update Kubernetes Deployment') {
            steps {
                script {
                    // Defina o nome da imagem com a tag gerada pelo build
                    def imageName = "${registry}:${dockerImageTag}"

                    // Atualize a imagem no deployment do Kubernetes
                    sh """
                    kubectl set image deployment/pet-care-app pet-care-app=${imageName} --namespace pet-care-app
                    kubectl rollout status deployment/pet-care-app --namespace pet-care-app
                    """
                }
            }
        }
    }
    post {
        always {
            cleanWs() // Limpa o workspace ao final da execução
        }
        success {
            echo "Pipeline executed successfully!"
        }
        failure {
            echo "Pipeline failed. Check logs for more details."
        }
    }
}
