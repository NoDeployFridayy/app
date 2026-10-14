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
                    sh 'python3 -m pip install -r requirements.txt'
                    sh 'python3 -m compileall -q app.py'
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
