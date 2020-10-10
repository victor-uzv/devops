pipeline {
    environment {
        registry = "deadlike/app-python"
        registryCredentials = 'deadlike'
        dockerImage = ''
    }
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Run app tests') {
            agent { dockerfile true }
            steps {
                sh 'pytest -svvv app/test_api.py'
            }
        }
        stage('Clone app repo') {
           agent any
           steps {
                script {
                    git 'https:///github.com/victor-uzv/devops'
                }
           }
        }
        stage('Build app image') {
           agent any
           steps {
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
           }
        stage('Deploy app image to dockerhub') {
          agent any
          steps {
               script {
                    docker.withRegistry( '', registryCredentials) {
                        dockerImage.push()
                    }
               }
          }
        stage('Clean up') {
         agent any
         steps {
                sh "docker rmi $registry:$BUILD_NUMBER"
              }
         }
    }
}