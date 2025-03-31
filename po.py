#BIBLIOTECAS
import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui

#LÓGICA
webbrowser.open('https://web.whatsapp.com/')
sleep(30)

workbook = openpyxl.load_workbook('Clientes (2).xlsx')
pagina_clientes = workbook['Folha1']

for linha in pagina_clientes.iter_rows(min_row=2):
    nome = linha[0].value
    telefone = linha[1].value
    vencimento = linha[2].value
    
    mensagem = f'Olá {nome} seu preço da agiotagem pode ser pago no {vencimento.strftime("%d/%m/%Y")}'
    link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
    webbrowser.open(link_mensagem_whatsapp)
