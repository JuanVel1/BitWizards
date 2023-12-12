from fastapi import APIRouter, HTTPException
from typing import Dict
from services.scraper_services import scrape_amazon
from services.scrap_aliexpress import scrape_aliexpress
from services.scrap_alibaba import scrape_alibaba

router = APIRouter()

# Endpoint para realizar el scraping de Amazon
# Retorna una lista de productos
@router.post("/scrape/")
async def scrape_endpoint(search_data: Dict[str, str]):
    # Verifica si el término de búsqueda está presente en los datos
    if "search_term" not in search_data:
        raise HTTPException(status_code=422, detail="Falta el término de búsqueda")
    
    search_term = search_data["search_term"]
    
    # Llama a la función de scraping con el término de búsqueda
    product_data = scrape_amazon(search_term)

    return {"productos": product_data}


@router.post("/scrape_aliexpress/")
async def scrape_endpoint(search_data: Dict[str, str]):
    # Verifica si el término de búsqueda está presente en los datos
    if "search_term" not in search_data:
        raise HTTPException(status_code=422, detail="Falta el término de búsqueda")
    
    search_term = search_data["search_term"]
    
    # Llama a la función de scraping con el término de búsqueda
    product_data = scrape_aliexpress(search_term)

    return {"productos": product_data}


@router.post("/scrape_alibaba/")
async def scrape_endpoint(search_data: Dict[str, str]):
    # Verifica si el término de búsqueda está presente en los datos
    if "search_term" not in search_data:
        raise HTTPException(status_code=422, detail="Falta el término de búsqueda")
    
    search_term = search_data["search_term"]
    
    # Llama a la función de scraping con el término de búsqueda
    product_data = scrape_alibaba(search_term)

    return {"productos": product_data}

#Se crea un endpoint para realizar el scraping tanto de alibaba como de aliexpress
#Y se retorna una lista combinada de los productos de ambas fuentes ordenada por precio
@router.post("/scrape_both/")
async def scrape_both_endpoints(search_data: Dict[str, str]):
    # Verifica si el término de búsqueda está presente en los datos
    if "search_term" not in search_data:
        raise HTTPException(status_code=422, detail="Falta el término de búsqueda")
    
    search_term = search_data["search_term"]
    
    # Llama a las funciones de scraping con el término de búsqueda en ambas fuentes
    aliexpress_data = scrape_aliexpress(search_term)
    alibaba_data = scrape_alibaba(search_term)
    
    # Ordena la lista combinada por el precio
    combined_data = sorted(aliexpress_data + alibaba_data, key=lambda x: x['Price'])
    
    return {"productos": combined_data}



