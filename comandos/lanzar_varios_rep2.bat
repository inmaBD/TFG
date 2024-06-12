yolo train data=dataset.yaml obb model=yolov8x-obb.pt project=iteracionRotEnl_auto_2 epochs=600 patience=60 imgsz=512 batch=-1 
yolo train data=dataset.yaml obb model=yolov8x-obb.pt project=iteracionRotEnl_auto_2cos epochs=600 patience=60 imgsz=512 batch=-1 cos_lr=True

yolo train data=dataset.yaml obb model=yolov8x-obb.pt project=iteracionRotEnl_SGD_2 epochs=600 patience=60 imgsz=512 batch=-1 optimizer=SGD
yolo train data=dataset.yaml obb model=yolov8x-obb.pt project=iteracionRotEnl_SGD_2cos epochs=600 patience=60 imgsz=512 batch=-1 optimizer=SGD cos_lr=True

yolo train data=dataset.yaml obb model=yolov8x-obb.pt project=iteracionRotEnl_ADAM_2 epochs=600 patience=60 imgsz=512 batch=-1 optimizer=Adam 
yolo train data=dataset.yaml obb model=yolov8x-obb.pt project=iteracionRotEnl_ADAM_2cos epochs=600 patience=60 imgsz=512 batch=-1 optimizer=Adam cos_lr=True
 
yolo train data=dataset.yaml obb model=yolov8x-obb.pt project=iteracionRotEnl_ADAMW_2 epochs=600 patience=60 imgsz=512 batch=-1 optimizer=AdamW
yolo train data=dataset.yaml obb model=yolov8x-obb.pt project=iteracionRotEnl_ADAMW_2cos epochs=600 patience=60 imgsz=512 batch=-1 optimizer=AdamW cos_lr=True

yolo train data=dataset.yaml obb model=yolov8x-obb.pt project=iteracionRotEnl_NADAM_2 epochs=600 patience=60 imgsz=512 batch=-1 optimizer=NAdam
yolo train data=dataset.yaml obb model=yolov8x-obb.pt project=iteracionRotEnl_NADAM_2cos epochs=600 patience=60 imgsz=512 batch=-1 optimizer=NAdam cos_lr=True

yolo train data=dataset.yaml obb model=yolov8x-obb.pt project=iteracionRotEnl_RADAM_2 epochs=600 patience=60 imgsz=512 batch=-1 optimizer=RAdam
yolo train data=dataset.yaml obb model=yolov8x-obb.pt project=iteracionRotEnl_RADAM_2cos epochs=600 patience=60 imgsz=512 batch=-1 optimizer=RAdam cos_lr=True

yolo train data=dataset.yaml obb model=yolov8x-obb.pt project=iteracionRotEnl_RMSProp_2 epochs=600 patience=60 imgsz=512 batch=-1 optimizer=RMSProp
yolo train data=dataset.yaml obb model=yolov8x-obb.pt project=iteracionRotEnl_RMSProp_2cos epochs=600 patience=60 imgsz=512 batch=-1 optimizer=RMSProp cos_lr=True
 