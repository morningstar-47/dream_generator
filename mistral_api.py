
import os
from mistralai import Mistral
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

def generate_dream(context: str, style: str) -> str:
    prompt = f"""Tu es un générateur de rêves. Crée un rêve {style.lower()} à partir de ce contexte : {context}.
Sois imagé, immersif et symbolique."""

    

    messages = [
    {"role": "system", "content": "Tu es un générateur de rêves oniriques et poétiques."},
    {"role": "user", "content": prompt}
    ]

    try:
        response = client.chat.complete(model=model, messages=messages)
        return response.choices[0].message.content
    except Exception as e:
        return f"Erreur : {str(e)}"



def generate_bedtime_story(age: int, theme: str) -> str:
    prompt = f"""Écris une histoire courte et apaisante pour un enfant de {age} ans, sur le thème suivant : {theme}.
L’histoire doit être simple, bienveillante, sans violence, avec un message rassurant et une fin douce qui donne envie de dormir."""

    messages = [
    {"role": "system", "content": "Tu es un conteur expert d’histoires du soir pour enfants."},
    {"role": "user", "content": prompt}
    ]


    try:
        response = client.chat.complete(model=model, messages=messages)
        return response.choices[0].message.content
    except Exception as e:
        return f"Erreur : {str(e)}"
