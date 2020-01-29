pipeline {
    // Set up the docker agent the jenkins slave will run on
     agent { docker { image 'python:3.5.1' } }

    // Write out what happens each stage
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python --version'
                sh 'pip install -r requirements.txt'
                sh 'python3 /Game/py_compileCheck.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                // Pytest here
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh 'python3 /Game/game.py'
            }
        }
    }
}