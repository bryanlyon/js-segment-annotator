import os
import sys
import re
import json

# input dir of images
path = sys.argv[1]
# output json file
outfile = sys.argv[2]

# init
prefix1 = "data/images/"
prefix2 = "data/annotations/"
filenames = []
labels = ["background",
    "face",
    "hair",
    "obstructions",
    "glasses"]
imgURLs = []
annotationURLs = []

# collect all images name with jpg extension (change it with your own)
for filename in os.listdir(path):
    if filename.split(".")[1] == "png":
        filenames.append(filename)

# ordered the file names ascending
ordered_files = sorted(filenames, key=lambda x: (int(re.sub('\D','',x)),x))

print("Generate images list")
for i in ordered_files:
    new_path = '{}{}'.format(sys.argv[1], i)
    imgURLs.append(new_path)
print("Generate images list done")

print("Generate annotation list")
for i in ordered_files:
    new_filename = i.split(".")[0]
    new_path = '{}{}.png'.format(prefix2, new_filename)
    annotationURLs.append(new_path)
print("Generate annotation list done")

# construct the json
data = {"labels":labels,
"imageURLs":imgURLs,
"annotationURLs":annotationURLs}

# save to json
with open(outfile, 'w') as fp:
    json_data = json.dump(data, fp, indent=4, sort_keys=True)

# usage : python generatejson.py images_dir output.json
