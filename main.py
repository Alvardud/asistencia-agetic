import requests
from datetime import datetime, time, timedelta
from telegram import Bot
import asyncio

# Token del bot de Telegram
TOKEN = "7186286901:AAGMi8mTCPTfW_a_Uki7AoP8SDi4UzBCftA"
# ID de chat al que enviar el mensaje
CHAT_ID = "288432726"

# APIS
TOKEN_URL = "https://intranet.agetic.gob.bo/personal/ws/api-token-auth/"
REGISTROS_URL = "https://intranet.agetic.gob.bo/personal/ws/proxy/api/v1/registros_usuario_dia"

user = None
password = None
token = None

horarios = {
    "monday": ["07:30", "12:30", "14:00", "18:30"],
    "tuesday": ["10:30", "12:30", "14:00", "17:30"],
    "wednesday": ["07:30", "12:30", "14:00", "17:30"],
    "thursday": ["07:30", "12:00", "14:00", "17:30"],
    "friday": ["07:30", "12:30", "14:00", "17:30"]
}


async def obtener_token():
    print('Ingresa a obtener token')
    global token
    if token is None:
        response = requests.post(TOKEN_URL, json={"username": user, "password": password})
        if response.status_code == 200:
            data = response.json()
            token = data["token"]
    return token

async def obtener_datos(token):
    print('Ingresa a obtener datos')
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    params = {"uid": user, "fecha": fecha_actual}
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(REGISTROS_URL, params=params, headers=headers)
    print(f'Solicitud: {REGISTROS_URL} params: {params} headers: {headers}')
    if response.status_code == 200:
        return response.json()
    if response.status_code == 401:
        tokenAcceso = await obtener_token()
        return await obtener_datos(tokenAcceso)
    return None

async def enviar_mensaje(datos):
    print('Ingresa a enviar mensaje')
    bot = Bot(token=TOKEN)
    mensaje = f"Datos obtenidos a las {datetime.now()}:\n"
    for registro in datos:
        mensaje += f"{registro['hora']}\n"
    await bot.send_message(chat_id=CHAT_ID, text=mensaje)
    
async def enviar_mensaje_simple(datos):
    print('Ingresa a enviar mensaje simple')
    bot = Bot(token=TOKEN)
    mensaje = f"Datos obtenidos a las {datetime.now()}:\n"
    mensaje += f"Execpcion ocurrida {datos}\n"
    await bot.send_message(chat_id=CHAT_ID, text=mensaje)
    
async def obtener_credenciales():
    global user, password
    user = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")

async def main():
    await obtener_credenciales()
    global token
    while True:
        try:
            print('Ingresa a algoritmo')
            ahora = datetime.now()
            dia_semana = ahora.strftime("%A").lower()
            if dia_semana in horarios:
                print('Ingresa a horario')
                for hora_str in horarios[dia_semana]:
                    hora = datetime.strptime(hora_str, "%H:%M").time()
                    inicio = datetime.combine(ahora.date(), hora) - timedelta(minutes=5)
                    fin = datetime.combine(ahora.date(), hora) + timedelta(minutes=35)
                    if inicio.time() <= ahora.time() <= fin.time():
                        datos = await obtener_datos(token)
                        print(f'Datos obtenidos {datos}')
                        if datos:
                            await enviar_mensaje(datos)
                    break
        except Exception as e:
            print(f"Error en el proceso principal: {e}")
            await enviar_mensaje_simple(e)
        await asyncio.sleep(600)  

if __name__ == "__main__":
    asyncio.run(main())