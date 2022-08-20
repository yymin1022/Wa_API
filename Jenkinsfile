pipeline {
    agent any

    stages {
        stage("Set Variable") {
            steps {
                script {
                    DOCKERHUB_CREDENTIAL = credentials("dockerhub-yymin1022")
                    DOCKER_IMAGE_NAME = "wa-api"
                    DOCKER_IMAGE_STORAGE = "yymin1022"
                }
            }
        }

        stage("Build Docker Image") {
            steps {
                script {
                    image = docker.build("${DOCKER_IMAGE_STORAGE}/${DOCKER_IMAGE_NAME}")
                }
            }
        }

        stage("Push Docker Image to Dockerhub") {
            steps {
                script {
                    docker.withRegistry('https://hub.docker.com', "dockerhub-yymin1022") {
                        image.push()
                    }
                }
            }
        }
    }

}