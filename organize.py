
# importing necessary Libraries
import os
import shutil

raw_dataset = "./dataset_raw"
organized_dataset = "./dataset_organized"


# Create organized folders for train test and annotations
os.makedirs(f"{organized_dataset}/images/train", exist_ok = True)
os.makedirs(f"{organized_dataset}/images/test", exist_ok = True)
os.makedirs(f"{organized_dataset}/annotations/train", exist_ok = True)

# storing the list of countries that we have in our dataset
# At any point of time we can add new dataset files to this list
countries = ["China_MotorBike","Czech","India","Japan","United_States"]

def copy_files(source, destination):

    for file in os.listdir(source):
        # Copying file from source to destination
        shutil.copy(os.path.join(source,file), destination)



for country in countries:
    copy_files(f"{raw_dataset}/{country}/train/images", f"{organized_dataset}/images/train")
    copy_files(f"{raw_dataset}/{country}/train/annotations/xmls", f"{organized_dataset}/annotations/train")
    copy_files(f"{raw_dataset}/{country}/test/images", f"{organized_dataset}/images/test")

print("Dataset has been organized into a unified structure!!!")