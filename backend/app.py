from flask import Flask, jsonify, request
import pymysql
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# # Configure MySQL connection
# db = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='Kh@ls@13032003',
#     database='trial'
# )

# # Create a cursor object to execute SQL queries
# cursor = db.cursor()

@app.route('/get_value', methods=['GET'])
def get_value_from_mysql():

    db = pymysql.connect(
        host='localhost',
        user='root',
        password='Kh@ls@13032003',
        database='trial'
    )
    cursor = db.cursor()
    
    try:
        # Execute a sample SQL query to fetch a value
        cursor.execute("SELECT username FROM new_users;")
        
        # Fetch one result
        result = cursor.fetchone()
        
        # Convert the result to JSON format
        value = {'value': result[0]} if result else {'value': None}
        
        return jsonify(value)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        # Close the cursor and database connection
        cursor.close()
        db.close()

username = 'hargun'
password = 'password'
email = 'hargun@example.com'

@app.route('/insert_data', methods=['POST'])
def insert_data_to_mysql():
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='Kh@ls@13032003',
        database='trial'
    )
    cursor = db.cursor()

    try:
        # Execute an INSERT INTO SQL query to insert data into the table using predefined variables
        cursor.execute("INSERT INTO new_users (username, password, email) VALUES (%s, %s, %s);",
                       (username, password, email))
        
        # Commit the transaction
        db.commit()
        
        return jsonify({'message': 'Data inserted successfully'})
    except Exception as e:
        db.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        # Close the cursor and database connection
        cursor.close()
        db.close()


if __name__ == '__main__':
    app.run(debug=True)
