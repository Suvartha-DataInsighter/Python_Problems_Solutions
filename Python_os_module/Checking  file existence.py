import os
print(os.path.isfile("D:/Myfiles"))
import os

filepaths = ["/folder/soundfile.mp3", "folder1/folder/soundfile.flac"]

for fp in filepaths:
    # Split the extension from the path and normalise it to lowercase.
    ext = os.path.splitext(fp)[-1].lower()

    # Now we can simply use == to check for equality, no need for wildcards.
    if ext == ".mp3":
        print(fp, "is an mp3!")
    elif ext == ".flac":
        print(fp, "is a flac file!")
    else:
        print(fp, "is an unknown file format.")