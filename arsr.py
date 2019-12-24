import cv2, imutils
from darknetfunctions import load_net, load_meta, detect
import os

path = '/home/pdi/ARSR/dataset/'

NET = load_net(b"/home/pdi/darknet2/darknet2/ARSR/yolov3.cfg",
               b"/home/pdi/darknet2/darknet2/backup/yolov3.backup", 0)

'''NET = load_net(b"/home/pdi/aforosDRON/cfg_intertelco/yolov3_4.cfg",
               b"/home/pdi/aforosDRON/DATA_TRAIN/training/backup/yolov3_4.backup", 0)'''

print("cargando metadata ")
METADATA = load_meta(b"/home/pdi/darknet2/darknet2/ARSR/coco.data")
#METADATA = load_meta(b"/home/pdi/aforosDRON/DATA_TRAIN/training/dron4.data")

WIDTHDIVIDER = 1.5

for data in os.listdir(path):
	_,ext = os.path.splitext(path + data)

	if(ext == '.jpg'):
		img = cv2.imread(path + data)
		img = imutils.resize(img, width=int(1920/WIDTHDIVIDER))
		cv2.imwrite('/home/pdi/ARSR/processing/processing.jpg',img)
		detections = detect(NET, METADATA,  b'/home/pdi/ARSR/processing/processing.jpg', thresh=0.003)
		for detection in detections:
			pt1 = (int(detection[2][0]-detection[2][2]/WIDTHDIVIDER),
                   int(detection[2][1]-detection[2][3]/WIDTHDIVIDER))
			pt2 = (int(detection[2][0]+detection[2][2]/WIDTHDIVIDER),
                   int(detection[2][1]+detection[2][3]/WIDTHDIVIDER))

			cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2)
		cv2.imshow('a',img)
	cv2.waitKey(0)
        
	cv2.destroyAllWindows()
		