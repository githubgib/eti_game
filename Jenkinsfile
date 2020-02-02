// Declarative Pipeline
pipeline {
    // Set up the docker agent the jenkins slave will run on
    //  agent { docker { image 'python:3.8' } }
    agent { dockerfile true  }

    envrionment{
        VERSION_NO = '1.0'
        REGISTRY = "bchewy/eti_game"
        REGISTRY_CREDS = 'dockerhub'
        DOCKER_IMG = ''
    }

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
                // Run pytest and check coverage of explicit files to 90% Coverage.
                sh 'pytest  --cov --cov-fail-under 90'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                // Push to dockerhub image repository with tags per mergeid/featurebranch or etc.
                script{
                    DOCKER_IMG = docker.build("bchewy/eti_game:${env.VERSION_NO}")
                    docker.withRegistry('', REGISTRY_CREDS){
                        DOCKER_IMG.push()
                    }
                }
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