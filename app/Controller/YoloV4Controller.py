from google.api_core.gapic_v1 import method
from app import app
from PIL import Image, ImageFont, ImageDraw
# from app.Service.YoloV4Service import img, YoloV4Recognition
from flask import jsonify
from datetime import datetime
import requests
from flask import request
#from app.utils.test import YoloV4Recognition, img
from app.Service.YoloV4Service import YoloV4Recognition, img

@app.route("/", methods=["GET", "POST"])
def hello():
    return "hello"

@app.route('/post', methods=['POST','GET'])
def hellFlask_post():      
    result =YoloV4Recognition(img())
    print(result)
    return jsonify(result)
    