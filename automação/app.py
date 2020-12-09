#abrindo navegador
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from time import sleep

driver = webdriver.Chrome(
    executable_path=os.getcwd() + os.sep + 'chromedriver.exe')
#navegar ate o site
driver.get('https://www.mercadolivre.com.br')
# se livrando dos cookies
cokies = driver.find_element_by_xpath("//button[@class='nav-cookie-disclaimer__button']")
cokies.click()
#pesquisando item
campo_pesquisa = driver.find_element_by_xpath("//input[@class='nav-search-input']")
campo_pesquisa.click()
#inserindo pesquisa!
sleep (int(5))
iten = input('O que você esta procurando? ')
campo_pesquisa.send_keys( iten )
campo_pesquisa.send_keys(Keys.ENTER)

#Titulos
while True:
    try:
        textos = driver.find_elements_by_xpath("//h2[@class='ui-search-item__title']")
    except:
        print(' Não estamos no lista')
    try:
        textos = driver.find_elements_by_xpath("//h2[@class='ui-search-item__title ui-search-item__group__element']")
    except:
        print('isso não é uma tumbnail')

    precos = driver.find_elements_by_xpath(
    "//div[@class='ui-search-price ui-search-price--size-medium ui-search-item__group__element']//div[@class= 'ui-search-price__second-line'] //span[@class= 'price-tag ui-search-price__part']//span[@class= 'price-tag-fraction']")
    
    for texto, preco in zip(textos, precos):
        with open ('obejtos.txt' , 'a', newline='', encoding='utf-8') as arquivo:
            arquivo.write(texto.text + ', ' + 'valor do produto: ' + preco.text + ' R$' + os.linesep)

#navegar
    try:
        driver.execute_script('window.scrollTo(0,document.body.scrollheight);')
        botton_next = driver.find_element_by_xpath(
            "//li[@class='andes-pagination__button andes-pagination__button--next']")
        botton_next.click()
    except:
        pass
#titulo em lista class="ui-search-item__title"
#titulo em tubneil //h2[@class='ui-search-item__title ui-search-item__group__element']
#botão next //li[@class='andes-pagination__button andes-pagination__button--next']