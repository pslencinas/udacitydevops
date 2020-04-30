pipeline {
  agent any
  stages {
    stage('Checking out git repo') {
      steps{
        echo 'Checkout...'
        checkout scm
      }
    }
    stage('Checking environment') {
      steps{
        echo 'Checking environment...'
        sh 'git --version'
        sh 'docker -v'
      }
    }
    stage('Linting') {
      steps {
        echo 'Checking Lint...'
        sh 'hadolint Dockerfile'
        sh 'pylint --disable=R,C,W app.py'
      }
    }
    stage('Building Docker image') {
      steps {
        echo 'Building Docker image...'
        sh "sudo docker build -t pslencinas/myproject ."
        sh "sudo docker tag pslencinas/myproject pslencinas/myproject"
        
      }
    }
    stage('Pushing Docker image') {
      steps {
        echo 'Building Docker image...'
        withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
          sh "sudo docker push pslencinas/myproject"
          
        }
      }
    }
    
    // stage('set current kubectl context') {

    // }

    // stage('Deploy container') {

    // }
  }
}