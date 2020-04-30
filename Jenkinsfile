pipeline {
  agent any
  stages {
    stage('Lint') {
      steps {
        echo 'Checking Lint...'
        sh 'make lint'
      }
    }
    stage('Build Docker') {
      steps {
        sh 'make build'
      }
    }
    stage('Push image') {
      steps {
        sh 'make upload'
      }
    }
    stage('set current kubectl context') {

    }

    stage('Deploy container') {

    }
    
  }
}