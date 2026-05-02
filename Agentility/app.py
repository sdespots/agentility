from flask import Flask, jsonify
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()
db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/db-test", methods=["GET"])
def db_test():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        row = result.fetchone()
    return jsonify({"db_test": row[0]})

if __name__ == "__main__":
    app.run(debug=True)