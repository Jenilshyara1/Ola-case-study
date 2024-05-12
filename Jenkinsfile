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
	        sh 'docker-compose build'
	        }
	   }
	   stage('Deploy') {
	        steps {
	        sh 'docker-compose up'
	        }
	   }
	   stage('Testing'){
	        steps {
	            echo 'Testing..'
	            }
	   }
    }
}
