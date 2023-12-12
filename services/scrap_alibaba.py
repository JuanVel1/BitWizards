import requests
from bs4 import BeautifulSoup

def extract_price(price_text):
    # Divide el texto del precio en base al guion
    price_parts = price_text.split('-')
    # Se valida que el texto del precio tenga al menos un elemento, si sólo tiene uno, quiere decir que el precio es único, en caso contrario, se toma el primer elemento
    if len(price_parts) > 0:
        price = float(price_parts[0].strip().replace('$', '').replace(',', ''))
        return price
    
def scrape_alibaba(search_term):
    url = requests.get(f'https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText={search_term}')
    soup = BeautifulSoup(url.content, 'html.parser')
    productos = soup.find_all("div", class_="fy23-search-card fy23-gallery-card m-gallery-product-item-v2 J-search-card-wrapper")

    # Extraer los datos de los productos
    product_data = get_products_data(productos)

    # Devolver la lista de productos
    return product_data

# Función para extraer los datos de los productos
def get_products_data(productos):
    product_data = []
    for prod in productos:
        # Extraer el nombre del producto
        name = prod.find("h2", class_="search-card-e-title").text.strip()

        # Extraer la imagen del producto
        img_tag = prod.find("img")
        image = img_tag['src'] if img_tag else 'Not found'
        image= 'https:'+image

        # Extraer el precio del producto
        price_text = prod.find("div", class_="search-card-e-price-main").text.strip()

        # Utiliza la función extract_price para obtener el precio
        min_price = extract_price(price_text)
        
        # Convierte el precio a COP
        min_price = min_price * 4249.00
        min_price = round(min_price, 2)  # Asumiendo una tasa de conversión Post se intento utilizar librerias de conversion de moneda pero no funcionaron
        
        # Extraer el enlace del producto
        link_tag = prod.find("a")
        link = link_tag['href'] if link_tag else 'Not found'
        link = 'https:' + link if link.startswith('//') else link

        # Añadir el producto a la lista de productos
        product_data.append({
            'Product': name,
            'Price': min_price,
            'Link': link,
            'Image': image
        })
    return product_data