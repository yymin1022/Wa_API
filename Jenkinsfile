pipeline {
    agent any

    stages {
        stage("Set Variable") {
            steps {
                script {
                    IMAGE_NAME = "wa-api"
                    IMAGE_STORAGE = "yymin1022"
                }
            }
        }

        stage("Build Docker Image") {
            steps {
                script {
                    image = docker.build("${IMAGE_STORAGE}/${IMAGE_NAME}")
                }
            }
        }
    }

}