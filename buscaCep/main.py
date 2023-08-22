import requests
import json
from tkinter import *
from tkinter import simpledialog

def buscar_dados():
    cep = simpledialog.askstring("Input", "Digite o CEP")

#   cep  =  input('Digite CEP: ')

    request = requests.get("https://viacep.com.br/ws/"+cep+"/json/")

    print(request.content)
  
   # data = json.loads(request)

  #  print(request["cep"])
    



if __name__ == '__main__':
    buscar_dados()