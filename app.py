from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS
from indexer import retrieve_query

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


@app.route('/<query>', methods=['GET'])
def shark(query):
    print("The query is : " +query)
    result_df = retrieve_query(query)
    result_json = result_df.to_dict(orient='records')
    return jsonify(result_json)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
