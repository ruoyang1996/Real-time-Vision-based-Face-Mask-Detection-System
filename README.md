# Real-time Vision-based Face Mask Detection

## Environment
Pytorch > 1.2  
OpenCV, Numpy, etc.

## File Explanation
`train.py`: used for training YOLOv4-baed model.    
`eval.py`: used for evaluating trained model and testing interative interface.

## Dataset 
[AIZOO dataset](https://github.com/AIZOOTech/FaceMaskDetection) is used for training and testing models.

## How to start

### 1. Download weight file
* Darknet pre-trained weight :  [yolov4](https://drive.google.com/open?id=1cewMfusmPjYWbrnuJRuKhPMwRe_b9PaT)  
* Make dir `weight/` and put the weight file in.

### 2. Train the model
```Bash
CUDA_VISIBLE_DEVICES=0 nohup python -u train.py  --weight_path weight/yolov4.weights --gpu_id 0 > nohup.log 2>&1 &
```

### 3. Test the model
```Bash
for VOC dataset:
CUDA_VISIBLE_DEVICES=0 python3 eval_voc.py --weight_path weight/xxx.pt --gpu_id 0 --visiual $DATA_TEST --eval --mode val
```
* `xxx` is the name of trained model.

### 4. Detect face mask 
```Bash
CUDA_VISIBLE_DEVICES=0 python3 eval_voc.py --weight_path weight/xxx.pt --gpu_id 0 --visiual $DATA_TEST --det --mode val
```
* `xxx` is the name of trained model.
