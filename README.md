## Configuración
Para ejecutar el proyecto es necesario:
- Descargar el repositorio
- Instala las dependencias ejecutando 
	- ```  pip install -r requirements.txt ```
- Crea un archivo llamado ```.env```
	- En el archivo coloca las llaves:
	- ```OPENAI_API_KEY=XXXXXX```
	- ```ELEVENLABS_API_KEY=XXXXXX```
	- ```WEATHER_API_KEY=XXXXXX```

## Ajustes
Es importante reemplazar en el archivo pc_command.py, las rutas que correspondan a sus programas


El proyecto cuenta con algunas cosas que quizá quieras modificar, por ejemplo:

- En la clase LLM puedes modificar para que el asistente no sea "malhablado". Se utiliza en 2 lugares del archivo.
- En la clase PcCommand, abre Chrome buscándolo en una ruta fija para Windows. Puedes modificarlo para que busque el ejecutable en Mac / Linux.

## Ejecución
- Este proyecto utiliza Flask. Puedes levantar el servidor en modo debug por defecto en el puerto 5000 con el comando
	- ```flask --app app run --debug```
	- En tu navegador ve a http://localhost:5000
	
## Licencias
- Imagen de micrófono por Freepik
