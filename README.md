# Cobrança Automatica

Como o próprio nome já diz, este programa foi feito para otimizar o tempo daqueles que fornecem algum tipo de serviço, e precisam ficar cobrando mensalmente ou semanalmente.

## Instalação

Para instalar o projeto, você precisa de pelo menos do [Python 3.13](https://www.python.org/downloads/) instalado na sua máquina.(caso não tenha instalado só clicar aonde está escrito Python)

Agora no terminal:
``` bash
# Clone o repositorio
git clone https://github.com/BernardoF1/Cobranca-Automatica.git

# Após isso entre na pasta
cd Cobranca-automatica

# Instale as bibliotecas necessarias
pip install requirements.txt
```
## Como funciona

O script funciona da seguinte forma:

1. No Arquivo Clientes.xlsx você vai colocar o nome da pessoa, o telefone dela e a data que ela tem que pagar.
2. Em main.py na váriavél mensagem, você pode modificar a mensagem ao seu gosto.
     1. "A mensagem padrão é: (Olá {nome_da_pessoa} sua prestação pode ser pago no {dia_do_vencimento} \n A chave pix é: {seu_pix})"

## Para iniciar

Os seguintes comandos são necessários no terminal:
``` bash
# Entrar na pasta

cd Cobranca-automatica

# Rodar o script

python main.py

```

O ideal após iniciar o script, é deixar ele funcionando até rodar todos os contatos então neste tempo não mexa no computador para evitar bugar o script.

## 

Caso ele não consiga mandar a mensagem por algum motivo, ele escreve em um arquivo csv com o nome do contato que ele não conseguiu além do número de telefone.
