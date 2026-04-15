import requests
import os
import random

# Seymour Diera - Versión Definitiva 2026 (Los Jenkins de Andacollo)
frases = [
    # --- CLAN 1: ANDACOLLO & EL INTERNET MUNDO ---
    "¿Se juega hoy? ¿O se cayó el Mundo de nuevo y están todos mirando el techo en Andacollo? 🌐",
    "¡Guau! El internet Mundo está más lento que subida a la Virgen en procesión... ¿Sale algo? ⛪",
    "¿Hay mambo? Si no juegan, voy a pensar que se cortó la fibra en la entrada del pueblo otra vez. ✂️",
    "¡Ladrido de alerta! Bajen de la nube, cabros, que en Andacollo ya hace frío y el PC es la mejor estufa. ❄️",
    "¿Se juega hoy? Ojalá que el ping de Mundo nos deje jugar aunque sea una partida sin lag. 🐌",
    "¡Guau! Los Jenkins de Andacollo están más apagados que el pueblo un lunes en la noche. 💤",
    "¿Hay partida? Aprovechen que el internet de Mundo anda 'estable' (por ahora)... ¡Pura fe! 🙏",
    "¿Se juega hoy o andan todos sin señal? Mundo Pacífico nos tiene a puros ladridos. 🐕",
    "Siento olor a azufre... ¿es la mina o se quemó el router de Mundo otra vez? 💨",
    "¡Guau! Si el internet de Andacollo fuera como mi lealtad, estaríamos jugando a 1ms. 🦴",
    "¿Sale partida? Miren que el viento de los cerros me va a botar la señal si no se apuran. 🌬️",

    # --- CLAN 2: NOSTALGIA L4D (RECUERDOS DEL SHREK) ---
    "¿Se acuerdan cuando el Shrek nos dejaba agonizando en el L4D? Menos mal ya terminamos esa custión. 👹",
    "¡Guau! Todavía escucho los gritos de cuando nos pillaba el Tank... qué tiempos más terribles, de vio. 🧟",
    "A veces extraño el L4D, pero después me acuerdo de cómo morían como pollos y se me pasa. 🍗",
    "¿Se juega hoy? Ojalá sea algo más tranqui que el L4D, sus corazones ya no aguantan un Shrek. 👴",
    "¡Guau! Menos mal que el Shrek no tiene fibra Mundo, si no, no nos arrancamos nunca. 🐢",
    "A veces sueño que el Tank me persigue por la calle Urmeneta... culpo al L4D. ⛪",

    # --- CLAN 3: GTA ONLINE (EL JEFE Y EL CASINO) ---
    "¡Guau! El Jefe de la sesión se está haciendo millonario mientras ustedes andan a pata. ¡Pague las misiones po! 💼",
    "¿Pasaron por el Casino ya? Seguro la ruleta les tiró un polerón ordinario en vez del auto. 🎡",
    "Siento olor a negocios del GTA... el Jefe debe estar frotándose las manos con el trabajo ajeno. 💸",
    "¡Ladrido de alerta! Vayan a ver la ruleta del Casino, a ver si hoy la suerte no les es tan esquiva. 🎰",
    "¿Se juega GTA hoy? Dice el Jefe que si no llegan, les descuenta el bono de colación. 🌭",
    "¡Guau! El Jefe manda más que el alcalde de Andacollo. ¡Ya po, muevan la merca! 🚚",

    # --- CLAN 4: EL MURO DE LA VERGÜENZA (RAFT & VALHEIM) ---
    "¿El Raft? Bien, gracias. El tiburón ya se armó un castillo con la madera que dejaron tirada. 🦈",
    "¡Guau! Dicen que si entras al Valheim hoy, los vikingos te cobran pensión alimenticia por abandono. 🕸️",
    "Me pregunto si algún día terminarán el Raft... o si va a ser otra reliquia como el Valheim. 🛶",
    "Odin me mandó un WhatsApp preguntando por qué dejaron el Valheim botado. Me dio vergüenza ajena. ⚔️",
    "La balsa del Raft ya debe estar en la Antártica de tanto que la dejaron a la deriva, giles. 🌊",
    "¡Guau! El tiburón del Raft tiene más horas de juego que ustedes este mes. 🪵",
    "¿Se juega algo? Miren que si no, me voy a buscar la balsa yo solo. 🐾",

    # --- CLAN 5: CHILENISMOS Y TONO SEYMOUR (RANDOM) ---
    "¿Se juega hoy? Sigo esperando aquí afuera... ¿O ya se fueron a acostar, giles? 🐶",
    "¡Guau! Siento olor a vicio... ¿Alguien va a prender el server hoy o andan puro dando jugo? 🎮",
    "El Fry no está, pero ustedes sí po. ¿Sale su partida o les da amansadora? 🍕",
    "Esperaría mil años si fuera necesario, pero puta que sería bacán que jugáramos ahora. 🦴",
    "¿Se juega hoy o me quedo haciendo tuto en mi caja de pizza de la esquina? 📦",
    "¡Ladrido de alerta! El grupo está más helado que pasillo de yogur... ¿se juega o no? 🐾",
    "Caminé caleta por Nueva Nueva York buscando señal para preguntar: ¿Sale su mambo hoy? 🗽",
    "Si caminan bajo el sol, yo los espero... pero si prenden el PC, puta que me pongo feliz po. 🐕",
    "¿Se juega hoy? Traje una promo de Panucci... me comí el borde pero queda lo demás. 🍕",
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
    "Último ladrido: ¿Se juega o se les hizo? ¡Los espero en el lobby! 🐶",
    "¿Se juega hoy? O andan puro vendiendo humo como el profesor Farnsworth... 💨",
    "¡Guau! Menos mal que despertaron, pensé que estaban congelados como el Fry. ¿Sale algo? ❄️",
    "¿Hay mambo hoy? No me dejen esperando como estatua po, miren que no soy de piedra. 🗿",
    "¡Ladrido de alerta! Siento olor a que hoy nos carrean. ¿Quién apaña? 🎒",
    "¿Se juega hoy o se les arrancó el chancho? Los espero en el lobby, giles. 🐷",
    "¡Guau! El server está más botado que el Bender cuando se queda sin alcohol. 🤖",
    "¿Se juega algo o están viendo las noticias como los tatas? Ya po, muevan las nalgas. 📺",
    "Puta que hace frío... ¿sale su partida pa' calentar las manos o qué? 🔥",
    "¿Hay alguien? No me hagan el vacío, miren que ya me dio la depre. 😢",
    "¡Guau! Traje una pizza de Panucci, pero me la quitaron en la aduana por ser del siglo XX. 🍕",
    "¿Se juega hoy? Mi instinto dice que hoy sacamos la del honor. 🎖️",
    "¡Alerta! Los Jenkins están más desaparecidos que el sueldo a fin de mes. ¿Sale partida? 💸",
    "¿Se juega hoy? Si no se conectan, les mando un virus del Dr. Zoidberg. 🦀",
    "¡Guau! Puta que son fomes, ¿van a jugar o no? Me tienen chato esperando. 🙄",
    "¿Se juega hoy? Mi colita dice que hoy hay puro 'GG easy'. 🐕",
    "¡Ladrido de la suerte! Hoy el lag no nos gana, ¡vamos que se puede! ⚡",
    "¿Se juega hoy? Ojalá no manqueen tanto como ayer po, cabros. 🎮",
    "¡Guau! El Fry me dijo que eran secos, no me dejen de mentiroso. 🤥",
    "¿Hay partida? Miren que mi caja de pizza no es tan cómoda como el sillón gamer. 📦",
    "¿Se juega hoy? Si no aparecen, voy a ir a mearles el router. 💦",
    "¡Alerta de vicio! Siento que hoy sale su triunfo épico. ¿Quién invita? 🏆",
    "¿Se juega hoy? No sean amarillos, miren que el Seymour no perdona. 🧀",
    "¡Guau! Estaba soñando con ovejas eléctricas, pero prefiero verlos jugar. 🐑",
    "¿Hay mambo? Si no juegan, me voy con la tía del furgón. 🚌",
    "¿Se juega hoy? Traje el medio buff pa' que no mueran al primer minuto. 🧪",
    "¡Ladrido de guerra! Vamos a romperla hoy día, de vio. ⚔️",
    "¿Se juega algo? Miren que el tiempo vuela y yo no soy eterno po. ⏳",
    "¡Guau! ¿Están ahí o se los tragó la tierra como a la Nueva York antigua? 🌍",
    "¿Se juega hoy? Avisen con tiempo po, miren que tengo que pasear... ah verdad que no. 🐾",
    "¡Alerta! El grupo está más lento que el internet del VTR (o Mundo Pacífico). 🐌",
    "¿Se juega hoy? Si ganamos, invito las galletas de perro (mentira, me las como yo). 🍪",
    "¡Guau! ¿Quién se raja con el server hoy? No sean manos de guagua. 👶",
    "¿Hay partida? Puta que me gusta ver cuando se pican porque pierden. 😂",
    "¿Se juega hoy? Traje una ración de Dolomita pa' que aguanten los balazos. 💎",
    "¡Ladrido de ánimo! Vamos Jenkins, que hoy nos paseamos a todos. 🥇",
    "¿Se juega hoy? Ojalá que el ping esté bajo, no como mi ánimo cuando no juegan. 📉",
    "¡Guau! ¿Hay alguien? Me siento más solo que el Bender en una iglesia. ⛪",
    "¿Se juega algo? Ya po, que me aburro más que viendo crecer el pasto. 🌱",
    "Último aviso: ¿Se juega hoy o les mando al Mordelón a que les coma las tareas? 🦖"
]

webhook_url = os.getenv('DISCORD_WEBHOOK_URL')

def enviar_mensaje():
    if not webhook_url:
        print("Error: No se encontró la URL del Webhook")
        return
    
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
