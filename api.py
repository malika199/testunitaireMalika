from flask import Flask, request, Response, jsonify
import json
from pymongo import MongoClient
from flask_restful import Resource, Api
from bson.objectid import ObjectId
import pymongo
db_uri = "mongodb+srv://malika:malika123@cluster0.mu5cs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(db_uri)


app = Flask(__name__)
api = Api(app)

@app.route('/read', methods=['GET'])
def read_product():
    data =  client["pythonapi"]["products"].find()
    print(data)

    dat = [{k: str(v) for k, v in val.items()} for val in data]

    return Response(
        response = json.dumps(dat),
        status = 200,
        mimetype = "application/json"
    )

@app.route("/create", methods=['POST'])
def create_product():
    req = json.loads(request.data)
   
    product ={"name":req["name"], "desc":req["desc"], "price": req["price"]}
    dbResponse = client["pythonapi"]["products"].insert_one(product)
    for attr in dir(dbResponse):
        print(attr)
    return Response(
        response = json.dumps({"message":"prodcut created", "id": f"{dbResponse.inserted_id}"}),
        status = 200,
        mimetype = "application/json"
    )


@app.route("/update/<id>",methods=['PATCH'])
def Update(id):
    req = json.loads(request.data)
    informations =  {"name":req["name"], "desc":req["desc"], "price": req["price"]}
    dbResponse =  client["pythonapi"]["products"].update_one({ '_id': ObjectId(id) }, {'$set': informations})
    for attr in dir(dbResponse):
        print(f"******{attr}********")
        return Response(
            response= json.dumps({"message":"upload sucess"}),
            status=200,
            mimetype="application/json"
        )


@app.route("/delete/<id>", methods = ["DELETE"])
def delete_user(id):
    book_obj = client["pythonapi"]["products"].find_one_and_delete({"_id": ObjectId(id)})
    return Response(
        response= json.dumps({"message":"upload sucess"}),
        status=200,
        mimetype="application/json"
    )


if __name__ == "__main__":
    app.run( debug=True)