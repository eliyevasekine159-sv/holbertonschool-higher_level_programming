#!/usr/bin/python3
"""
Flask application that reads data from a JSON file and renders it
using Jinja loops and conditionals.
"""
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Renders the index page"""
    return render_template('index.html')


@app.route('/about')
def about():
    """Renders the about page"""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Renders the contact page"""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Reads items from items.json and renders them in items.html"""
    try:
        with open('items.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []

    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
