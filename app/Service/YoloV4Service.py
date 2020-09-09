from app.utils.test import Yolo4
from PIL import Image, ImageFont, ImageDraw
from datetime import datetime
import requests
from flask import request

def YoloV4Recognition(img):
    from datetime import datetime
    print("hi!")
    image = Image.open(img)
    print(image)
    model_path = './app/utils/model_data/yolo_obj_weights.h5'
    anchors_path = './app/utils/model_data/yolo4_anchors.txt'
    classes_path = './app/utils/model_data/obj_classes.txt'
    score = 0.5
    iou = 0.5
    model_image_size = (608, 608)
    yolo4_model = Yolo4(score, iou, anchors_path, classes_path, model_path)
    result = yolo4_model.detect_image(image, model_image_size=model_image_size)
    print("this is a result:", result[0])
    yolo4_model.close_session()
    date_time = datetime.now().strftime("%Y%m%d%H%M%S%f")   
   
    result[1].save(f'./app/static/result_img/{date_time}.png')
    
    
    print("end!")
    return {
        "result": result[0],
        "url": "http://10.120.26.240:8080/result/"+ date_time + ".png"
    }

def img():
    # 下載圖片
    request_data = request.get_json()
    r = requests.get(request_data['url'], stream=True)
    try:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        filename = "./app/static/get_img/get_img1.jpg"
        # Open a local file with wb ( write binary ) permission.
        with open(filename, 'wb') as f:
            f.write(r.content)
        print('成功下載圖檔: ', filename)
        """
        這邊呼叫 Yolov4 預測功能
        """
        return filename

    except Exception as e :
        print(e,"\n 下載失敗")
