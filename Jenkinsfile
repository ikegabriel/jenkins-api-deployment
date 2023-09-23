pipeline {
    agent any

    environment{
        SCANNER_HOME= tool 'sonar-scanner'
        AWS_CLUSTER_NAME='DJANGO-CLUSTER'
        AWS_LAUNCH_TYPE='FARGATE'
    }

    stages {
        stage('Git Checkout') {
            steps {
                git branch: 'main', changelog: false, credentialsId: 'b8e9a50d-d47b-4fab-9aa6-20a030b97eae', poll: false, url: 'https://github.com/ikegabriel/jenkins-api-deployment.git'
            }
        }
        
        stage('Quality Scan') {
            steps {
                withSonarQubeEnv('sonar-server') {
                    sh ''' $SCANNER_HOME/bin/sonar-scanner -Dsonar.projectName=Django-Api \
                    -Dsonar.java.binaries=. \
                    -Dsonar.projectKey=Django-api '''
                }
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
                    sh '. ./test.sh'
                }
                
            }
        }
        
        stage('Docker Build & Push') {
            steps {
                script{
                    withDockerRegistry(credentialsId: 'ce1c36b2-5c54-42ac-940e-0372d929ec2d', toolName: 'docker') {
                        sh 'docker build -t ikegabrielez/django-api:latest .'
                        sh 'docker push ikegabrielez/django-api:latest'
                    }
                sh 'docker ps'
                
            }
        }
        
        stage('Deployment Approval Dev'){
            steps{
                input(message: 'Do you want to deploy this version to Dev?', ok: 'Deploy')
            }
        }
        
        stage('Deploy To Dev') {
            steps {
                withCredentials([string(credentialsId: 'a0a700c7-8a60-4654-8b36-ef6dfcc3b6fe', variable: 'SECRET_ACCESS_KEY'),
                string(credentialsId: '2e701915-c12e-4259-87bd-d69b33737eac', variable: 'ACCESS_KEY_ID'),
                string(credentialsId: 'cb509d99-cd5c-490e-a791-ed7e86b3f810', variable: 'TASK_ARN')]) {
                    
                    sh 'aws configure set aws_access_key_id $ACCESS_KEY_ID'
                    sh 'aws configure set aws_secret_access_key $SECRET_ACCESS_KEY'
                    sh 'aws configure set region us-east-1'
                    sh 'aws configure list'

                    sh ''' aws ecs run-task \
                            --cluster $AWS_CLUSTER_NSME \
                            --launch-type $AWS_LAUNCH_TYPE \
                            --task-definition $TASK_ARN '''
                }
            }
        }
        
        stage('Deployment Approval QA'){
            steps{
                input(message: 'Do you want to deploy this version to QA?', ok: 'Deploy')
            }
        }
        
        stage('Deploy To QA') {
            steps {
                sh 'docker ps'
            }
        }
        
        stage('Deployment Approval Prod'){
            steps{
                input(message: 'Do you want to deploy this version to Prod?', ok: 'Deploy')
            }
        }
        
        stage('Deploy To Prod'){
            steps{
                sh 'printenv'
            }
        }
        
    }
}
