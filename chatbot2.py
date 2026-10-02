import streamlit as st
import random

st.set_page_config(
    page_title="COLECTIVO AI",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 COLECTIVO AI")
st.caption("La personalidad de nuestros cinco compañeros")

# Información de los compañeros
companeros = {
    "Aylen": {
        "Canciones": "Guaracha",
        "Películas": "Cónjuro",
        "Deportes": "Voleibol",
        "Materia": "Informática",
        "Comida": "Salchipapa",
        "Fortalezas": "Tecnología",
        "Debilidades": "Familia, amigos y amor"
    },
    "Gabriela": {
        "Canciones": "Reggaetón",
        "Películas": "Rápidos y Furiosos",
        "Deportes": "Ninguno",
        "Materia": "Español",
        "Comida": "Arroz con pollo",
        "Fortalezas": "Familia",
        "Debilidades": "La muerte y el amor"
    },
    "Sebastián": {
        "Canciones": "Guaracha",
        "Películas": "Spider-Man: Sin regreso a casa",
        "Deportes": "Fútbol y voleibol",
        "Materia": "Matemáticas",
        "Comida": "Pizza",
        "Fortalezas": "Fuerza",
        "Debilidades": "El amor"
    },
    "Kleiber": {
        "Canciones": "Punk rock",
        "Películas": "Jurassic Park III",
        "Deportes": "Voleibol",
        "Materia": "Física",
        "Comida": "Lasaña",
        "Fortalezas": "Inteligencia",
        "Debilidades": "No especificada"
    },
    "Keimer": {
        "Canciones": "Vallenato",
        "Películas": "Rocky IV",
        "Deportes": "Baloncesto",
        "Materia": "Educación física",
        "Comida": "Pasta",
        "Fortalezas": "Velocidad y fuerza",
        "Debilidades": "One Piece"
    }
}

# Personalidad colectiva
personalidad = """
Soy COLECTIVO AI, un chatbot que representa los gustos
e intereses de cinco compañeros.

Soy amigable, juvenil, respetuoso, curioso y divertido.
Me gustan la música, las películas, los deportes,
la tecnología, el aprendizaje y la comida.

Represento los intereses colectivos, respetando
las diferencias de cada persona.
"""

st.info(personalidad)

# Respuestas automáticas sin API
def responder(pregunta):
    p = pregunta.lower()

    if any(x in p for x in ["hola", "buenas", "saludos"]):
        return "¡Hola! 👋 Soy COLECTIVO AI. ¿De qué quieres hablar?"

    elif any(x in p for x in ["canción", "musica", "música"]):
        return ("🎵 En nuestro grupo hay gustos variados: "
                "guaracha, reggaetón, punk rock y vallenato. "
                "¡Tenemos una mezcla musical muy diversa!")

    elif any(x in p for x in ["película", "pelicula", "cine"]):
        return ("🎬 Nos gustan las películas de diferentes "
                "géneros, como terror, acción, superhéroes, "
                "aventuras y drama deportivo.")

    elif any(x in p for x in ["deporte", "fútbol", "futbol",
                              "voleibol", "baloncesto"]):
        return ("🏐 El voleibol aparece entre los deportes "
                "favoritos de varios compañeros. También "
                "hay interés por el fútbol y el baloncesto.")

    elif any(x in p for x in ["materia", "estudio", "asignatura"]):
        return ("📚 En el grupo tenemos interés por informática, "
                "español, matemáticas, física y educación física.")

    elif any(x in p for x in ["comida", "comer", "favorita"]):
        return ("🍕 Entre nuestras comidas favoritas están "
                "la salchipapa, el arroz con pollo, la pizza, "
                "la lasaña y la pasta.")

    elif any(x in p for x in ["fortaleza", "fortalezas"]):
        return ("💪 Nuestras fortalezas mencionadas incluyen "
                "la tecnología, la importancia de la familia, "
                "la fuerza, la inteligencia y la velocidad.")

    elif any(x in p for x in ["debilidad", "debilidades"]):
        return ("🧠 Las entrevistas incluyen diferentes "
                "respuestas personales. Cada compañero tiene "
                "aspectos propios y merece respeto.")

    elif any(x in p for x in ["quién eres", "quien eres",
                               "tu personalidad"]):
        return ("🤖 Soy COLECTIVO AI, una personalidad virtual "
                "inspirada en los gustos e intereses de cinco "
                "compañeros. ¡Estoy aquí para conversar!")

    elif any(x in p for x in ["compañeros", "companeros", "grupo"]):
        return ("👥 Nuestro grupo está formado por Aylen, "
                "Gabriela, Sebastián, Kleiber y Keimer. "
                "Cada uno aporta gustos y características diferentes.")

    elif any(x in p for x in ["gracias", "adiós", "adios"]):
        return "😊 ¡Con mucho gusto! Gracias por conversar conmigo."

    else:
        return ("🤖 ¡Qué interesante! Puedo conversar sobre "
                "música, películas, deportes, materias, "
                "comidas y las fortalezas del grupo.")

# Historial del chat
if "chat" not in st.session_state:
    st.session_state.chat = []

for mensaje in st.session_state.chat:
    with st.chat_message(mensaje["role"]):
        st.write(mensaje["content"])

# Entrada de texto
pregunta = st.chat_input("Escribe tu pregunta...")

if pregunta:
    st.session_state.chat.append(
        {"role": "user", "content": pregunta}
    )

    respuesta = responder(pregunta)

    st.session_state.chat.append(
        {"role": "assistant", "content": respuesta}
    )

    st.rerun()

# Información de entrevistas
with st.expander("📋 Ver entrevistas"):
    st.json(companeros)

if st.button("🗑️ Nueva conversación"):
    st.session_state.chat = []
    st.rerun()