pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'python src/loan_calculator.py'
            }
        }
    }
}
