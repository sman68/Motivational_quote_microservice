from flask import Flask, request, jsonify
import random
import json

app = Flask(__name__)

# Load quotes from JSON file
with open('quotes.json', 'r', encoding='utf-8') as file:
    quotes = json.load(file)

@app.route('/quotes', methods=['GET'])
def get_quote():
    category = request.args.get('category')
    if category:
        category_quotes = quotes.get(category)
        if not category_quotes:
            return jsonify({"error": "Category not found"}), 404
        quote = random.choice(category_quotes)
    else:
        all_quotes = [quote for category_quotes in quotes.values() for quote in category_quotes]
        quote = random.choice(all_quotes)
    return jsonify({"quote": quote})

@app.route('/quotes/favorite', methods=['POST'])
def favorite_quote():
    quote = request.json.get('quote')
    if not quote:
        return jsonify({"error": "No quote provided"}), 400
    with open('favorites.json', 'a', encoding='utf-8') as file:
        file.write(json.dumps({"quote": quote}, ensure_ascii=False) + '\n')
    return jsonify({"message": "Quote favorited"}), 201

@app.route('/quotes/favorites', methods=['GET'])
def get_favorites():
    try:
        with open('favorites.json', 'r', encoding='utf-8') as file:
            favorites = [json.loads(line) for line in file]
        return jsonify(favorites)
    except FileNotFoundError:
        return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
