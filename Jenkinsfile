pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Test') {
            agent { dockerfile true }
            steps {
                sh 'pytest --junit-xml test-reports/results.xml app/tests/test_api.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}