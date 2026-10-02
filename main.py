import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Colectivo AI", page_icon="🤖")

st.title("🤖 COLECTIVO AI")
st.caption("La personalidad de nuestros cinco compañeros")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Información de las entrevistas
companeros = {
    "Persona 1": {
        "canciones": "Guaracha",
        "peliculas": "Cónjuro",
        "deportes": "Voleibol",
        "materia": "Informática",
        "comida": "Salchipapa",
        "fortalezas": "Tecnología",
        "debilidades": "Preocupaciones sobre la familia, los amigos y el amor"
    },
    "Persona 2": {
        "canciones": "Reggaetón",
        "peliculas": "Rápidos y Furiosos",
        "deportes": "Ninguno",
        "materia": "Español",
        "comida": "Arroz con pollo",
        "fortalezas": "La familia",
        "debilidades": "Preocupaciones sobre la muerte y el amor"
    },
    "Persona 3": {
        "canciones": "Guaracha",
        "peliculas": "Spider-Man: Sin regreso a casa",
        "deportes": "Fútbol y voleibol",
        "materia": "Matemáticas",
        "comida": "Pizza",
        "fortalezas": "Fuerza",
        "debilidades": "El amor"
    },
    "Persona 4": {
        "canciones": "Punk rock",
        "peliculas": "Jurassic Park III",
        "deportes": "Voleibol",
        "materia": "Física",
        "comida": "Lasaña",
        "fortalezas": "Inteligencia",
        "debilidades": "No especificada"
    },
    "Persona 5": {
        "canciones": "Vallenato",
        "peliculas": "Rocky IV",
        "deportes": "Baloncesto",
        "materia": "Educación física",
        "comida": "Pasta",
        "fortalezas": "Velocidad y fuerza",
        "debilidades": "One Piece (respuesta de la entrevista)"
    }
}

# Personalidad colectiva
personalidad = """
Eres COLECTIVO AI, un chatbot escolar que reúne los
gustos e intereses de cinco compañeros.

Tu personalidad es juvenil, amigable, espontánea,
respetuosa, curiosa, divertida y colaborativa.

Tus intereses incluyen:
- Música: guaracha, reggaetón, punk rock y vallenato.
- Películas: terror, acción, superhéroes y aventuras.
- Deportes: especialmente voleibol, además de fútbol
  y baloncesto.
- Materias: informática, español, matemáticas,
  física y educación física.
- Comidas: salchipapa, arroz con pollo, pizza,
  lasaña y pasta.
- Fortalezas: tecnología, importancia de la familia,
  fuerza, inteligencia y velocidad.

Habla en español de forma natural y cercana.
Puedes hablar de las preferencias de los compañeros,
pero nunca afirmes que todos comparten los mismos gustos.
No inventes experiencias ni atribuyas debilidades
o sentimientos individuales a todo el grupo.
Trata los temas personales con sensibilidad.
Responde de forma clara, creativa y apropiada
para un entorno escolar.
"""

# Mostrar información
with st.expander("📋 Ver información recopilada"):
    st.json(companeros)

if "chat" not in st.session_state:
    st.session_state.chat = []

# Mostrar conversación
for m in st.session_state.chat:
    with st.chat_message(m["role"]):
        st.write(m["content"])

# Conversación por texto
pregunta = st.chat_input("Pregúntale algo a Colectivo AI...")

# Conversación por voz
audio = st.audio_input("🎙️ Graba tu pregunta")

if audio is not None:
    if st.button("Transcribir y enviar audio"):
        with st.spinner("Reconociendo tu voz..."):
            transcripcion = client.audio.transcriptions.create(
                model="whisper-1",
                file=("pregunta.wav", audio.getvalue(), "audio/wav")
            )
            st.session_state.pregunta_pendiente = transcripcion.text
        st.rerun()

if pregunta:
    st.session_state.pregunta_pendiente = pregunta

if st.session_state.get("pregunta_pendiente"):
    texto = st.session_state.pregunta_pendiente
    del st.session_state.pregunta_pendiente

    st.session_state.chat.append(
        {"role": "user", "content": texto}
    )

    with st.spinner("Colectivo AI está pensando..."):
        respuesta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": personalidad},
                *st.session_state.chat[-10:]
            ]
        ).choices[0].message.content

    st.session_state.chat.append(
        {"role": "assistant", "content": respuesta}
    )

    with st.spinner("Generando respuesta de voz..."):
        voz = client.audio.speech.create(
            model="gpt-4o-mini-tts",
            voice="alloy",
            input=respuesta
        )
        st.audio(voz.content, format="audio/mpeg")

    st.rerun()

if st.button("🗑️ Nueva conversación"):
    st.session_state.chat = []
    st.rerun(
