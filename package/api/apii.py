''' Put and deleete  HTTP Methods
  Eorking with API - Json - Flask'''
from flask import Flask , jsonify , request
app = Flask(__name__)
## itnitial data in my do do list

items = [
    {"id": 1, "name": "item one", "decription": "this is item one"},
    {"id": 2, "name": "item two", "decription": "this is item two"},
]
@app.route('/')
def home():
    return "Welcome to my API"

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)
## rttrive sprecific items by ID:

@app.route('/items/<int:item_id>', methods=['GET'])
def get_all_items(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "No item found with the given ID"}), 404
    return jsonify(item)

## $ bew Task :-
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error": "Name field is required"}), 400
    new_item = {
        "id": items[-1]['id'] + 1 if items else 1,
        "name": request.json['name'],
        "decription": request.json.get('decription', "")
    }
    items.append(new_item)
    return jsonify(new_item)

## put method to update an existing item
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item = next ((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    item['name'] = request.json.get('name', item['name'])
    item['decription'] = request.json.get('decription', item['decription'])
    return jsonify(item)

## delete method to remove an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    items.remove(item)
    return jsonify({"result": "Item deleted successfully"})


if __name__ == '__main__':
    app.run(debug=True)