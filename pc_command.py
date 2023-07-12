from subprocess import call
import subprocess

#Clase para ejecutar comandos en la PC
#De momento esta en duro funcional para Windows hohoh
class PcCommand():
    def __init__(self):
        pass
    
    def open_chrome(self, website):
        website = "" if website is None else website
        #Funciona para windows, si quieres para otro, modificalo!! :D
        call("C:/Program Files/Google/Chrome/Application/chrome.exe " + website)

    def open_discord(self):
        comando = 'Discord'
        subprocess.Popen(["C:/Users/nicol/AppData/Local/Discord/app-1.0.9013/Discord.exe",  comando])

    def open_spotify(self):
        comando = 'Spotify'
        subprocess.Popen(["C:/Users/nicol/AppData/Local/Microsoft/WindowsApps/SpotifyAB.SpotifyMusic_zpdnekdrzrea0/Spotify.exe",  comando])    

    def open_visual_studio_code(self):
        command = 'code'

    def open_whatsapp(self):
        subprocess.Popen('whatsapp')
    
    def open_programs(self):
          
        #Open Discord
        subprocess.Popen(["C:/Users/nicol/AppData/Local/Discord/app-1.0.9013/Discord.exe"])

        #Open Notepad++
        subprocess.Popen(["C:/Program Files/Notepad++/notepad++.exe"])

        #Open Google Chrome - Con pestañas en Mail Cenco, Mail Personal, AWS, GitLab
        subprocess.Popen(["C:/Program Files/Google/Chrome/Application/chrome.exe ", "https://outlook.office365.com/mail/", 
                      "https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox",
                      "https://d-90675d22db.awsapps.com/start#/", 
                      "https://gitlab.com/cencosud-ds/cencommerce/post-purchase-experience/fulfilment/delivery/backend"])


      

