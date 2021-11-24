from flask import Flask, jsonify

#default falsk configuration localhost:5000
#provides the foundations for interacting with HTTP requests via the
#WSGI protocol, and various tools such as a routing system

app = Flask(__name__)#one flask instance will be created here 

#a route method, which can decorate your functions When you decorate a
#function with it, it becomes a view, and it's registered into Werkzeug's routing system

@app.route('/') #http://localhost:5000/
def welcome_url():
    return jsonify({"Welcome":"user"})

@app.route('/api') #http://localhost:5000/api
def my_microservice():
    return jsonify({'Hello': 'World!'})

if __name__ == '__main__':
    app.run()