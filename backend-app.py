import psycopg2
from psycopg2 import sql
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import pyodbc

app = Flask(__name__)
CORS(app)

def get_db_connection():
    connection = psycopg2.connect(
        host='crack-in-database.postgres.database.azure.com', 
        database='postgres',  
        user='aman123database',  
        password='crackin@123',  
        port=5432,
        sslmode='require'
    )
    return connection



# Connect to the database
def get_db_connection():
    conn = pyodbc.connect(
        f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}'
    )
    return conn



# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM Users WHERE email = ? AND password = ?",
            (email, password)
        )
        user = cursor.fetchone()
        if user:
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'message': 'Invalid email or password'}), 401
    except Exception as e:
        return jsonify({'message': 'Internal server error', 'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
