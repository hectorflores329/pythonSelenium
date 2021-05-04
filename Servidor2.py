import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup


if __name__ == '__main__':
    df = pd.read_html("<table><tr><th>Company</th><th>Contact</th><th>Country</th>"+
    "</tr> <tr><td>Alfreds Futterkiste</td> <td>Maria Anders</td><td>Germany</td>"+
    "</tr> <tr><td>Centro comercial Moctezuma</td><td>Francisco Chang</td><td>Mexico</td>"+
    "</tr> <tr> <td>Ernst Handel</td> <td>Roland Mendel</td> <td>Austria</td></tr>"+
    "<tr>  <td>Island Trading</td><td>Helen Bennett</td><td>UK</td></tr>"+
    "<tr>  <td>Laughing Bacchus Winecellars</td> <td>Yoshi Tannamuri</td><td>Canada</td></tr>"+
    "<tr> <td>Magazzini Alimentari Riuniti</td><td>Giovanni Rovelli</td> <td>Italy</td> </tr>"+
    "</table>")[0]
    print(df)