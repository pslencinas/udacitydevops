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

    stage('Upload Image') {
      steps {
        sh 'make upload'
      }
    }

  }
}