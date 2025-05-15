from ultralytics import YOLO


def main():
    model = YOLO('models/yolo12n.pt')  # or yolov8s.pt, etc.
    model.train(data="dataset/data.yaml", epochs=25, imgsz=640)

if __name__ == '__main__':
    from multiprocessing import freeze_support
    freeze_support()
    main()