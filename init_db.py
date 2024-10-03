import sqlite3

# Conectar a SQLite
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Crear tabla de ejemplo
cursor.execute('''
    CREATE TABLE IF NOT EXISTS entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        entry TEXT NOT NULL
    )
''')

# Guardar cambios y cerrar la conexión
conn.commit()
conn.close()

print("Base de datos inicializada.")
