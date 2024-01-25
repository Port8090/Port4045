from ultralytics import YOLO
model = YOLO('./yolov8n.pt')
results = model.predict(source="./images/", save = True)
print(results)