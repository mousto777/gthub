from flask import Flask, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

# Connexion à MongoDB
client = MongoClient(os.getenv("MONGO_URI"))
db = client["Cluster0gthub"]
collection = db["gthub"]

@app.route('/question', methods=['GET'])
def get_answer():
    question = request.args.get('q')

    # Exemple simple : chercher un document avec un champ "question"
    result = collection.find_one({"question": question})

    if result:
        return jsonify({"reponse": result["reponse"]})
    else:
        return jsonify({"reponse": "Désolé, je n’ai pas trouvé de réponse."})

if __name__ == '__main__':
    app.run()
