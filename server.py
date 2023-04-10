from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    #translationengfr = language_translator.translate(text="Hello", model_id="en-fr").get_result()
    # Write your code here
     
def englishtofrench(word):
    """This class does english to french translation"""

    url_lt='https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/c1377980-0456-4f5b-8fc3-de3692d65df2'
    apikey_lt='0O-8rrFSWtd6xEzrSBmWPYyuO3W48imBYsHDYXoKyEYi'
    version_lt='2018-05-01'
    authenticator = IAMAuthenticator(apikey_lt)
    language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
    language_translator.set_service_url(url_lt)
    lt = language_translator
    translation = lt.translate(text=word, model_id="en-fr").get_result()
    
    if word == " ":
        print("Please enter a word")
    else:
        pass

    return translation['translations'][0]['translation']
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here

def frenchtoenglish(word):
    """This class does french to english  translation"""

    url_lt='https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/c1377980-0456-4f5b-8fc3-de3692d65df2'
    apikey_lt='0O-8rrFSWtd6xEzrSBmWPYyuO3W48imBYsHDYXoKyEYi'
    version_lt='2018-05-01'
    authenticator = IAMAuthenticator(apikey_lt)
    language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
    language_translator.set_service_url(url_lt)
    lt = language_translator
    translation = lt.translate(text=word, model_id="fr-en").get_result()
    return translation['translations'][0]['translation']
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template

#i#f __name__ == "__main__":
  #  app.run(host="0.0.0.0", port=8080)
