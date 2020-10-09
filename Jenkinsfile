pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Test') {
            agent { dockerfile true }
            steps {
                sh 'pytest --html test-reports/results.html app/test_api.py'
            }
            post {
                always {
                    'test-reports/results.html'
                }
            }
        }
    }
}