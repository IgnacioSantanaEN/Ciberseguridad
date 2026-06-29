pipeline {
    agent any

    stages {
        stage('1. Construccion (Build)') {
            steps {
                echo 'Construyendo entorno Docker...'
                sh 'docker build -t hola-mundo-prod:latest .'
            }
        }
        
        stage('2. Analisis Estatico (Linting)'){
            steps {
                echo 'Buscando vulnerabilidades de infraestructura...'
                sh 'docker run --rm -v \$(pwd):/root -w /root hadolint/hadolint hadolint Dockerfile || true'
            }
        }

        stage('3. Despliegue (Deploy)') {
            steps {
                echo 'Desplegando aplicacion de manera persistente...'
                // Detener contenedor viejo si existe
                sh 'docker stop hola-mundo-container || true'
                sh 'docker rm hola-mundo-container || true'
                
                // Levantar el script original manteniendolo vivo para auditoria
                sh 'docker run -d --name hola-mundo-container hola-mundo-prod:latest'
            }
        }
    }
}
