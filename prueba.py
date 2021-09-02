from flask import Flask, jsonify, request #import objects from the Flask model
app = Flask(__name__) #define app using Flask

languages = [{'name' : 'JavaScript'}, {'name' : 'Python'}, {'name' : 'Ruby'}]

#El metodo GET mostrara este mensaje si no se colocan parametros
@app.route('/', methods=['GET'])
def test():
	return jsonify({'message' : 'It works!'})

#El metodo GET mostrara la lista si se coloca /lang
@app.route('/lang', methods=['GET'])
def returnAll():
	return jsonify({'languages' : languages})

#El metodo GET mostrara el lenguaje escrito en la ruta /lang/language
@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
	langs = [language for language in languages if language['name'] == name]
	return jsonify({'language' : langs[0]})

#El metodo POST añadira un elemento a la lista leyendo un json
@app.route('/lang', methods=['POST'])
def addOne():
	language = {'name' : request.json['name']}

	languages.append(language)
	return jsonify({'languages' : languages})

#El metodo PUT modificara algun elemento de la lista
@app.route('/lang/<string:name>', methods=['PUT'])
def editOne(name):
	langs = [language for language in languages if language['name'] == name]
	langs[0]['name'] = request.json['name']
	return jsonify({'language' : langs[0]})

#El metodo DELETE eliminara un elemento de la lista
@app.route('/lang/<string:name>', methods=['DELETE'])
def removeOne(name):
	lang = [language for language in languages if language['name'] == name]
	languages.remove(lang[0])
	return jsonify({'languages' : languages})

if __name__ == '__main__':
	app.run(debug=True, port=3000) #run app on port 8080 in debug mode