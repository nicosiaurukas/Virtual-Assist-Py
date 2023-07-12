import os
import openai
from dotenv import load_dotenv
from flask import Flask, render_template, request
import json
from transcriber import Transcriber
from llm import LLM
from weather import Weather
from tts import TTS
from pc_command import PcCommand

#Cargar llaves del archivo .env
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
elevenlabs_key = os.getenv('ELEVENLABS_API_KEY')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("recorder.html")

@app.route("/audio", methods=["POST"])
def audio():
    #Obtener audio grabado y transcribirlo
    audio = request.files.get("audio")
    text = Transcriber().transcribe(audio)
    
    #Utilizar el LLM para ver si llamar una funcion
    llm = LLM()
    function_name, args, message = llm.process_functions(text)
    #while function_name is not None:
    if function_name is not None:
        #Si se desea llamar una funcion de las que tenemos
        if function_name == "get_weather":
            #Llamar a la funcion del clima
            function_response = Weather().get(args["ubicacion"])
            function_response = json.dumps(function_response)
            print(f"Respuesta de la funcion: {function_response}")
            
            final_response = llm.process_response(text, message, function_name, function_response)
            tts_file = TTS().process(final_response)
            return {"result": "ok", "text": final_response, "file": tts_file}
        
        elif function_name == "send_email":
            #Llamar a la funcion para enviar un correo
            final_response = "Tu que estas leyendo el codigo, implementame y envia correos muahaha"
            tts_file = TTS().process(final_response)
            return {"result": "ok", "text": final_response, "file": tts_file}
        
        elif function_name == "open_chrome":
            PcCommand().open_chrome(args["website"])
            final_response = "Listo, ya abrí chrome en el sitio " + args["website"]
            tts_file = TTS().process(final_response)
            return {"result": "ok", "text": final_response, "file": tts_file}
        
        elif function_name == "open_discord":
            PcCommand().open_discord()
            final_response = "Listo, ya abrí la app de Discord. ¿Deseas abrir otra aplicación?  "
            tts_file = TTS().process(final_response)
            return {"result": "ok", "text": final_response, "file": tts_file, "listen_again": True}
        
        elif function_name == "open_spotify":
            PcCommand().open_spotify()
            final_response = "Listo, ya abrí la app de Spotify. ¿Deseas abrir otra aplicación? "
            tts_file = TTS().process(final_response)
            return {"result": "ok", "text": final_response, "file": tts_file, "listen_again": True}
    
        elif function_name == "open_visual_studio_code":
            PcCommand().open_visual_studio_code()
            final_response = "Listo, ya abrí la app de Vs Code. ¿Deseas abrir otra aplicación?  "
            tts_file = TTS().process(final_response)
            return {"result": "ok", "text": final_response, "file": tts_file, "listen_again": True}
        
        elif function_name == "open_whatsapp":
            PcCommand().open_whatsapp()
            final_response = "Listo, ya abrí Whatsapp. ¿Deseas abrir otra aplicación? "
            tts_file = TTS().process(final_response)
            return {"result": "ok", "text": final_response, "file": tts_file, "listen_again": True}
        
        elif function_name == "open_programs":
            PcCommand().open_programs()
            final_response = "Listo, ya procedo a abrir discord, notepad++ y chrome con lo solicitado. ¿Deseas abrir otra aplicación?  "
            tts_file = TTS().process(final_response)
            return {"result": "ok", "text": final_response, "file": tts_file, "listen_again": True}
        
        
    else:
        final_response = "No tengo idea de lo que estás hablando. ¿Deseas abrir alguna aplicación?"
        tts_file = TTS().process(final_response)
        return {"result": "ok", "text": final_response, "file": tts_file, "listen_again": True}
    
    #llm = LLM()
    #function_name, args, message = llm.process_functions(text)