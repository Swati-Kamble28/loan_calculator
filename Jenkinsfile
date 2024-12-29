pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Display a message in the Stage View
                bat 'echo Starting Build Stage...'

                // Run the Loan Calculator script
                bat 'python src/loan_calculator.py'

                // Notify completion of the stage
                bat 'echo Build Stage Completed.'
            }
        }
    }

    post {
        success {
            // Success message visible in Stage View
            echo 'Build completed successfully!'
        }
        failure {
            // Failure message visible in logs
            echo 'Build failed. Please check the logs.'
        }
    }
}
