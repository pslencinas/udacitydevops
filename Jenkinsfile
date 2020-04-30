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
        withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
          sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
          sh "docker build -t pslencinas/myproject ."
          sh "docker tag pslencinas/myproject pslencinas/myproject"
        }
      }
    }
    stage('Push image') {
      steps {
        echo 'Pushing Image'
        sh "docker push pslencinas/myproject"
      }
    }
    // stage('set current kubectl context') {

    // }

    // stage('Deploy container') {

    // }
  }
}