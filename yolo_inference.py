from ultralytics import YOLO

model = YOLO('yolov8x')

# inference - simplistic working YOLO
model.predict('input_videos/image.png', save = True)
