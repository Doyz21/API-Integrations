import requests
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("FAKESTORE_API")

def get_all_products():
    try:
        response = requests.get(f"{BASE_URL}/products")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error saat mengambil data produk: {e}")
        return []