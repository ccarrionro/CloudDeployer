from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Conexión a la base de datos SQLite
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Ruta para la página principal
@app.route('/')
def index():
    return '¡Hola desde Flask y SQLite!'

# Ruta para agregar datos a la base de datos
@app.route('/add', methods=['POST'])
def add_entry():
    conn = get_db_connection()
    cursor = conn.cursor()
    new_entry = request.json['entry']
    cursor.execute("INSERT INTO entries (entry) VALUES (?)", (new_entry,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'Entry added successfully!'})

# Iniciar la app Flask
if __name__ == '__main__':
    app.run(debug=True)
