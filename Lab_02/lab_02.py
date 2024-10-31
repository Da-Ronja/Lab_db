from store_api import get_all_products_lab_two, get_all_categories_lab_two, get_product_details_lab_two, add_new_product_lab_two

def display_all_products():
    products = get_all_products_lab_two()
    if isinstance(products, list):
        print("\nAlla produkter:")
        for product in products:
            print(f"Produktnamn: {product['title']}")
    else:
        print(products)


def display_category_lab_two():
    categories = get_all_categories_lab_two()
    if isinstance(categories, list):
        print("\nVälj en kategori:")
        for index, category in enumerate(categories, start=1):
            print(f"{index}. {category}")
        return categories
    else:
        print(categories)

def choose_category_lab_two():
    categories = display_category_lab_two()
    
    is_valid = False
    while not is_valid:
        try:
            choice = int(input("Ange kategori: "))
            if choice in range(1, len(categories)+1):
                is_valid = True
            else:
                print("Felaktigt val. Ange ett nummer mellan 1 och", len(categories))
        except ValueError:
            print("Felaktig inmatning. Ange ett nummer.")
    return categories[choice-1]

def add_new_product_menu_lab_two():
    is_valid = False
    product = {}
    product["title"] = input("Ange produktnamn: ")

    while not is_valid:
        try:
            product["price"] = float(input("Ange pris: "))
            is_valid = True
        except ValueError:
            print("Felaktig inmatning. Ange ett tal.")
    product["description"] = input("Ange produktbeskrivning: ")
    product['image'] = "https://fakestoreapi.com/img/placeholder.png"
    categories = choose_category_lab_two()
    product["category"] = categories
    
    return product

def display_product_added_lab_two(product):
    print(f"Produkten tillagd: {product}")

def display_product_details_lab_two(product_id):
    product = get_product_details_lab_two(product_id)
    if isinstance(product, dict):
        print("\nProduktdetaljer:")
        print(f"Produktnamn: {product['title']}")
        print(f"Pris: {product['price']}")
        print(f"Beskrivning: {product['description']}")
        print(f"Kategori: {product['category']}")
    else:
        print(product)

def menu_lab_two():
    print("")
    print("1. Visa alla produkter")
    print("2. Visa produktdetaljer")
    print("3. Lägg till ny produkt")
    print("4. Avsluta")

def main_lab_two():
    menu_lab_two()
    choice = input("Välj ett alternativ: ")

    while choice != "4":
        match choice:
            case "1":
                print("Visa alla produkter")
                display_all_products()
            case "2":
                print("Visa produktdetaljer")
                product_id = input("Ange produkt-ID du vill se: ")
                display_product_details_lab_two(product_id)
            case "3":
                print("Lägg till ny produkt")
                product = add_new_product_menu_lab_two()
                product_respons = add_new_product_lab_two(product)
                if isinstance(product_respons, dict):
                    display_product_added_lab_two(product_respons)
                else:
                    print(product_respons)
            case "4":
                print("Avsluta")
            case _:
                print("Felaktigt val. Välj ett alternativ mellan 1-4.")
                
        input("Tryck på valfri tangent för att fortsätta...")
        menu_lab_two()
        choice = input("Välj ett alternativ: ")

    print("Tack för att du använder programmet!")

if __name__ == "__main__":
    main_lab_two()
