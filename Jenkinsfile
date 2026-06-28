pipeline {
    agent any

    stages {
        stage('1. Build Image') {
            steps {
                echo 'Construyendo entorno Docker...'
                sh 'docker build -t hola-mundo-prod:latest .'
            }
        }

        stage('2. Deploy Production') {
            steps {
                echo 'Desplegando aplicacion de manera persistente...'
                // Detener contenedor viejo si existe
                sh 'docker stop hola-mundo-container || true'
                sh 'docker rm hola-mundo-container || true'
                
                // Levantar el script original manteniendolo vivo para auditoria
                sh 'docker run -d --name hola-mundo-container hola-mundo-prod:latest'
            }
        }

        stage('3. Verify Trazability') {
            steps {
                echo 'Mostrando estado de ejecucion...'
                sh 'docker ps'
                sh 'docker logs hola-mundo-container'
            }
        }
    }
}