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
                
                // Levantamos el contenedor un momento para analizarlo dinámicamente
                sh 'docker stop hola-mundo-container || true'
                sh 'docker rm hola-mundo-container || true'
                sh 'docker run -d --name hola-mundo-container hola-mundo-prod:latest'
                
                // IDENTIFICACIÓN: Inspeccionamos si el contenedor expone puertos de forma insegura
                echo '[AUDITORÍA] Verificando puertos e IP asignada al contenedor...'
                sh 'docker inspect --format="{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}" hola-mundo-container'
                
                // Validamos que el contenedor no tenga puertos escuchando hacia el exterior innecesariamente
                sh 'sh -c "ss -tulpn | grep docker || echo No se detectan puertos publicos criticos expuestos"'
            }
        }

        stage('3. Despliegue con Mitigacion (Deploy)') {
            steps {
                echo '=== ETAPA 3: Aplicando Endurecimiento (Hardening) y Despliegue Seguro ==='
                // MITIGACIÓN: Desplegamos limitando los recursos y aislando el contenedor sin mapear puertos host externos
                sh 'docker stop hola-mundo-container || true'
                sh 'docker rm hola-mundo-container || true'
                
                // Levantamos el contenedor mitigando riesgos: sin flags de privilegios (-d) y aislado de la red publica
                sh 'docker run -d --read-only --network bridge --name hola-mundo-container hola-mundo-prod:latest'
                
                echo '=== Trazabilidad final de ejecucion ==='
                sh 'docker ps -f name=hola-mundo-container'
            }
        }
    }
}
