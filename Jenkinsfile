pipeline {
    agent any

    stages {
        stage('Git Checkout') {
            steps {
                git branch: 'main', changelog: false, credentialsId: 'b8e9a50d-d47b-4fab-9aa6-20a030b97eae', poll: false, url: 'https://github.com/ikegabriel/jenkins-api-deployment.git'
            }
        }
        
        stage('Quality Scan') {
            steps {
                sh 'ls'
            }
        }
        
        
        stage('Configure Environment') {
            steps {
                sh 'python3 -m venv myenv'
                sh '. ./myenv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Test App') {
            steps {
                withCredentials([string(credentialsId: 'talent-secret-key', variable: 'SECRET_KEY')]) {
                    sh 'export SECRET_KEY=$SECRET_KEY'
                    sh 'python3 manage.py runserver 8000 &'
                    sh 'sleep 10'
                    sh 'curl http://localhost:8000/api/talent/'
                }
                
            }
        }
        
        stage('Docker Build & Push') {
            steps {
                sh 'ls'
            }
        }
        
        // stage('Test Dir') {
        //     steps {
        //         dir('backend/'){
        //             sh 'ls'
        //             withCredentials([string(credentialsId: 'talent-secret-key', variable: 'SECRET_KEY')]) {
        //             sh 'export SECRET_KEY=$SECRET_KEY'
        //             sh 'printenv'
        //         }
        //         }
        //     }
        // }
        // stage('OWASP Scan') {
        //     steps {
        //         dependencyCheck additionalArguments: '--scan ./', odcInstallation: 'dp'
        //         dependencyCheckPublisher pattern: '**/dependency-check-report.xml'
        //     }
        // }
        // stage('Test Env') {
        //     steps {
                
        //     }
        // }
    }
}