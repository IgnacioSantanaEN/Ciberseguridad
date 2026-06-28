pipeline {
    agent any

    stages {
        stage('1. Build') {
            steps {
                echo 'Etapa 1: Construyendo la imagen Docker del Hola Mundo...'
                // Construye la imagen usando el Dockerfile de la carpeta actual
                sh 'docker build -t hola-mundo-prod:latest .'
            }
        }

        stage('2. Deploy Production) {
            steps {
                echo 'Etapa 2: Desplegando el entorno de produccion...'
                // Detiene y elimina contenedores anteriores si existen, y levanta el nuevo en el puerto 5000
                sh 'docker stop hola-mundo-container || true'
                sh 'docker rm hola-mundo-container || true'
                
                sh 'docker run -d --name hola-mundo-container hola-mundo-prod:latest'
            }
        }

        stage('3. Verify & Logs) {
            steps {
                echo 'Etapa 3: Verificando ejecucion y trazabilidad'
                sh 'docker ps'
                
                sh 'docker logs hola-mundo-container'
            }
        }
    }
}
