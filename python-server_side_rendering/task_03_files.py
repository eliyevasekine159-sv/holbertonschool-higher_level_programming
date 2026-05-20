#!/usr/bin/python3
"""
Flask application that reads and displays data from JSON or CSV files
based on user-provided query parameters with error handling.
"""
import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_products():
    """Reads products from products.json file"""
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_csv_products():
    """Reads products from products.csv file"""
    products = []
    try:
        with open('products.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except (FileNotFoundError, KeyError, ValueError):
        pass
    return products


@app.route('/products')
def products():
    """
    Renders products list from json or csv source with optional id filtering.
    """
    source = request.args.get('source')
    product_id = request.args.get('id')

    # 1. Yanlış mənbə (source) yoxlanışı
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    # Mənbəyə uyğun funksiyanı çağırırıq
    if source == 'json':
        product_list = read_json_products()
    else:
        product_list = read_csv_products()

    # 2. Əgər id parametri ötürülübsə, süzgəcdən keçiririk
    if product_id is not None:
        try:
            target_id = int(product_id)
            filtered_list = [p for p in product_list if p.get('id') == target_id]

            # Məhsul tapılmadıqda verilən xəta mesajı
            if not filtered_list:
                return render_template('product_display.html', error="Product not found")

            product_list = filtered_list
        except ValueError:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=product_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
