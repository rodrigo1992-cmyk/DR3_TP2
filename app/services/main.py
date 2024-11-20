import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app.router.routes import *
import requests


# Para executar o uvicorn, usar: python -m uvicorn app.router.routes:router --reload

#--------------------------------RESPOSTA À PARTE 1 QUESTÃO 1--------------------------#
#Arquivo main.py
def P1Q1():
    json1 = {"input": "In the year 1500, the navigator Pedro Alvares Cabral"}

    response = requests.post('http://localhost:8000/autocomplete/', json = json1)
    if response.status_code == 200:
        print(response.json())

#--------------------------------RESPOSTA À PARTE 1 QUESTÃO 2--------------------------#
#Arquivo main.py
def P1Q2():
    #Usei como input o resultado que a questão 1 tinha gerado
    json2 = {"input": "In ther year 1500, the navigator Pedro Alvares Cabral, an American Sailor who was sailing in the Mediterranean at the end of the 17th century and was a founding member of the expedition, had witnessed such a dramatic event."}

    response = requests.post('http://localhost:8000/translate/', json = json2)
    if response.status_code == 200:
        print(response.json())


#--------------------------------RESPOSTA À PARTE 2 QUESTÃO 1--------------------------#
#Arquivo main.py
def P2Q1():
    json3 = {"input": "Hello Fake LLM!"}

    response = requests.post('http://localhost:8000/fakellm/', json = json3)
    if response.status_code == 200:
        print(response.json())

#--------------------------------RESPOSTA À PARTE 2 QUESTÃO 2--------------------------#
#Arquivo main.py
def P2Q2():
    json4 = {"input": "Why Oil Companies Are Walking Back From Green Energy. Investors have rewarded oil giants like Exxon Mobil that did not embrace wind and solar, which have been less profitable in recent years than oil and gas."}

    response = requests.post('http://localhost:8000/traduzir-en-fr/', json = json4)
    if response.status_code == 200:
        print(response.json())


#--------------------------------RESPOSTA À PARTE 2 QUESTÃO 3--------------------------#
#Arquivo main.py
def P2Q3():
    json5 = {"input": "Why Oil Companies Are Walking Back From Green Energy. Investors have rewarded oil giants like Exxon Mobil that did not embrace wind and solar, which have been less profitable in recent years than oil and gas."}

    response = requests.post('http://localhost:8000/traduzir-en-de/', json = json5)
    if response.status_code == 200:
        print(response.json())



if __name__ == "__main__":
    #P1Q1()
    #P1Q2()
    #P2Q1()
    #P2Q2()
    #P2Q3()




    