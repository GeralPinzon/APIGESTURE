from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/api/gesture', methods=['POST'])
def ejemplo5():
    if request.method == 'POST':

            content = request.get_json(force=True)
            print(content)

            if 'nombre' in content.keys():
                nombre =content['nombre']
            else:
                return jsonify(error='json no es correcto')
            if 'apellido' in content.keys():
                apellido =content['apellido']
            else:
                return jsonify(error='json no es correcto')            
            return jsonify(result='Quien eres? Soy ' + nombre +  apellido,hola="pez")

        

        
if __name__ == "__main__":
    
    app.run(host='0.0.0.0',
            debug=True,
            port=8089)