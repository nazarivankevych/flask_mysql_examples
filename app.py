from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(host=os.getenv('MYSQL_HOST', 'localhost'),
                                   user=os.getenv('MYSQL_USER', 'root'),
                                   password=os.getenv('MYSQL_PASSWORD', ''),
                                   database=os.getenv('MYSQL_DATABASE', 'test_db'))


@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT DATABASE();')
    db_name = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify({'database': db_name})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
