import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select


def getDriver():
    
    options = Options()
    options.log.level = "trace"
    options.add_argument("--headless")
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")
    driver = webdriver.Firefox(options=options)
    driver.set_page_load_timeout("60")
    driver.get("http://cognos.deis.cl/ibmcognos/cgi-bin/cognos.cgi?b_action=cognosViewer&ui.action=run&ui.object=/content/folder%5B@name=%27PUB%27%5D/folder%5B@name=%27REPORTES%27%5D/folder%5B@name=%27Atenciones%20de%20Urgencia%27%5D/report%5B@name=%27Atenciones%20Urgencia%20-%20Vista%20por%20semanas%20-%20Servicios%27%5D&ui.name=Atenciones%20Urgencia%20-%20Vista%20por%20semanas%20-%20Servicios&run.outputFormat=&run.prompt=true#")
    return driver

def descargarTablas():
    driver = getDriver()
    time.sleep(5)

    # Seleccionado años
    yers = driver.find_element_by_xpath("/html/body/form[1]/table/tbody/tr[3]/td/div/div[1]/table/tbody/tr/td/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/div/table/tbody/tr/td/div[1]/select")
    yearsValues = yers.find_elements_by_tag_name("option")

    # for i in range(len(yearsValues)):
    for i in range(1):
        yers = driver.find_element_by_xpath("/html/body/form[1]/table/tbody/tr[3]/td/div/div[1]/table/tbody/tr/td/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/div/table/tbody/tr/td/div[1]/select")
        yearsValues = yers.find_elements_by_tag_name("option")

        selectYears = Select(yers)
        selectYears.deselect_all()

        yearsValues[i].click()
        time.sleep(1)

        # Seleccionado regiones
        region = driver.find_element_by_xpath("/html/body/form[1]/table/tbody/tr[3]/td/div/div[1]/table/tbody/tr/td/div[2]/div/div[2]/table/tbody/tr[2]/td[1]/div/table/tbody/tr[2]/td[1]/div/table/tbody/tr/td/div[1]/select")
        yearsRegion = region.find_elements_by_tag_name("option")

        # for j in range(len(yearsRegion)):
        for j in range(1):
            region = driver.find_element_by_xpath("/html/body/form[1]/table/tbody/tr[3]/td/div/div[1]/table/tbody/tr/td/div[2]/div/div[2]/table/tbody/tr[2]/td[1]/div/table/tbody/tr[2]/td[1]/div/table/tbody/tr/td/div[1]/select")
            yearsRegion = region.find_elements_by_tag_name("option")

            selectRegion = Select(region)
            selectRegion.deselect_all()

            yearsRegion[j].click()
            time.sleep(1)

            # Seleccionado tipo de establecimiento
            stableType = driver.find_element_by_xpath("/html/body/form[1]/table/tbody/tr[3]/td/div/div[1]/table/tbody/tr/td/div[2]/div/div[2]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[1]/div/table/tbody/tr/td/div[1]/select")
            yearsStableType = stableType.find_elements_by_tag_name("option")
            
            # for k in range(len(yearsStableType)):
            for k in range(1):
                stableType = driver.find_element_by_xpath("/html/body/form[1]/table/tbody/tr[3]/td/div/div[1]/table/tbody/tr/td/div[2]/div/div[2]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[1]/div/table/tbody/tr/td/div[1]/select")
                yearsStableType = stableType.find_elements_by_tag_name("option")

                selectStableType = Select(stableType)
                selectStableType.deselect_all()

                yearsStableType[k].click()
                time.sleep(1)

                # Seleccionado establecimiento
                stable = stableType = driver.find_element_by_xpath("/html/body/form[1]/table/tbody/tr[3]/td/div/div[1]/table/tbody/tr/td/div[2]/div/div[2]/table/tbody/tr[2]/td[3]/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div[1]/select")
                yearsStable = stable.find_elements_by_tag_name("option")

                # for l in range(len(yearsStable)):
                for l in range(1):
                    stable = stableType = driver.find_element_by_xpath("/html/body/form[1]/table/tbody/tr[3]/td/div/div[1]/table/tbody/tr/td/div[2]/div/div[2]/table/tbody/tr[2]/td[3]/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div[1]/select")
                    yearsStable = stable.find_elements_by_tag_name("option")

                    selectStable = Select(stable)
                    selectStable.deselect_all()

                    yearsStable[l].click()
                    time.sleep(1)

                    boton = driver.find_elements_by_tag_name("button")
                    boton[0].click()

                    time.sleep(20)

                    # Descargando tablas
                    yers = driver.find_element_by_xpath("/html/body/form[1]/table/tbody/tr[3]/td/div/div[1]/table/tbody/tr/td/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/div/table/tbody/tr/td/div[1]/select")
                    yearsValues = yers.find_elements_by_tag_name("option")

                    region = driver.find_element_by_xpath("/html/body/form[1]/table/tbody/tr[3]/td/div/div[1]/table/tbody/tr/td/div[2]/div/div[2]/table/tbody/tr[2]/td[1]/div/table/tbody/tr[2]/td[1]/div/table/tbody/tr/td/div[1]/select")
                    yearsRegion = region.find_elements_by_tag_name("option")

                    stableType = driver.find_element_by_xpath("/html/body/form[1]/table/tbody/tr[3]/td/div/div[1]/table/tbody/tr/td/div[2]/div/div[2]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[1]/div/table/tbody/tr/td/div[1]/select")
                    yearsStableType = stableType.find_elements_by_tag_name("option")

                    stable = stableType = driver.find_element_by_xpath("/html/body/form[1]/table/tbody/tr[3]/td/div/div[1]/table/tbody/tr/td/div[2]/div/div[2]/table/tbody/tr[2]/td[3]/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div[1]/select")
                    yearsStable = stable.find_elements_by_tag_name("option")

                    tabla = driver.find_elements_by_class_name("xt")
                    nombreArchivo = yearsValues[i].text + "_" + yearsRegion[j].text + "_"  + yearsStableType[k].text + "_" + yearsStable[l].text + ".csv"

                    try:

                        dataF = {'Column 1': [1, 2], 'Column 2': [3, 4]}

                        df = pd.DataFrame(data=dataF)
                        print(df)
                        df.to_csv("test2.csv", index=False)                      
                        print(nombreArchivo)    
                    except:
                        print("No se ha guardado la tabla.")
                        print(nombreArchivo)

    driver.close()

if __name__ == '__main__':
    descargarTablas()