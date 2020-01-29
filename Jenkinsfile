pipeline {
    // Set up the docker agent the jenkins slave will run on
     agent { docker { image 'python:3.5.1' } }

    // Write out what happens each stage
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python --version'
                sh 'python3 py_compileCheck.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh 'python3 game.py'
            }
        }
    }
}