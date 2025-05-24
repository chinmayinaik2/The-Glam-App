import requests

def fetch_products_by_tone(tone):
    tone_tag = tone.lower()
    url = f"http://makeup-api.herokuapp.com/api/v1/products.json?product_tags={tone_tag}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        products = response.json()
        return products[:5]
    except Exception as e:
        return [{"name": "Error fetching products", "error": str(e)}]
