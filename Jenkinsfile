pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo "Building using Docker..."
                sh "docker build -t square:latest -f ./Dockerfile ."
            }
        }
        stage('Test') {
            steps {
                echo "Testing using Selenium..."
                sh "pip install unittest"
                sh "python3 unittest -m tests/test.py"
            }
        }
        stage('Code Analysis') {
            steps {
                echo "Code analysis using pylint"
                sh "pip install pylint"
                sh "pylint src/main.py"
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying to Azure..."
            }
        }
        stage('Monitoring') {
            steps {
                echo "Running monitoring using New Relic..."
            }
        }
    }
}