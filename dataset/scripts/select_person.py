import os
import json
import shutil
from pycocotools.coco import COCO

# Define the path of the original COCO2017 train annotations file
coco_train_file = "/coco/original_coco/annotations/instances_val2017.json"

# Create a new JSON file to store the person images and annotations
person_coco_file = "/coco/person_only/annotations/instances_val2017.json"



# Load the COCO API with the original annotations file
coco = COCO(coco_train_file)

# Get the category id of person class
person_id = coco.getCatIds(catNms=["person"])[0]

# Get the image ids of images that contain person class
person_img_ids = coco.getImgIds(catIds=[person_id])

# Get the image and annotation details of person images
person_imgs = coco.loadImgs(person_img_ids)
person_anns = coco.loadAnns(coco.getAnnIds(imgIds=person_img_ids, catIds=[person_id]))

# Copy the info and licenses fields from the original file
person_coco = {}
person_coco["info"] = coco.dataset["info"]
person_coco["licenses"] = coco.dataset["licenses"]

# Add the person images and annotations to the new file
person_coco["images"] = person_imgs
person_coco["annotations"] = person_anns

# Add a single category for person class
person_coco["categories"] = [{"id": person_id, "name": "person", "supercategory": "person"}]

# Save the new file as JSON format
with open(person_coco_file, "w") as f:
    json.dump(person_coco, f)

print(f"Saved {len(person_imgs)} person images and {len(person_anns)} person annotations to {person_coco_file}")


# -----------------------image part--------------------------------------------


# Define the path of the original COCO2017 train images folder
coco_train_folder = "/coco/original_coco/images/val2017"

# Create a new folder to store the person images
person_img_folder = "/coco/person_only/images/val2017"
os.makedirs(person_img_folder, exist_ok=True)





# Copy the person images from the original folder to the new folder
for img in person_imgs:
    img_name = img["file_name"]
    img_path = os.path.join(coco_train_folder, img_name)
    shutil.copy(img_path, person_img_folder)

