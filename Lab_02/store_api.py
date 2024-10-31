import requests

URL_FAKE = "https://fakestoreapi.com/products"

def get_all_categories_lab_two():
    url = f"{URL_FAKE}/categories"
    response = requests.get(url)

    if response.status_code == 200:
        categories = response.json()
        return categories
    else:
        return f"Failed to retrieve categories. Status code: {response.status_code}"

def get_all_products_lab_two():
    url = URL_FAKE
    response = requests.get(url)

    if response.status_code == 200:
        products = response.json()
        return products
    else:
        return f"Failed to retrieve products. Status code: {response.status_code}"
    

def get_product_details_lab_two(product_id):
    url = f"{URL_FAKE}/{product_id}"
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        try:
            product = response.json()
            return product
        except ValueError:
            return f"Invalid response format from server. There was an error in retrieving product details for product ID: {product_id}"
    else:
        return f"Failed to retrieve product details. Status code: {response.status_code}"
    
def add_new_product_lab_two(product):
    url = URL_FAKE
    response = requests.post(url, json=product)
    
    if response.status_code == 200:
        return product
    else:
        return f"Failed to add product. Status code: {response.status_code}"