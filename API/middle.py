from flask import jsonify
from translate import translate

#import sys
#sys.path.append(".")
#from Command.translate import *

def validation(content):
    if 'imageString' in content.keys():
        if content['imageString'] == '':
            return jsonify(result=''),400
        palabra = translate(content['imageString'])
    if palabra == 'NOT_FOUND':
        return jsonify(result='NOT_FOUND'),404    
    if palabra == 'NOT_HANDS':
        return jsonify(result=''),400
    return jsonify(result=palabra),200