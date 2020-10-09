pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Test') {
            agent { dockerfile true }
            steps {
                sh 'pytest -svvv app/test_api.py'
            }
        }
    }
}