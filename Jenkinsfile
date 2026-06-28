pipeline {
    agent any

    stages {
        stage('1. Construccion (Build)') {
            steps {
                echo 'Construyendo entorno Docker...'
                sh 'docker build -t hola-mundo-prod:latest .'
            }
        }

        stage('2. Despliegue (Deploy)') {
            steps {
                echo 'Desplegando aplicacion de manera persistente...'
                // Detener contenedor viejo si existe
                sh 'docker stop hola-mundo-container || true'
                sh 'docker rm hola-mundo-container || true'
                
                // Levantar el script original manteniendolo vivo para auditoria
                sh 'docker run -d --name hola-mundo-container hola-mundo-prod:latest'
            }
        }

        stage('3. Pruebas (Testing)') {
            steps {
                echo '[TEST] verificando que el contenedor este activo...'
                sh 'docker ps -f name=hola-mundo-container'
                
                echo '[TEST] Verificando los logs internos de la aplicacion...'
                sh 'docker logs hola-mundo-container | grep "HOLA MUNDO PYTHON"'
            }
        }
    }
}
