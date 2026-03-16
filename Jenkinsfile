pipeline {
  agent any

  stages {

    stage('Clone Repo') {
      steps {
        git 'https://github.com/user/devops-app.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t devops-app .'
      }
    }

    stage('Tag Image') {
      steps {
        sh 'docker tag devops-app:latest <ECR_URL>/devops-app:latest'
      }
    }

    stage('Push to ECR') {
      steps {
        sh 'docker push <ECR_URL>/devops-app:latest'
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
