import streamlit as st
from mistral_api import generate_dream, generate_bedtime_story
import pyttsx3
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Générateur de rêves & histoires", page_icon="🌜")

st.title("🌌 Générateur de rêves et histoires pour s'endormir")

mode = st.radio("Que souhaites-tu générer ?", ["💤 Rêve", "📖 Histoire pour enfant"])

if mode == "💤 Rêve":
    st.subheader("✨ Générer un rêve")
    context = st.text_area("🎭 Contexte du rêve")
    style = st.selectbox("🎨 Style", ["Réaliste", "Onirique", "Cauchemar", "Surréaliste", "Méditatif"])

    dream = None
    if st.button("🪄 Générer le rêve"):
        if not context.strip():
            st.warning("Merci d'ajouter un contexte.")
        else:
            with st.spinner("L'IA imagine un rêve..."):
                dream = generate_dream(context, style)
            st.success("🌙 Voici ton rêve")
            st.write(dream)

    if dream:
        if st.button("🔊 Lire le rêve à voix haute"):
            engine = pyttsx3.init()
            engine.setProperty("rate", 150)
            engine.say(dream)
            engine.runAndWait()

elif mode == "📖 Histoire pour enfant":
    st.subheader("🧸 Générer une histoire pour enfant")
    age = st.slider("👶 Âge de l’enfant", 2, 10, 5)
    theme = st.text_input("🌈 Thème de l’histoire (ex : animaux, forêt magique, nuit, licorne...)")

    story = None
    if st.button("📚 Générer l’histoire"):
        if not theme.strip():
            st.warning("Merci de préciser un thème.")
        else:
            with st.spinner("L'IA écrit une belle histoire..."):
                story = generate_bedtime_story(age, theme)
            st.success("📖 Voici l’histoire")
            st.write(story)

    if story:
        if st.button("🔊 Lire l’histoire à voix haute"):
            engine = pyttsx3.init()
            engine.setProperty("rate", 140)
            engine.say(story)
            engine.runAndWait()
