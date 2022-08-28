from flask import Blueprint, jsonify, request, json


mod = Blueprint('user', __name__, url_prefix='/user')


data = json.load(open('D:\First Flask\First_flask\data.json'))
print(data)


@mod.route('/', methods=['GET'])
def fetchall():
    return data

@mod.route('/<user_id>', methods=['GET'])
def show(user_id):
    response = [x for x in data if x['id'] == int(user_id)]
    return jsonify(response)


@mod.route('/fetch_user/', methods=['GET'])
def fetch_user():
    user_id = request.args.get('user_id')
    user_detail = [x for x in data if x['id'] == int(user_id)]
    user_detail = user_detail[0] if user_detail else {}
    return jsonify(user_detail)


@mod.route('/create_user', methods=['POST'])
def create_user1():
    request_data = request.get_json()
    new_user_id = data[-1]['id'] + 1
    response = request_data
    response['id'] = new_user_id
    data.append(response)
    json.dump(data, open('D:\First Flask\First_flask\data.json','w'))
    return jsonify((response))


@mod.route('/create_user_form', methods=['post'])
def create_user2():
    name = request.form.get('name')
    password = request.form.get('password')
    new_user_id = data[-1]['id'] + 1
    response = {
        'id': new_user_id,
        'name': name,
        'password': password
    }
    data.append(response)
    json.dump(data, open('D:\First Flask\First_flask\data.json', 'w'))
    return jsonify((response))


@mod.route('/update_user/<user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.get_json()
    for d in data:
        if d['id'] == int(user_id):
            if 'name' in user_data:
                d['name'] = user_data['name']
            if 'password' in user_data:
                d['password'] = user_data['password']
    json.dump(data, open('D:\First Flask\First_flask\data.json', 'w'))
    return "user details updataed successfully"


@mod.route('/delete_user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    for index, d in enumerate(data):
        if d['id'] == int(user_id):
            del data[index]
    json.dump(data, open('D:\First Flask\First_flask\data.json', 'w'))
    return "user has been deleted  successfully"

