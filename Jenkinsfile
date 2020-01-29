pipeline {
    // Set up the docker agent the jenkins slave will run on
     agent { docker { image 'python:3.5.1' } }

    // Write out what happens each stage
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                echo 'Python Version'
                sh 'python --version'
                sh 'python -m py_compile game.py'
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
            }
        }
    }
}