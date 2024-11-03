import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


from app.model.models import *
from fastapi import APIRouter
from transformers import pipeline

#--------------------------------RESPOSTA À QUESTÃO 1--------------------------#
#Arquivo routes.py
router = APIRouter()

def gerar_resposta(input: str) -> dict:
    pipe = pipeline('text-generation', model='gpt2')
    return pipe(input)


@router.post("/autocomplete/")
async def autocomplete(body: InputExerc1) -> OutputExerc1:
    resposta = gerar_resposta(body.input)
    return OutputExerc1(output=resposta[0]['generated_text'])


#--------------------------------RESPOSTA À QUESTÃO 2--------------------------#
#Arquivo routes.py
def gerar_traducao(input: str) -> dict:
    pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")
    return pipe(input)

@router.post("/translate/")
async def translate(body: InputExerc2) -> OutputExerc2:
    resposta = gerar_traducao(body.input)
    #return{'Resposta':resposta}
    return OutputExerc2(output=resposta[0]['translation_text'])

