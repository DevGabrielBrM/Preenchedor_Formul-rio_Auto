# Passo 1 - Entrar no sistema da Empresa
#     link - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2 - Fazer Login
# Passo 3 - Pegar/importar a base de dados
# Passo 4 - Cadastrar um produto
# Passo 5 - Repetir o passo 4 até cadastrar todos os produtos

import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
# pyautogui.scroll -> rolar a tela para cima ou para baixo

pyautogui.PAUSE = 0.5

# Passo 1 - entrar no sistema
# abrir o navegador
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# entrar no link
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(3)

# Passo 2 - Fazer o login
pyautogui.click(x=835, y=615)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write('devsenior@apple.com')

# passar par ao campo de senha

pyautogui.press('tab')
pyautogui.write('soudevsenior')

pyautogui.click(x=916, y=846)

time.sleep(3)

# Passo 3 - Importar a base de dados

import pandas as pd

dados = pd.read_csv('produtos.csv')

# Passo 4 - Cadastrar o produto
# para cada linha da tabela:
for linha in dados.index:   
    
    # codigo
    pyautogui.click(x=773, y=433)
    codigo = str(dados.loc[linha,'codigo'])
    pyautogui.write(codigo)

    # marca
    pyautogui.press('tab')
    marca = codigo = str(dados.loc[linha,'marca'])
    pyautogui.write(marca)

    # tipo
    pyautogui.press('tab')
    tipo = str(dados.loc[linha,'tipo'])
    pyautogui.write('tipo')

    # categoria
    pyautogui.press('tab')
    categoria = str(dados.loc[linha,'categoria'])
    pyautogui.write(categoria)

    # preço
    pyautogui.press('tab')
    preco = str(dados.loc[linha,'preco_unitario'])
    pyautogui.write(preco)

    # custo
    pyautogui.press('tab')
    custo = str(dados.loc[linha,'custo'])
    pyautogui.write(custo)

    # obs
    pyautogui.press('tab')
    obs = str(dados.loc[linha,'obs'])
    if obs != 'nan' :
        pyautogui.write(obs)

    #clicar no botão de enviar
    pyautogui.press('tab')
    pyautogui.press('enter')

    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)

