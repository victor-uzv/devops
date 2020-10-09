pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Test') {
            agent { dockerfile true }
            steps {
                sh 'pytest -svvv --junit-xml test-reports/results.xml app/test_api.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}