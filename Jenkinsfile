pipeline {
    agent any

    environment {
        IMAGE_NAME = 'dairy-classifier'
        CONTAINER_NAME = 'dairy-classifier-container'
    }

    stages {
        stage('Clone Repository') {
            steps {
                // If using Jenkins with Git, clone is automatic if configured properly
                echo "Repository cloned automatically by Jenkins job"
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build(IMAGE_NAME)
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh "docker rm -f ${CONTAINER_NAME} || true"
                    sh """
                        docker run -d --name ${CONTAINER_NAME} \\
                        -p 8501:8501 ${IMAGE_NAME}
                    """
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        failure {
            echo 'Pipeline failed.'
        }
        success {
            echo 'Dairy Classifier app is up and running at http://localhost:8501'
        }
    }
}
