from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector


MEMBERS = [
    {
        'id': '1',
        'firstname': 'casa',
        'lastname': 'blanca',
        'address': 'Ain Diab'
    },
    {
        'id': '2',
        'firstname': 'like',
        'lastname': 'that',
        'address': 'Oasis city'
    },
    {
        'id': '3',
        'firstname': 'ok',
        'lastname': 'that',
        'address': 'Oasis city'
    }
]

isAdmin = True

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

connection_params = {
    'host': "localhost",
    'user': "crudvuejsdb",
    'password': "crudvuejsdb",
    'database': "crudvuejsdb",
}

# enable CORS
CORS(app, ressources={r'/*':{'origins': '*'}})

# check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong')

@app.route('/members', methods=['GET'])
def all_members():
    return jsonify({
        'status': 'success',
        'members': MEMBERS
    })

@app.route('/')
def home():
    try:
        if not isAdmin:
            return jsonify({
                'status': 'success',
                'members': [],
                'message': 'Unauthenticated'
            })
        
        with mysql.connector.connect(**connection_params) as db :
            with db.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * from members order by id")
                userslist = cursor.fetchall()
                return jsonify({
                    'status': 'success',
                    'members': userslist
                })
    except Exception as e:
        print("ERREUR ",e)

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    try:
        response_object = {'status': 'success'}
        if request.method == 'POST':
            if not isAdmin:
                return jsonify({
                    'status': 'success',
                    'message': 'Unauthenticated'
                })
            
            post_data = request.get_json(silent=True)
            firstname = post_data.get('firstname')
            lastname = post_data.get('lastname')
            address = post_data.get('address')
    
            print(firstname)
            print(lastname)
    
            sql = "INSERT INTO members(firstname,lastname,address) VALUES(%s, %s, %s)"
            data = (firstname, lastname, address)
            with mysql.connector.connect(**connection_params) as db :
                with db.cursor(dictionary=True) as cursor:
                    cursor.execute(sql, data)
                    db.commit()
    
                    response_object['message'] = "Successfully Added"
        return jsonify(response_object)
    except Exception as e:
        print("ERREUR ",e)

@app.route('/edit/<string:id>', methods=['GET', 'POST'])
def edit(id):
    try:
        if not isAdmin:
            return jsonify({
                'status': 'success',
                'editmember': [],
                'message': 'Unauthenticated'
            })

        with mysql.connector.connect(**connection_params) as db :
                with db.cursor(dictionary=True) as cursor:
                    print(id)
                    cursor.execute("SELECT * FROM members WHERE id = %s", [id])
                    row = cursor.fetchone() 
                    print("pass")
                    return jsonify({
                        'status': 'success',
                        'editmember': row
                    })
    except Exception as e:
        print("ERREUR ",e)
    finally:
        db.close()

@app.route('/update', methods=['GET', 'POST'])
def update():
    try:
        if not isAdmin:
            return jsonify({
                'status': 'success',
                'message': 'Unauthenticated'
            })
        
        print("HERE")
        response_object = {'status': 'success'}
        if request.method == 'POST':
            post_data = request.get_json(silent=True)
            edit_id = post_data.get('edit_id')
            edit_firstname = post_data.get('edit_firstname')
            edit_lastname = post_data.get('edit_lastname')
            edit_address = post_data.get('edit_address')
    
            print(edit_firstname)
            print(edit_lastname)
            try:
                with mysql.connector.connect(**connection_params) as db :
                    with db.cursor(dictionary=True) as cursor:
                        cursor.execute ("UPDATE members SET firstname=%s, lastname=%s, address=%s WHERE id=%s",(edit_firstname, edit_lastname, edit_address, edit_id))
                        db.commit()
                        cursor.close()
        
                        response_object['message'] = "Successfully Updated"
                return jsonify(response_object)
            except Exception as e:
                print("ERREUR ",e)
            finally:
                db.close()
    except Exception as e:
        print("ERREUR ",e)
    finally:
        db.close()
    
@app.route('/delete/<string:id>', methods=['GET', 'POST'])
def delete(id):
    try:
        if not isAdmin:
            return jsonify({
                'status': 'success',
                'message': 'Unauthenticated'
            })
        
        with mysql.connector.connect(**connection_params) as db :
            with db.cursor(dictionary=True) as cursor:
   
                response_object = {'status': 'success'}
            
                cursor.execute("DELETE FROM members WHERE id = %s", [id])
                db.commit()
                cursor.close()
                response_object['message'] = "Successfully Deleted"
        return jsonify(response_object)
    except Exception as e:
        print("ERREUR ",e)
    finally:
        db.close()

if __name__ == '__main__':
    app.run()