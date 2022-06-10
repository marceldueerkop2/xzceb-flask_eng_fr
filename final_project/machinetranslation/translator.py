"""This is a translator"""
import os
import json
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(english_text):
    """Translates English txt to French using IBM Watson API"""
    translation_result = language_translator.translate(english_text, model_id='en-fr').get_result()
    french_text = translation_result['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    """Translates French txt to English using IBM Watson API"""
    translation_result = language_translator.translate(french_text, model_id='fr-en').get_result()
    english_text = translation_result['translations'][0]['translation']
    return english_text
