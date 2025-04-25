pipeline {
    agent any

    environment {
        IMAGE_NAME = 'dairy-classifier'
        CONTAINER_NAME = 'dairy-classifier-container'
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo "Repository cloned automatically by Jenkins job"
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME} .'
            }
        }

        stage('Run Docker Container') {
            steps {
                // Stop and remove existing container if it's running
                sh """
                    docker rm -f ${CONTAINER_NAME} || true
                    docker run -d --name ${CONTAINER_NAME} -p 8501:8501 ${IMAGE_NAME}
                """
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
            echo 'Dairy Classifier app is running at http://localhost:8501'
        }
    }
}
