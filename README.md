# README: Guía de Descarga y Pruebas para Bitwizards
Proyecto de mantenimiento para el proyecto BitWizards de la materia Software lll

## Pasos para Descargar e Instalar

1. **Clona el Repositorio:**
   ```
   git clone https://github.com/BitWizards-Software3/scraphone-backend
   ```

2. **Accede al Directorio del Proyecto:**
   ```
   cd scraphone-backend
   ```

3. **Crea el ambiente:**
   ```
   python -m venv venv
   \venv\Scripts\activate
   ```

4. **Configura la Base de Datos:**
   - Utiliza el archivo `config/database.py` para establecer la conexión a tu base de datos local.

## Ejecución del Programa

1.  **Ejecuta el siguiente comando para correr el proyecto:**
     ```
     uvicorn main:app --reload
     ```
2. **Accede al Programa en tu Navegador:**
   - Abre tu navegador y visita `http://localhost:3000` para interactuar con el backend de Scraping.

## Pruebas Unitarias

1. **Instala las Dependencias de Desarrollo:**
   ```
   npm install --save-dev
   ```

2. **Ejecuta las Pruebas Unitarias:**
   ```
   npm test
   ```


