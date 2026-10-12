from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/user")
def get_user():
    user_input = request.args.get("id")
    user_input = "123"
    
    # ... some lines in between ...
    
    # Line 20: Sink (Dynamic SQL query execution)
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = " + user_input)
