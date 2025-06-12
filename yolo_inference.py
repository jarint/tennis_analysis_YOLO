from ultralytics import YOLO

model = YOLO('yolov8x')

# inference - simplistic working YOLO
result = model.predict('input_videos/image.png', save = True)
print(result)
print("boxes: ")
for box in result[0].boxes:
    print(box)
