def predict_image():
    from ultralytics import YOLO
    model = YOLO('./yolov8n.pt')
    r = model.predict(source=".\images\KakaoTalk_20231017_092510262_0rNq6QF.jpg", save = True)
