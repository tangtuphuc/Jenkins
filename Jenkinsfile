pipeline {
    agent any
    tools{
        maven 'local_maven'
        jdk 'local_jdk'
    }
    stages {
        stage('Stage Clone') {
            steps {
                    git branch: 'main', url: 'https://github.com/tangtuphuc/Jenkins.git'
            }
        }
        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }
        stage('Test') {
            steps {
                sh 'mvn test'
            }
        }
        stage('Scan')
        {
            steps{
                withSonarQubeEnv(installationName: 'server-sonar')
                sh './mvnw clean org.sonarsource.scanner.maven:sonar-maven-plugin:4.5.0.2216:sonar'
            }
        }
        stage('Deploy') {
            steps {
                deploy adapters: [tomcat9(credentialsId: 'Tomcat', path: '', url: 'http://4.194.27.233:8080/')], contextPath: null, war: '**/*.war'
                }
            }
        }
    }
