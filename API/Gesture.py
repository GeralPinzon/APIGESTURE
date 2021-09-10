from translate import translate
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/api/gesture', methods=['POST'])
def ejemplo5():
    if request.method == 'POST':
            content = request.get_json(force=True)
            if 'imageString' in content.keys():
                if content['imageString'] == '':
                    return jsonify(result=''),400
                palabra = translate(content['imageString'])
            if palabra == '':
                return jsonify(result=palabra),404        
            return jsonify(result=palabra),200

if __name__ == "__main__":
    
    app.run(host='0.0.0.0',
            debug=True,
            port=8089)