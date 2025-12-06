from ultralytics import YOLO
import torch

def train():
    print("Using CUDA:", torch.cuda.is_available())
    model = YOLO("yolov8s.pt")  

    results = model.train(
        data="data.yaml",          
        imgsz=960,                
        epochs=100,                
        batch=8,                  
        workers=4,
        device=0,
        patience=15,

        #augmentation
        hsv_h=0.015,               
        hsv_s=0.7,
        hsv_v=0.4,
        degrees=0.0,               
        translate=0.1,
        scale=0.5,
        shear=0.0,
        flipud=0.0,               
        fliplr=0.5,                
        mosaic=0.7,               
        mixup=0.1,                 

        
        lr0=0.001,                 
        lrf=0.01,               
        weight_decay=0.0005,
        warmup_epochs=3,

        # enhance quality
        close_mosaic=10,           
        pretrained=True,
        optimizer="AdamW",           
        amp=True,                  
        cache=True,

        #create file
        name="Genshin_Enemy_V1",
        exist_ok=True
    )

    print("Done!")

if __name__ == "__main__":
    train()
