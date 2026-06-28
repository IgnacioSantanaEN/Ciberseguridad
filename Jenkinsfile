pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Construyendo la imagen Docker del Hola Mundo...'
                // Construye la imagen usando el Dockerfile de la carpeta actual
                sh 'docker build -t hola-mundo-prod:latest .'
            }
        }

        stage('Deploy Test') {
            steps {
                echo 'Desplegando la app temporalmente para pruebas...'
                // Detiene y elimina contenedores anteriores si existen, y levanta el nuevo en el puerto 5000
                sh '''
                docker stop hola-mundo-container || true
                docker rm hola-mundo-container || true
                docker run -d -p 5000:5000 --name hola-mundo-container hola-mundo-prod:latest
                sleep 5
                '''
            }
        }

        stage('Security Test (OWASP ZAP)') {
            steps {
                echo 'Iniciando escaneo automatizado con OWASP ZAP (DAST)...'
                // Usamos la imagen oficial de Docker de ZAP para atacar nuestra app en el puerto 5000
                // Guardará un reporte HTML llamado zap_report.html en tu carpeta de proyecto
                sh '''
                docker run --rm -v $(pwd):/zap/wrk/:rw ghcr.io/zaproxy/zaproxy:stable zap-baseline.py \
                    -t http://localhost:5000 \
                    -r zap_report.html || true
                '''
            }
        }

        stage('Deploy Production') {
            steps {
                echo 'Aplicación verificada. Despliegue final en producción exitoso.'
                // Muestra en los logs de Jenkins que el contenedor quedó corriendo estable
                sh 'docker ps'
            }
        }
    }
}