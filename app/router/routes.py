import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


from app.model.models import *
from fastapi import APIRouter
from dotenv import load_dotenv
from transformers import pipeline
from langchain_community.llms import FakeListLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai.chat_models import ChatOpenAI


#--------------------------------RESPOSTA À PARTE 1 QUESTÃO 1--------------------------#
#Arquivo routes.py
router = APIRouter()

def gerar_resposta(input: str) -> dict:
    pipe = pipeline('text-generation', model='gpt2')
    return pipe(input)


@router.post("/autocomplete/")
async def autocomplete(body: InputExercP1Q1) -> OutputExercP1Q1:
    resposta = gerar_resposta(body.input)
    return OutputExercP1Q1(output=resposta[0]['generated_text'])


#--------------------------------RESPOSTA À PARTE 1 QUESTÃO 2--------------------------#
#Arquivo routes.py
def gerar_traducao(input: str) -> dict:
    pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")
    return pipe(input)

@router.post("/translate/")
async def translate(body: InputExercP1Q2) -> OutputExercP1Q2:
    resposta = gerar_traducao(body.input)
    return OutputExercP1Q2(output=resposta[0]['translation_text'])

#--------------------------------RESPOSTA À PARTE 2 QUESTÃO 1--------------------------#
#Arquivo routes.py
def gerar_resposta_fake(input: str) -> dict:
    fake_llm = FakeListLLM(responses=["Fake is your mother"])
    return fake_llm.invoke(input)

@router.post("/fakellm/")
async def fakellm(body: InputExercP2Q1) -> OutputExercP2Q1:
    resposta = gerar_resposta_fake(body.input)
    return OutputExercP2Q1(output=resposta)



#--------------------------------RESPOSTA À PARTE 2 QUESTÃO 2--------------------------#
#Arquivo routes.py
def mod_traduzir_en_fr(input: str) -> dict:

    template = ChatPromptTemplate([
        ("system", "You are an English to French translator. Reject any other language."),
        ("user", "Translate this: {input}")
    ])
    llm = ChatOpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))
    response = llm.invoke(template.format_messages(input=input))
    return response.content

@router.post("/traduzir-en-fr/")
async def traduzir_en_fr(body: InputExercP2Q2) -> OutputExercP2Q2:
    resposta = mod_traduzir_en_fr(body.input)
    return OutputExercP2Q2(output=resposta)

