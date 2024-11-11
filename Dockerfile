# Usar una imagen oficial de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de la aplicación en el contenedor
COPY . /app

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 5000 para acceder a la aplicación web
EXPOSE 5000

# Ejecutar la aplicación Flask
CMD ["python", "app.py"]
