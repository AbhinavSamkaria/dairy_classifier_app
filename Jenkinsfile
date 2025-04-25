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
                bat "docker build -t %IMAGE_NAME% ."
            }
        }

        stage('Run Docker Container') {
            steps {
                bat """
                    docker rm -f %CONTAINER_NAME%
                    docker run -d --name %CONTAINER_NAME% -p 8601:8501 %IMAGE_NAME%
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
            echo 'Dairy Classifier app should be running at http://localhost:8501'
        }
    }
}
