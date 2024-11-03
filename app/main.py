import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from router.routes import *
from services.base import *
import requests


# Para executar o uvicorn, usar: python -m uvicorn app.router.routes:router --reload

#--------------------------------RESPOSTA À QUESTÃO 1--------------------------#
#Arquivo main.py
def QUEST1():
    json1 = {"input": "In the year 1500, the navigator Pedro Alvares Cabral"}

    response = requests.post('http://localhost:8000/autocomplete/', json = json1)
    if response.status_code == 200:
        print(response.json())

#--------------------------------RESPOSTA À QUESTÃO 2--------------------------#
#Arquivo main.py
def QUEST2():
    #Usei como input o resultado que a questão 1 tinha gerado
    json2 = {"input": "In ther year 1500, the navigator Pedro Alvares Cabral, an American Sailor who was sailing in the Mediterranean at the end of the 17th century and was a founding member of the expedition, had witnessed such a dramatic event."}

    response = requests.post('http://localhost:8000/translate/', json = json2)
    if response.status_code == 200:
        print(response.json())


if __name__ == "__main__":
    #QUEST1()
    QUEST2()


    