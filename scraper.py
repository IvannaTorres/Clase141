from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# Enlace a NASA Exoplanet
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

# Controlador web





# Definir el método de extracción de datos para Exoplanet
def scrape():

    
        
        # Objeto BeautifulSoup
        

        # Bucle para encontrar los elementos usando XPATH
        
           
            

            

                
                    

        # Encontrar todos los elementos en la página y hacer clic para desplazarse a la siguiente
        browser.find_element(by=By.XPATH, value='//*[@id="primary"]/div/div[3]/div/div/div/div/div/div/div[2]/div[2]/nav').click()

# Llamada del método
scrape()

print(len(planets_data))

# Definir los encabezados
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]

# Definir el dataframe de Pandas


# Convertir a CSV

