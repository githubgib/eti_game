// Declarative Pipeline
pipeline {
    // Set up the docker agent the jenkins slave will run on
    //  agent { docker { image 'python:3.8' } }
    agent { dockerfile true  }

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
                // Pytest here
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                // Key in some values to test the game here, manual inputs.. etc!
                // sh 'python3 game.py'
            }
        }
    }
}

// Scripted Pipeline
// node{
//     Stage 'Checkout'
//         echo 'Checkout Stage'
//         checkout scm

//     Stage 'Build'
//         echo 'Building Stage'
//         sh 'python --version'
//         sh 'python3 Game/py_compileCheck.py'

//     Stage 'Test'
//         echo 'Test Stage'
//         //Pytest here

//     Stage 'Deploy'
//         echo 'Test Stage'

// }