from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb+srv://moustaphadiopimt:<db_password>@cluster0gthub.0eoswgn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0gthub")
db = client['gthub']
modules_collection = db['modules']

@app.route('/module', methods=['GET'])
def get_module():
    nom = request.args.get('nom')
    module = modules_collection.find_one({"nom": nom})
    if module:
        return jsonify({"nom": module['nom'], "description": module['description'], "responsable": module['responsable']})
    else:
        return jsonify({"error": "Module non trouvé"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
