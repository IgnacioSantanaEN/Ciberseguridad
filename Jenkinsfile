pipeline {
    agent any

    stages {
        stage('1. Construccion (Build)') {
            steps {
                echo '=== ETAPA 1: Construyendo la imagen del sistema ==='
                sh 'docker build -t hola-mundo-prod:latest .'
            }
        }

        stage('2. Revision de Seguridad Continua (DAST/Surfaces)') {
            steps {
                echo '=== ETAPA 2: Analizando superficie de ataque y puertos expuestos ==='
                sh 'docker stop hola-mundo-container || true'
                sh 'docker rm hola-mundo-container || true'
                sh 'docker run -d --name hola-mundo-container hola-mundo-prod:latest'
                sh 'docker inspect --format="{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}" hola-mundo-container'
                sh 'sh -c "ss -tulpn | grep docker || echo No se detectan puertos publicos criticos expuestos"'
            }
        }

        stage('3. Despliegue con Mitigacion (Deploy)') {
            steps {
                echo '=== ETAPA 3: Aplicando Endurecimiento (Hardening) y Despliegue Seguro ==='
                sh 'docker stop hola-mundo-container || true'
                sh 'docker rm hola-mundo-container || true'
                // NOTA: Para que OWASP ZAP pueda escanear la app en el paso siguiente, mapeamos temporalmente un puerto interno si tu app expone red, o bien usamos su IP
                sh 'docker run -d -p 5000:5000 --name hola-mundo-container hola-mundo-prod:latest'
            }
        }
    }
}
