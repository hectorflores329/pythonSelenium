import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

def saveCSV(tabla, anio, region, tipo_Establecimiento, nombre_establecimiento, nombreArchivo):
    html = tabla[0].get_attribute('innerHTML')
    html = '<table>' + html.text + '</table>'
    html = html.replace(".","")
    data = pd.read_html(html, skiprows=2)
    df = data[0]
    columnas = list(df.columns)
    columnas[0] = "Total"
    columnas.insert(0,"Urgencia")
    columnas.pop(len(columnas) - 1)
    df.columns = columnas
    df["Fecha"] = anio
    df["Region"] = region
    df["Tipo Establecimiento"] = tipo_Establecimiento 
    df["Nombre establecimiento"] = nombre_establecimiento                
    df.to_csv(nombreArchivo, index=False, encoding="UTF-8") # 

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
                        
                        df = pd.read_csv("tabla.txt")
                        df.to_csv("tabla_de_ejemplo.csv", index=False)
                        
                    except:
                        print("No se ha guardado la tabla.")
                        print(nombreArchivo)

    driver.close()

if __name__ == '__main__':
    descargarTablas()