import os
from shutil import copyfile

org_path = '/home/pdi/OpenLabeling2/main/'
new_path = '/home/pdi/ARSR/dataset/'
output_folder = 'output/YOLO_darknet/'

data_list = []

type_count = 0

for data in os.listdir(org_path + output_folder):
    f = open(org_path + output_folder + data, "r")
    to_copy = 0
    while True:    
        sample = f.readline()
        if not sample.strip():
            break
        else:
            stype = sample.split(' ')[0]
            if(stype == '12'):
                #print(data)
                type_count += 1
                to_copy = 1
    if(to_copy):
        copyfile(org_path + output_folder + data, new_path + data)
        copyfile(org_path+ 'input/' + data.split('.')[0] + '.jpg', new_path + data.split('.')[0] + '.jpg')
        data_list.append(data)
    to_copy = 0

for data in os.listdir(new_path):
    _,ext = os.path.splitext(new_path + data)

    if(ext == '.txt'):
        #image_count += 1
            
        f = open(new_path + data, "r")
        text = []
        while True:    
            sample = f.readline()
            if not sample.strip():
                break
            else:
                stype = sample.split(' ')[0]
                if(stype == '12'):
                    text.append(sample)
        open(new_path + data, 'w').close()
        with open(new_path + data, 'w') as f:
            for line in text:
                f.write("%s" % line)

        #print(type_count)