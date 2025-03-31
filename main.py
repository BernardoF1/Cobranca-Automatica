#BIBLIOTECAS
import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui
from datetime import datetime


#LÓGICA
webbrowser.open('https://web.whatsapp.com/')
sleep(15)

workbook = openpyxl.load_workbook('Clientes.xlsx')
pagina_clientes = workbook['Folha1']

for linha in pagina_clientes.iter_rows(min_row=2):
    nome = linha[0].value
    telefone = linha[1].value
    vencimento = datetime.now()
    mensagem = (f'Olá {nome} sua prestação pode ser pago no {vencimento.strftime('%d/%m/%Y')} \n A chave pix é: ')
    try:
        link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
        webbrowser.open(link_mensagem_whatsapp)
        sleep(10)
        seta = pyautogui.hotkey('enter')
        sleep(5)
        pyautogui.click(seta[0], seta[1])
        sleep(5)
        pyautogui.hotkey('ctrl' and 'w')
        sleep(5)
    except:
        print(f'Não foi possível enviar mensagem para {nome}')
        with open('erro.csv','a',newline='',encoding='utf-8') as arquivo:
            arquivo.write(f'{nome}, {telefone}')



