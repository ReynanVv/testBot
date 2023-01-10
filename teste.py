from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import requests

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

# tempo para escanear o QRcode
time.sleep(30)


def Notificacao():
    bolinha = driver.find_element_by_class_name('_1pJ9J')
    bolinha = driver.find_elements_by_class_name('_1pJ9J')
    clica_bolinha = bolinha[-1]
    acao_bolinha = webdriver.common.action_chains.ActionChains(driver)
    acao_bolinha.move_to_element_with_offset(clica_bolinha, 0, -20)
    acao_bolinha.click()
    acao_bolinha.perform()
    time.sleep(6)


def Numero():
    telefone_cliente = driver.find_element_by_xpath(
        '//*[@id="main"]/header/div[2]/div[1]/div/span')
    telefone = telefone_cliente.text
    print(telefone)


telefone_cliente = driver.find_element_by_xpath(
    '//*[@id="main"]/header/div[2]/div[1]/div/span')
telefone = telefone_cliente.text

def UltimaMensagem():
    todas_as_msgs = driver.find_elements_by_class_name('_1Gy50')
    todas_as_msgs_texto = [e.text for e in todas_as_msgs]
    msg = todas_as_msgs_texto[-1]
    
    if msg == 'mensagem do bot':  # o perfil fixado precisa ter uma mensagem padrão que seja igual o valor da variável
        Voltar()
    else:
        ResponderMensagem()

todas_as_msgs = driver.find_elements_by_class_name('_1Gy50')
todas_as_msgs_texto = [e.text for e in todas_as_msgs]
msg = todas_as_msgs_texto[-1]



def ResponderMensagem():
    campo_de_texto = driver.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    campo_de_texto.click()
    resposta = requests.get("http://localhost/bot/index.php", params={'msg': {msg},'telefone':{telefone}})
    aux = resposta.text
    campo_de_texto.send_keys(aux, Keys.ENTER)


def Voltar():
    contato_padrao = driver.find_element_by_class_name('_1pJ9J _2XH9R')
    acao_contato = webdriver.common.action_chains.ActionChains(driver)
    acao_contato.move_to_element_with_offset(contato_padrao, 0, -20)
    acao_contato.click()
    acao_contato.perform()


def Bot():
    try:
        # Pega o valor da notificação e clica em quem enviou
        Notificacao()

        # Pega o número ou nome do contato salvo
        Numero()

        # Pega a última mensagem enviada
        UltimaMensagem()

    except:
        print('buscando')
        time.sleep(3)



while True:
    Bot()

# TENTATIVA DE RESOLVER O bug! FALHA
# As classes usadas nos elementos de notificação e de fixação de contato tem o mesmo valor o programa
# confunde os dois. _1pJ9J._2XH9R esse valor é interpretado como _1pJ9J gerando o bug
# Usando recursão fiz uma condicional pra não ficar mandando mensagem no perfil fixado infinitamente
# Bug resolvido!
