import pymysql
from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
from flask_restful import Resource, Api


#Create an instance of Flask
app = Flask(__name__)

#CORS(app)
#Create an instance of MySQL
mysql = MySQL()

#Create an instance of Flask RESTful API
api = Api(app)

#Set database credentials in config.
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Mani@123'
app.config['MYSQL_DATABASE_DB'] = 'urldb'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'

#Initialize the MySQL extension
mysql.init_app(app)


#Get All Users, or Create a new user
class URLList(Resource):
    def get(self):
        try:
            conn = mysql.connect()
            # cursor = conn.cursor()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            # cursor.execute("""select * from otg_demo_users""")
            cursor.execute("SELECT id, shorturl, longurl, hitcount FROM urls")
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def post(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            data = request.get_json()
            _shorturl = data['shorturl']
            _longurl = data['longurl']
            _hitcount = data['hitcount']
            insert_user_cmd = """INSERT INTO urls(shorturl, longurl, hitcount) 
                                VALUES(%s, %s, %s)"""
            cursor.execute(insert_user_cmd, (_shorturl, _longurl, _hitcount))
            conn.commit()
            response = jsonify(message='User added successfully.', id=cursor.lastrowid, shorturl=_shorturl)
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers.add('Access-Control-Allow-Origin', '*')

            #response.data = cursor.lastrowid
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to add user.')         
            response.status_code = 400 
        finally:
            cursor.close()
            conn.close()
            return(response)
            
#Get a user by id, update or delete user
class URL(Resource):
    def get(self, id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute('select * from urls where id = %s',id)
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def post(self, id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            data = request.get_json()
            _shorturl = data['shorturl']
            cursor.execute('select * from urls where shorturl = %s',_shorturl)
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def put(self, id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            data = request.get_json()
            _hitcount = data['hitcount']
            update_user_cmd = """update urls 
                                 set hitcount=%s
                                 where id=%s"""
            cursor.execute(update_user_cmd, (_hitcount, id))
            conn.commit()
            response = jsonify('User updated successfully.')
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to update user.')         
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()    
            return(response)       

    def delete(self, user_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute('delete from otg_demo_users where id = %s',user_id)
            conn.commit()
            response = jsonify('User deleted successfully.')
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to delete user.')         
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()    
            return(response)       

#API resource routes
api.add_resource(URLList, '/urls', endpoint='urls')
api.add_resource(URL, '/url/<int:id>', endpoint='url')

if __name__ == "__main__":
    app.run(debug=True)