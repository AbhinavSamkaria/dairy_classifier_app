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
                    docker.build(dairy_classifier_app-streamlit-app)
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh "docker rm -f ${dairy-classifier} || true"
                    sh """
                        docker run -d --name ${dairy-classifier} \\
                        -p 8501:8501 ${dairy_classifier_app-streamlit-app:latest}
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
