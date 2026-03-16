pipeline {
  agent any

  stages {

    stage('Clone Repo') {
      steps {
        git 'https://github.com/RushiPatil1881/17march2026.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t my-app .'
      }
    }

    stage('Tag Image') {
      steps {
        sh 'docker tag my-app:latest 339772065903.dkr.ecr.ap-south-1.amazonaws.com/my-app:latest' 
     }
    }

    stage('Push to ECR') {
      steps {
        sh 'docker push 339772065903.dkr.ecr.ap-south-1.amazonaws.com/my-app:latest'
      }
    }

    stage('Deploy to EKS') {
      steps {
        sh 'kubectl apply -f deployment.yaml'
        sh 'kubectl apply -f service.yaml'
      }
    }

  }
}
