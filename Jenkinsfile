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
                echo "Testing using Unittest..."
                sh "python3 -m unittest tests/test.py"
            }
        }
        stage('Code Analysis') {
            steps {
                echo "Code analysis using pylint"
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