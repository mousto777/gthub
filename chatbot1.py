from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb+srv://moustaphadiopimt:<db_password>@cluster0gthub.0eoswgn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0gthub")
db = client["gthub"]

@app.route("/question", methods=["GET"])
def get_reponse():
    question = request.args.get("q")
    result = db.questions_frequentes.find_one({"question": question})
    if result:
        return jsonify({"reponse": result["reponse"]})
    else:
        return jsonify({"reponse": "Désolé, je n'ai pas compris la question."})

if __name__ == "__main__":
    app.run(debug=True)
