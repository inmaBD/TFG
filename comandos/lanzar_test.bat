REM yolo train data=dataset_rotondas.yaml obb model=yolov8n-obb.pt project=rot-yolov8n-obb-auto epochs=600 patience=60 imgsz=512 batch=-1
REM yolo train data=dataset.yaml obb model=yolov8s-obb.pt project=rot-yolov8s-obb-auto epochs=600 patience=60 imgsz=512 batch=-1
REM yolo train data=dataset.yaml obb model=yolov8m-obb.pt project=rot-yolov8m-obb-auto epochs=600 patience=60 imgsz=512 batch=-1
REM yolo train data=dataset.yaml obb model=yolov8l-obb.pt project=rot-yolov8l-obb-auto epochs=600 patience=60 imgsz=512 batch=-1
yolo val data=dataset_test.yaml obb model= pruebaM/train/weights/best.pt project=pruebaM_F_T imgsz=512 batch=1 
yolo val data=dataset_test.yaml obb model= pruebaL/train/weights/best.pt project=pruebaL_F_T imgsz=512 batch=1 
yolo val data=dataset_test.yaml obb model= pruebaX/train/weights/best.pt project=pruebaX_F_T imgsz=512 batch=1 

REM Te genera la val y predic de la cxarpeta test
