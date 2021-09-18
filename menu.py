from flask import Flask, jsonify, request #import objects from the Flask model
app = Flask(__name__) #define app using Flask

@app.route('/carga', methods=['GET'])
def test():
	return jsonify({'message' : 'It works!'})