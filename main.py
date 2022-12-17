from urllib.request import urlopen
import cv2 as cv
import torch
import numpy as np
import urllib
from test import YoloV5
from Distance import Distance

model = torch.hub.load("ultralytics/yolov5", 'custom', path='best.pt', force_reload=True)

url = r'http://192.168.1.2/capture'
while True:
    img_resp = urlopen(url)
    imgnp = np.asarray(bytearray(img_resp.read()), dtype="uint8")
    img = cv.imdecode(imgnp, -1)
    result = model(img)
    results = Distance.get_result(model, img)
    if results:
        distance = Distance.get_traffic_light_distance(results)
        print(distance)
    cv.imshow("test", np.squeeze(result.render()))
    if cv.waitKey(1) == 113:
        break