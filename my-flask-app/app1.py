from flask import Flask, render_template,request,jsonify
import pymysql


app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='do0614',
        database='my_db',
    )


@app.route("/user")
def detailUser():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM user where user_idx=3")
        users = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(users)
    except Exception as e:
        return jsonify({"error": str(e)})
    
if __name__ == "__main__":
    app.run(debug=True)