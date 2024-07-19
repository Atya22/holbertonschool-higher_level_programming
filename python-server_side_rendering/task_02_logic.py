#!/usr/bin/python
from flask import Flask, render_template, jsonify
import os

def create_app():
    app = Flask(__name__)

    def load_items_from_file(file_path):
        if not os.path.exists(file_path):
            return []
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file).get('items', [])

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/contact')
    def contact():
        return render_template('contact.html')

    @app.route('/items')
    def items():
        items_list = load_items_from_file('items.json')
        return render_template('items.html', items=items_list)

    return app

if __name__ == '__main__':
    app_instance = create_app()
    app_instance.run(debug=True, port=5000)