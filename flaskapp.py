from flask import Flask,request,jsonify
import psycopg2
from script import *

app=Flask(__name__)

config= {
        "dbname": "postgres",
        "user": "postgres",
        "password": "postgres",
        "host": "postgres-container",
        "port": 5432
}

@app.route("/")
def home():
    return "All good!!!"

@app.route("/insert-data", methods=["POST"])
def add_data():
    try:
        conn= psycopg2.connect(**config)
        cursor= conn.cursor()

        data= request.get_json()
        #data= request
        if data is None:
            return jsonify({"error": "Missing JSON in request"})

        insert_val(cursor, data)
        conn.commit()
        return jsonify({"message": "All good"}), 200
    except Exception as e:
        raise jsonify({"error": str(e)})

    finally:
        conn.close()

@app.route("/show-all")
def show_data():
    try:
        conn= psycopg2.connect(**config)
        cursor= conn.cursor()

        result= show_all_data(cursor)

        return jsonify(result), 200
    except Exception as e:
        raise jsonify({"error": str(e)})
    finally:
        conn.close()



if __name__=="__main__":
    app.run(host= "0.0.0.0", debug=True)
