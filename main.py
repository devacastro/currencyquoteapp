#(toda a lógica de programacao estará aqui)
#como padrao de inicialização do kivy, começar na seguinte ordem
#1 importar o App, Builder (GUI)
#2 criar o nosso aplicativo
#3 criar a função build

#1 Importar o App, Builder (GUI)

from webbrowser import get
from kivy.app import App
import requests
import os

#2 Criar o nosso aplicativo

from kivy.lang import Builder

#3 Criar a funcao build

GUI = Builder.load_file("tela.kv") #importa a tela

#Criando aplicativo com a funcao build, todo aplicativo kivy e criado dentro de uma classe.

class  MeuAplicativo(App):
    def build(self):
        return GUI
    
    #sempre atualiza meu aplicativo com dados do dia.
    def on_start(self):
        #cotacao_dolar = self.pegar_cotacao("USD")
        self.root.ids["moeda1"].text = f"USD {os.linesep}{self.pegar_cotacao('USD')}"
        self.root.ids["moeda2"].text = f"EUR {os.linesep}{self.pegar_cotacao('EUR')}"
        self.root.ids["moeda3"].text = f"BTC {os.linesep}{self.pegar_cotacao('BTC')}"
        self.root.ids["moeda4"].text = f"ETH {os.linesep}{self.pegar_cotacao('ETH')}"

    #vai receber o codigo da moeda como refe buscar na internet.
    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        
        #biblioteca que permite realizar requisicao a API
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao

    #roda o aplicativo em looping infinito, para ficar sempre aberto
    
MeuAplicativo().run()

