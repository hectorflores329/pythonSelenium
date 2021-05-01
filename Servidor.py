from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

def getDriver():
    
    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.set_page_load_timeout("60")
    driver.get("http://cognos.deis.cl/ibmcognos/cgi-bin/cognos.cgi?b_action=cognosViewer&ui.action=run&ui.object=/content/folder%5B@name=%27PUB%27%5D/folder%5B@name=%27REPORTES%27%5D/folder%5B@name=%27Atenciones%20de%20Urgencia%27%5D/report%5B@name=%27Atenciones%20Urgencia%20-%20Vista%20por%20semanas%20-%20Servicios%27%5D&ui.name=Atenciones%20Urgencia%20-%20Vista%20por%20semanas%20-%20Servicios&run.outputFormat=&run.prompt=true#")
    return driver

def datos():

    driver = getDriver()
    time.sleep(5)

    title = driver.find_element_by_xpath("/html/body/form[1]/table/tbody/tr[3]/td/div/div[1]/table/tbody/tr/td/div[2]/div/div[1]/span")
    print(title.text)

    driver.close()

if __name__ == '__main__':
    print("Este es un mensaje.")