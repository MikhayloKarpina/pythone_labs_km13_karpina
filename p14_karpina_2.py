import json

with open("image_info_test-dev2017.json", "r") as read_file:
    data = json.load(read_file)

counter = 0
for i in data["images"]:
    counter += 1

print(f"JSON document have {counter} photos inside") 

counter = 0
for i in data["categories"]:
    counter += 1

print(f"JSON document have {counter} categories inside")   

for i in data["images"]:
    if i["file_name"] == "000000000001.jpg":
        link = i["coco_url"]
        width = i["width"]
        height = i["height"]
        id = i["id"]
print(f"Link to this photo is {link}\nWindth of this photo is {width} and height of this photo is {height}\nId of this photo is {id}")

current_max = 0
for i in data["images"]:
    digit_name = int(i["file_name"][0:12])
    if current_max < digit_name:
        current_max = digit_name
        max_name = i["file_name"]

print(f"Name of photo with biggest number is {max_name}")