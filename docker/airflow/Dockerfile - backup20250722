# 1. Usar la imagen base con Airflow 2.9.2 y Python 3.10.
FROM apache/airflow:2.9.2-python3.10

# 2. Asegurarnos de operar como el usuario de bajos privilegios 'airflow'.
USER airflow

# 3. Copiar nuestro archivo de requerimientos hacia dentro de la imagen.
COPY requirements.txt .

# 4. Instalar las dependencias listadas en el requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt