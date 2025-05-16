from ultralytics import YOLO


def main():
    model = YOLO('runs/detect/train2/weights/last.pt')  # or yolov8s.pt, etc.
    model.train(data="dataset_big2k/data.yaml", epochs=10, imgsz=640, device='cuda')

if __name__ == '__main__':
    from multiprocessing import freeze_support
    freeze_support()
    main()