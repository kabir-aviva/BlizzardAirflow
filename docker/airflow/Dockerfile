# 1. Usar la imagen base con Airflow 3.0.2 y Python 3.12.
FROM apache/airflow:3.0.2-python3.12

# 2. Cambiar a usuario root para instalar paquetes del sistema.
USER root

# 3. Instalar el SDK de Google Cloud (que incluye gsutil).
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        gnupg && \
    echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg && \
    apt-get update && \
    apt-get install -y google-cloud-sdk && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# 4. Volver al usuario de bajos privilegios 'airflow' por seguridad.
USER airflow

# 5. Copiar nuestro archivo de requerimientos hacia dentro de la imagen.
COPY requirements.txt .

# 6. Instalar las dependencias de Python.
RUN pip install --no-cache-dir -r requirements.txt