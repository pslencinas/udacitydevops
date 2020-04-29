pipeline {
  agent any
  stages {
    stage('Lint') {
      steps {
        sh 'make lint'
      }
    }
    stage('Build Docker') {
      steps {
        sh 'make build'
      }
    }
    stage('Login to dockerhub') {
      steps {
        withCredentials([string(credentialsId: 'docker-pwd', variable: 'dockerhubpwd')]) {
          sh 'docker login -u pslencinas -p ${dockerhubpwd}'
        }
      }
    }
    stage('Upload Image') {
      steps {
        sh 'make upload'
      }
    }
    
  }
}