import requests
import os
import random

# Lista de Seymour Diera versión Chilensis para Los Jenkins
frases = [
    "¿Se juega hoy? Sigo esperando aquí afuera, como siempre... ¿O ya se fueron a acostar, giles? 🐶",
    "¡Guau! Siento olor a vicio... ¿Alguien va a prender el server hoy o andan puro dando jugo? 🎮",
    "El Fry no está, pero ustedes sí po. ¿Sale su partida o les da amansadora? 🍕",
    "Esperaría mil años si fuera necesario, pero puta que sería bacán que jugáramos ahora. 🦴",
    "¿Se juega hoy o me quedo haciendo tuto en mi caja de pizza de la esquina? 📦",
    "¡Ladrido de alerta! El grupo está más helado que pasillo de yogur... ¿se juega o no? 🐾",
    "Caminé caleta por Nueva Nueva York buscando señal para preguntar: ¿Sale su mambo hoy? 🗽",
    "Si caminan bajo el sol, yo los espero... pero si prenden el PC, puta que me pongo feliz po. 🐕",
    "¿Se juega hoy? Traje una promo de Panucci... bueno, me comí el borde pero queda lo demás. 🍕",
    "¡Guau! ¿Hay alguien vivo o me quedo aquí como estatua esperando a los giles? 🗿",
    "¿Alguien dijo 'Walking on Sunshine'? ¡Esa es la señal pa' que se conecten, cabros! ☀️",
    "Mi olfato no falla: hoy hay puras ganas de quedar ciego frente al monitor. ¿Quién parte? 👃",
    "¿Se juega hoy? Prometo no morder los cables de la fibra... aunque se ven tentadores. ⚡",
    "Ladrido de la suerte pa' los Jenkins. ¡Hoy ganamos sí o sí, de vio! 🍀",
    "He esperado desde el año 1999 por esta partida... ¡no se pongan amarillos ahora! 🗓️",
    "¿Se juega hoy? Estoy listo pa' ser el soporte... aunque sea pa' puro dar ánimo. 🐕‍🦺",
    "¡Guau! El Discord está más solo que el llanero solitario, ¿dónde andan metidos? 🔊",
    "Traje una ración de Dolomita pa' aguantar el lag de hoy. ¿Sale su partida? 💎",
    "¿Se juega? Si no aparecen, voy a buscar al Mordelón pa' que les pegue un mascón en la oreja. 🦖",
    "Ladrido nivel 100. ¡Ya po, repórtense que quiero ver acción! 🎖️",
    "¿Se juega hoy o me pongo a dar vueltas como los tontos persiguiéndome la cola? 🔄",
    "¡Guau! El mejor amigo del hombre también quiere ver cómo manquean un rato. 🐾",
    "¿Hay partida? Si me convidan un poco de completito, les doy el medio buff de suerte. 🌭",
    "¿Se juega hoy? Mi instinto dice que hoy nos paseamos a todos. 🏆",
    "El Fry me enseñó a esperar, pero ustedes me enseñaron a ser gamer. ¿Sale algo o no? 🕹️",
    "¡Alerta de Seymour! Los Jenkins están más lentos que el internet del campo... 🚨",
    "¿Se juega hoy? Mi cola no para de moverse, ¡va a estar weno el mambo! 🐕",
    "¿Hay alguien con vida en este siglo? ¡Ya po, prendan el PC! 🚀",
    "¿Se juega hoy? Mi plato de comida está más vacío que el canal de voz, la dura. 🥣",
    "Último ladrido: ¿Se juega o se les hizo? ¡Los espero en el lobby! 🐶"
]

webhook_url = os.getenv('DISCORD_WEBHOOK_URL')

def enviar_mensaje():
    data = {
        "content": random.choice(frases)
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("Mensaje enviado con éxito")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    enviar_mensaje()
