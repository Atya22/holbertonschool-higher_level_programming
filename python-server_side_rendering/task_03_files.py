#!/usr/bin/python3

from flask import Flask, render_template, request, Blueprint
import json
import csv
import sqlite3

app = Flask(__name__)
data_bp = Blueprint('data_bp', __name__)

class DataReader:
    @staticmethod
    def read_json(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    @staticmethod
    def read_csv(file_path):
        products = []
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products

    @staticmethod
    def read_sql():
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        conn.close()
        return [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in rows]

@data_bp.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []

    if source == 'json':
        products = DataReader.read_json('products.json')
    elif source == 'csv':
        products = DataReader.read_csv('products.csv')
    elif source == 'sql':
        products = DataReader.read_sql()
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        products = [product for product in products if product['id'] == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found.")

    return render_template('product_display.html', products=products)

app.register_blueprint(data_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)