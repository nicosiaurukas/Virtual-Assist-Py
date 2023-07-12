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
Es importante reemplazar en el archivo pc_command.py, las rutas que correspondan a tus programas


El proyecto cuenta con algunas cosas que quizá quieras modificar, por ejemplo:


## Ejecución
- Este proyecto utiliza Flask. Puedes levantar el servidor en modo debug por defecto en el puerto 5000 con el comando
	- ```flask --app app run --debug```
	- En tu navegador ve a http://localhost:5000
	
