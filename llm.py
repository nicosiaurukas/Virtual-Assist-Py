import openai
import json

#Clase para utilizar cualquier LLM para procesar un texto
#Y regresar una funcion a llamar con sus parametros
#Uso el modelo 0613, pero puedes usar un poco de
#prompt engineering si quieres usar otro modelo
class LLM():
    def __init__(self):
        pass
    
    def process_functions(self, text):
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=[
                    #Aca podras cambiar que actitud toma el asistente
                    {"role": "system", "content": "Eres un asistente amable"},
                    {"role": "user", "content": text},
            ], functions=[
                {
                    "name": "get_weather",
                    "description": "Obtener el clima actual",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "ubicacion": {
                                "type": "string",
                                "description": "La ubicación, debe ser una ciudad",
                            }
                        },
                        "required": ["ubicacion"],
                    },
                },
                {
                    "name": "send_email",
                    "description": "Enviar un correo",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "recipient": {
                                "type": "string",
                                "description": "La dirección de correo que recibirá el correo electrónico",
                            },
                            "subject": {
                                "type": "string",
                                "description": "El asunto del correo",
                            },
                            "body": {
                                "type": "string",
                                "description": "El texto del cuerpo del correo",
                            }
                        },
                        "required": [],
                    },
                },
                {
                    "name": "open_chrome",
                    "description": "Abrir el explorador Chrome en un sitio específico",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "website": {
                                "type": "string",
                                "description": "El sitio al cual se desea ir"
                            }
                        }
                    }
                },
                {
                    "name": "open_discord",
                    "description": "Abrir la aplicacion de Discord",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "website": {
                                "type": "string",
                                "description": "Con quien deseas hablar"
                            }
                        }
                    }
                },
                {
                    "name": "open_spotify",
                    "description": "Abrir la aplicacion de Spotify",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "website": {
                                "type": "string",
                                "description": "La cancion que deseas escuchar"
                            }
                        }
                    }
                },                
                {
                    "name": "open_visual_studio_code",
                    "description": "Abrir la aplicacion de Microsoft Visual Studio Code",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "website": {
                                "type": "string",
                                "description": "La cancion que deseas escuchar"
                            }
                        }
                    }
                },
                {
                    "name": "open_whatsapp",
                    "description": "Abrir Whatsapp",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "website": {
                                "type": "string",
                                "description": "Con quien deseas hablar"
                            }
                        }
                    }
                },
                {
                    "name": "open_programs",
                    "description": "Abrir las aplicaciones diarias que utilizas",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "website": {
                                "type": "string",
                                "description": "Las aplicaciones diarias que usas"
                            }
                        }
                    }
                }
            ],
            function_call="auto",
        )
        
        message = response["choices"][0]["message"]
        
        #Nuestro amigo GPT quiere llamar a alguna funcion?
        if message.get("function_call"):
            #Sip
            function_name = message["function_call"]["name"] #Que funcion?
            args = message.to_dict()['function_call']['arguments'] #Con que datos?
            print("Funcion a llamar: " + function_name)
            args = json.loads(args)
            return function_name, args, message
        
        return None, None, message
    
    #Una vez que llamamos a la funcion (e.g. obtener clima, encender luz, etc)
    #Podemos llamar a esta funcion con el msj original, la funcion llamada y su
    #respuesta, para obtener una respuesta en lenguaje natural (en caso que la
    #respuesta haya sido JSON por ejemplo
    def process_response(self, text, message, function_name, function_response):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=[
                #Aqui tambien puedes cambiar como se comporta
                {"role": "system", "content": "Eres un asistente amable"},
                {"role": "user", "content": text},
                message,
                {
                    "role": "function",
                    "name": function_name,
                    "content": function_response,
                },
            ],
        )
        return response["choices"][0]["message"]["content"]
