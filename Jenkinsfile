pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Test') {
            agent { dockerfile true }
            steps {
                sh 'ls -lahtr'
            }
        }
    }
}