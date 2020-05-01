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
        echo 'Pushing Docker image...'
        sh 'sudo make upload'
      }
    }
    stage('Deploying to EKS') {
      steps {
        echo 'Deploying to EKS...'
        dir('k8s') {
          withAWS(credentials: 'aws-credentials', region: 'eu-west-2') {
              sh "aws eks --region eu-west-2 update-kubeconfig --name capstone"
              sh 'kubectl apply -f capstone-k8s.yaml'
            }
          }
      }
    }
    stage("Cleaning up") {
      steps{
        echo 'Cleaning up...'
        sh "docker system prune -a"
      }
    }
   
  }
}