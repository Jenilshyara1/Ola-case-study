pipeline {
	agent any
	    stages {
	        stage('Clone Repository') {
	        /* Cloning the repository to our workspace */
	        steps {
	        checkout scm
	        }
	   }
	   stage('Build') {
	        steps {
	        bat 'docker-compose build'
	        }
	   }
	   stage('Deploy') {
	        steps {
	        bat 'docker-compose -d up'
	        }
	   }
	   stage('Testing'){
	        steps {
	            echo 'Testing..'
	            }
	   }
    }
}
