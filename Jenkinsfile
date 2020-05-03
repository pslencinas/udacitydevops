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
    // stage('Building Docker image') {
    //   steps {
    //     echo 'Building Docker image...'
    //     sh "sudo docker build -t pslencinas/myproject ."
    //     sh "sudo docker tag pslencinas/myproject pslencinas/myproject"
        
    //   }
    // }
    stage('Login Docker Hub') {
      steps {
        echo 'Login Docker Hub...'
        echo '${env.dockerHubUser}'
        sh "sudo docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
      }
    }
    stage('Pushing Docker image') {
      steps {
        echo 'Pushing Docker image...'
        sh 'sudo docker push pslencinas/myproject'
      }
    }
    stage('Deploying to EKS') {
      steps {
        echo 'Deploying to EKS...'
        
          sh "sudo aws eks --region us-west-2 update-kubeconfig --name CapstoneEKS-wQ75l4pMqesU"
          // sh "kubectl apply -f aws/aws-auth-cm.yaml"
          // sh "kubectl set image deployments/capstone-app capstone-app=pslencinas/myproject:latest"
          sh "kubectl apply -f aws/capstone-app-deployment.yml"
          sh "kubectl get nodes"
          sh "kubectl get pods"
      
          
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