pipeline {
    agent any

    environment {
        VERSION = "1.0.${BUILD_NUMBER}" // Dynamic versioning
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the repository...'
                // Replace this line with your SVN checkout
                svn 'https://svn.mycorp/trunk/'
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building the project...'
                // Run the build command (make all)
                sh 'make all'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running tests...'
                // Run the test command (make test)
                sh 'make test'
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo 'Setting up Python environment...'
                bat '''
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                bat '''
                    python -m pytest tests/ --junitxml=test-results.xml
                '''
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }

        stage('Build Artifact') {
            steps {
                bat '''
                    mkdir artifacts
                    echo ${VERSION} > artifacts\\version.txt
                    python -c "import shutil; shutil.make_archive('artifacts\\\\loan_calculator_${VERSION}', 'zip', 'src')"
                '''
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'artifacts/*.zip', fingerprint: true
                echo 'Artifact archived successfully.'
            }
        }
    }

    post {
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed.'
        }
    }
}


