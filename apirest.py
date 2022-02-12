from flask import Flask
from flask import render_template, request, redirect, url_for
import json

app = Flask(__name__)

customers = [{'id': 1, 'name': 'danny', 'address': 'tel-aviv'},
             {'id': 2, 'name': 'suzi', 'address': 'california'},
             {'id': 3, 'name': 'rubi', 'address': 'tokyo'}]

@app.route('/customers', methods = ['GET','POST'])
def getpostcustomer():
    if request.method == 'GET':
        return json.dumps(customers)
    if request.method == 'POST':
        new_customer = request.get_json()
        print(new_customer)
        customers.append(new_customer)
        return json.dumps(customers)

@app.route('/customers/<int:id>', methods=['PUT', 'DELETE']) # add 'GET'
def putdeletecustomer(id):
    if request.method == 'DELETE':
        result = [c for c in customers if c["id"] != id]
        return json.dumps(result)
    if request.method == 'PUT':
        updated_customer = request.get_json()
        print(updated_customer)
        for c in customers:
            if c["id"] == id:
                c["id"] = updated_customer["id"]
                c["name"] = updated_customer["name"]
                c["address"] = updated_customer["address"]
        return json.dumps(customers)
    # add get by id 

app.run()
