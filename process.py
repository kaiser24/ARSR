import glob, os

# Current directory
#current_dir = os.path.dirname(os.path.abspath(__file__))
current_dir = os.path.dirname('/home/pdi/ARSR/dataset/')

# Directory where the data will reside, relative to 'darknet.exe'
path_data = '/home/pdi/darknet2/darknet2/ARSR/dataset/'

# Percentage of images to be used for the test set
percentage_test = 10

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')  
file_test = open('test.txt', 'w')

# Populate train.txt and test.txt
counter = 1  
index_test = round(100 / percentage_test)  
#print( glob.glob(os.path.join(current_dir, "*.jpg")))
for pathAndFilename in glob.glob(os.path.join(current_dir, "*.jpg")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    print("Asda")
    if counter == index_test:
        counter = 1
        file_test.write(path_data + title + '.jpg' + "\n")
    else:
        file_train.write(path_data + title + '.jpg' + "\n")
        counter = counter + 1
