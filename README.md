# README: Guía de Descarga y Pruebas para Bitwizards
Proyecto de mantenimiento para el proyecto BitWizards de la materia Software lll

## Pasos para Descargar e Instalar

1. **Clona el Repositorio:**
   ```
   git clone [URL del repositorio]
   ```

2. **Accede al Directorio del Proyecto:**
   ```
   cd [nombre-del-proyecto]
   ```

3. **Instala las Dependencias:**
   ```
   npm install
   ```

4. **Configura la Base de Datos:**
   - Utiliza el archivo `config/database.config.js` para establecer la conexión a tu base de datos local.

   - Ejecuta el siguiente comando para crear las tablas necesarias:
     ```
     npm run migrate
     ```

   - (Opcional) Si deseas poblar la base de datos con datos de prueba, ejecuta:
     ```
     npm run seed
     ```

## Ejecución del Programa

1. **Inicia el Servidor:**
   ```
   npm start
   ```

2. **Accede al Programa en tu Navegador:**
   - Abre tu navegador y visita `http://localhost:3000` para interactuar con [Nombre del Programa].

## Pruebas Manuales

Realiza las siguientes pruebas manuales para garantizar el correcto funcionamiento del programa:

- [ ] Registro de Usuario
- [ ] Inicio de Sesión
- [ ] Creación, Lectura, Actualización y Eliminación (CRUD) de Datos
- [ ] Funcionalidades Específicas [menciona las funcionalidades]

## Pruebas Unitarias

1. **Instala las Dependencias de Desarrollo:**
   ```
   npm install --save-dev
   ```

2. **Ejecuta las Pruebas Unitarias:**
   ```
   npm test
   ```

## Contribuciones

¡Apreciamos tus contribuciones! Si encuentras errores o mejoras, por favor, crea un *issue* o envía un *pull request*.



