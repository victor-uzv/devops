pipeline {
    environment {
        registry = "deadlike/app-python"
        registryCredentials = 'deadlike'
        buildVersion = 'latest'
        dockerImage = ''
        gcpProjectId = 'victoru'
        gcpClusterName = 'python-app-cluster'
        gcpLocation = 'europe-west3'
        gcpCredentialsId = 'victorusa'
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
                    dockerImage = docker.build(registry + ":${buildVersion}", "-f ${WORKSPACE}/app/Dockerfile .")
                }
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
        }
        stage('Clean up app image') {
         agent any
         steps {
                sh "docker rmi $registry:${buildVersion}"
              }
         }
        stage('Deploy app to GKE') {
         agent any
         steps {
             step([
             $class: 'KubernetesEngineBuilder',
             projectId:  gcpProjectId,
             clusterName: gcpClusterName,
             location: gcpLocation,
             manifestPattern: 'manifest.yaml',
             credentialsId: gcpCredentialsId,
             verifyDeployments: true])
            }
        }
    }
}