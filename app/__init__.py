from flask import Flask


app = Flask(__name__,  static_url_path="/result",static_folder="./static/result_img/")



from app.Controller import YoloV4Controller

