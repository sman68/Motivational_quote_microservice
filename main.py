import requests

def get_random_quote():
    response = requests.get("http://localhost:5000/quotes")
    if response.status_code == 200:
        return response.json()["quote"]
    else:
        return "Error: Could not retrieve quote"

def get_category_quote(category):
    response = requests.get(f"http://localhost:5000/quotes?category={category}")
    if response.status_code == 200:
        return response.json()["quote"]
    else:
        return "Error: Could not retrieve quote"

def favorite_quote(quote):
    url = "http://localhost:5000/quotes/favorite"
    response = requests.post(url, json={"quote": quote})
    return response.status_code == 201

def get_favorites():
    response = requests.get("http://localhost:5000/quotes/favorites")
    if response.status_code == 200:
        return response.json()
    else:
        return "Error: Could not retrieve favorites"

if __name__ == '__main__':
    # Example pip uninstall click requests
    
    quote = get_random_quote()
    print("Random Quote:", quote)

    if favorite_quote(quote):
        print("Quote favorited successfully")
    else:
        print("Error: Could not favorite quote")

    favorites = get_favorites()
    print("Favorite Quotes:", favorites)
