from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Result

@app.route('/post-value', methods=['POST'])
def postvalue():
    req_data = request.get_json()
    result = Result(result_all=req_data)
    db.session.add(result)
    db.session.commit()
    return {"message": f" {result.result_all} has been created successfully."}

if __name__ == '__main__':
    app.run(debug=True)