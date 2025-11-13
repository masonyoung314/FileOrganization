import os
import shutil 

print(os.getcwd())

# make current directory desktop
os.chdir("/Users/masonyoung/Desktop")
print(os.getcwd())

# print(os.listdir())


file_dir = {
    ".mp3": "Music",
    ".wav": "Music",
    ".png": "Screenshots",
    ".jpg": "Screenshots",
    ".heic": "Screenshots",
    ".pdf": "Documents"
}
if (not os.path.isdir("Music")):
    os.mkdir("Music")

if (not os.path.isdir("Screenshots")):
    os.mkdir("Screenshots")

if (not os.path.isdir("Documents")):
    os.mkdir("Documents")

print(os.listdir())

for file in os.listdir(): 
    fileExt = os.path.splitext(file)[1]
    if fileExt in file_dir:
        shutil.move(file, f"/Users/masonyoung/Desktop/{file_dir[fileExt]}")
        print(os.path.abspath(file))

