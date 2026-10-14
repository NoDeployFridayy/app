pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install and validate') {
            steps {
                dir('demo-app') {
                    sh 'python -m pip install -r requirements.txt'
                    sh 'python -m compileall -q app.py'
                }
            }
        }

        stage('Build Docker image') {
            steps {
                dir('demo-app') {
                    sh 'docker build -t my-app:latest .'
                }
            }
        }
    }
}
