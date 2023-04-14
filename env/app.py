from flask import Flask
from flask_cors import CORS
import pymongo
import json
from bson import ObjectId
import json
from flask import jsonify



app = Flask(__name__)

CORS(app)
@app.route("/Threats")
def threats():
    class JSONEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, ObjectId):
                return str(o)
            return json.JSONEncoder.default(self, o)

    client = pymongo.MongoClient("mongodb+srv://GUIMongoDb:BAJASEC123@cluster0.gsdusly.mongodb.net/?retryWrites=true&w=majority")
    db = client.BAJAsecDB
    collection = db.ThreatConfidence
    get = (collection.find().sort([('_id', -1)]).limit(1))
    print("the result is: ",get)
    for record in get:
        confidence = (record['Confidence'])
        time = (record['Time'])
    #The bellow code uses a loop to save the cursor
    #data to a json object using the json_util

    #for doc in get:
     #   json_doc = json.dumps(doc, default=json_util.default)
      #  json_docs["Threat"].append(json_doc)
   # print(get['Confidence'])
    #data = JSONEncoder().encode(get)

    return jsonify(confidence,time)

@app.route("/Members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}

@app.route("/timestamp")
def getTimestamp():
    client = pymongo.MongoClient("mongodb+srv://GUIMongoDb:BAJASEC123@cluster0.gsdusly.mongodb.net/?retryWrites=true&w=majority")
    db = client.BAJAsecDB
    collection = db.ThreatConfidence
    getTs = (collection.find().sort([('_id', -1)]).limit(1))
    for record in getTs:
        timeStamp = (record['Time'])
    return jsonify(timeStamp)



if __name__ == "__main__":
    app.run(debug=True)