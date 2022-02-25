# pyTelegramBotAPI
import telebot
import yaml


with open("bot_config.yaml", "r") as yamlfile:
    data = yaml.load(yamlfile, Loader=yaml.FullLoader)

API_KEY = data[0]['API_KEY']

enlaces = """ EIP : https://escuelaposgrado.ugr.es \n  
Web Máster : https://escuelaposgrado.ugr.es/datcom \n  
Resolución TFMs : https://escuelaposgrado.ugr.es/datcom/resolucionTFM \n 
Fechas EIP : https://escuelaposgrado.ugr.es/doctorado/estudiantes/calendario \n 
Calendario : https://secretariageneral.ugr.es/pages/calendariomasteres2122/\%21 \n"""

infoTFM = " propuesta consensuada -> formulario Google (profesor) CAM -> publicada en PRADO -> rellenar formulario (alumno)"

plazosTFM = """
------------------------------------------------------------
5. SOLICITUD DE CONVOCATORIA ESPECIAL Del 2 al 30 de noviembre de 2021 \n
rellenar formulario PRADO: 31 Diciembre y 15 de Mayo \n 
--------------------------------------------------------
\n Preasignación: \n
\n        Primer Plazo: hasta 17 de enero
\n
\n        Segundo Plazo: hasta 02 de mayo
\n
\n    Solicitud de asignación
\n
\n        Primer Plazo: 10-14 enero
\n        Segundo Plazo: 18-21 abril
\n
\n    Solicitud de evaluación
\n
\n        Convocatoria Especial: 10 Enero
\n        Convocatoria Julio: 26 Junio
\n        Convocatoria Septiembre: 2 Septiembre
\n
\n    Depósito
\n
\n        Convocatoria Especial: 17 Enero
\n        Convocatoria Julio: 04 Julio
\n        Convocatoria Septiembre: 05 Sept.
\n
\n    Defensa
\n
\n        Convocatoria Especial: 24-28 Enero
\n        Convocatoria Julio: 11-15 Julio
\n        Convocatoria Septiembre: 12-16 Sept.


"""

propuestasTFM = "\n Enlace a propuestas de TFMs: https://pradoposgrado2122.ugr.es/mod/url/view.php?id=56396"


plazosActas = """ 
"""

plazosEIP = """ 1. SOLICITUD DE RECONOCIMIENTO DE CRÉDITOS :  Del 20 de septiembre de 2021 al 25 de febrero de 2022 \n
\n
2. ANULACIÓN TOTAL DE MATRÍCULA   Del 20 de septiembre al 17 de diciembre de 2021 \n
\n
3. MODIFICACIÓN DE MATRÍCULA (anulación parcial o alteración) :\n
3.1 Asignaturas del primer semestre y anuales:  Del 27 de septiembre al 26 de octubre de 2021. Los estudiantes matriculados con 
posterioridad al 22 de octubre tendrán un plazo de un mes desde su fecha de matrícula. \n
3.2 Asignaturas del segundo semestre: Del 12 de enero al 25 de febrero de 2022 \n
 \n
4.  RENOVACIÓN DE MATRÍCULA  : Del 6 de septiembre al 31 de octubre de 2021 \n
 \n
 5.  SOLICITUD DE CONVOCATORIA ESPECIAL : Del 2 al 30 de noviembre de 2021 \n
 \n 
6. SOLICITUD DE CAMBIO DE MODALIDAD DE DEDICACIÓN DE ESTUDIOS : Del 20 de septiembre al 30 de noviembre de 2021 \n
"""


# print(API_KEY)

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start', 'help', 'hola', 'ayuda'])
def send_welcome(message):
	bot.reply_to(message, "Este bot tiene como fin ayudar al alumnado para resolver dudas de plazos y cuestiones relacionadas con el máster, para enviar sugerencias, escriba a coordina.datcom@ugr.es. Los comandos que puede usar son: \n enlaces \n TFM \n plazosEIP \n plazosActas")


@bot.message_handler(commands=['enlaces'])
def send_links(message):
	bot.reply_to(message, enlaces)


@bot.message_handler(commands=['TFM'])
def send_TFM(message):
	bot.reply_to(message, infoTFM + plazosTFM + propuestasTFM)

@bot.message_handler(commands=['plazosEIP'])
def send_TFM(message):
	bot.reply_to(message, plazosEIP)

@bot.message_handler(commands=['plazosActas'])
def send_TFM(message):
	#bot.reply_to(message, './CalendarioActas_2021-22.png')
	bot.send_photo(message.chat.id, photo=open('./CalendarioActas_2021-22.png', 'rb'))



bot.infinity_polling()