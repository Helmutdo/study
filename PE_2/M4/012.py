# nuevo programa ejemplo de web scrapper
import requests
from bs4 import BeautifulSoup
import csv
# URL de la página web a scrapear
url = 'https://example.com/products'
# Realizar la solicitud GET a la página web
response = requests.get(url)
# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    # Parsear el contenido HTML de la página web
    soup = BeautifulSoup(response.content, 'html.parser')
    # Encontrar todos los elementos que contienen la información de los productos
    products = soup.find_all('div', class_='product-item')
    # Abrir un archivo CSV para escribir los datos
    with open('products.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Escribir la cabecera del CSV
        writer.writerow(['Product Name', 'Price', 'Description'])
        # Iterar sobre cada producto y extraer la información relevante
        for product in products:
            name = product.find('h2', class_='product-name').text.strip()
            price = product.find('span', class_='product-price').text.strip()
            description = product.find('p', class_='product-description').text.strip()
            # Escribir la información del producto en el archivo CSV
            writer.writerow([name, price, description])
    print('Datos de productos guardados en products.csv')

    