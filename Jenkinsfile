pipeline {
    agent any

    environment {
        VERSION = '1.0.0' // Example version; adjust as needed
    }

    stages {
        stage('Start') {
            steps {
                echo 'Pipeline started by user.'
            }
        }

        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Checkout') {
            steps {
                echo 'Checking out the repository...'
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo 'Setting up Python environment...'
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                bat 'python -m pytest tests/ --junitxml=test-results.xml'
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }

        stage('Build Artifact') {
    steps {
        echo 'Building artifact...'
        script {
            if (!fileExists('artifacts')) {
                bat 'mkdir artifacts'
            }
        }
        bat 'echo ${VERSION} > artifacts/version.txt'
        bat '7z a artifacts/loan_calculator_${VERSION}.zip src\\*'
    }
}

        stage('Archive Artifacts') {
            steps {
                echo 'Archiving artifacts...'
                archiveArtifacts artifacts: 'artifacts/loan_calculator_${VERSION}.zip', fingerprint: true
            }
        }

        stage('Post Actions') {
            steps {
                echo 'Post-build actions...'
            }
        }
    }

    post {
        always {
            echo 'End of Pipeline'
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
