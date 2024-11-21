import os
import shutil


audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")

pdf = (".pdf")

zipf = (".zip")

office = (".csv",".docx")


def is_audio(file):
    return os.path.splitext(file)[1] in audio

def is_pdf(file):
    return os.path.splitext(file)[1] in pdf

def is_zip(file):
    return os.path.splitext(file)[1] in zipf


def is_office(file):
    return os.path.splitext(file)[1] in office

def is_video(file):
    return os.path.splitext(file)[1] in video

def is_image(file):
    return os.path.splitext(file)[1] in img

def is_screenshot(file):
    name, ext = os.path.splitext(file)
    return (ext in img) and "screenshot" in name.lower()

os.chdir("/Users/alexbanoun/Downloads")

for file in os.listdir():
    if file == ".DS_Store":
        continue

    # Determine the target subdirectory based on the file type
    if is_audio(file):
        target_subdir = "audio"
    elif is_video(file):
        target_subdir = "video"
    elif is_pdf(file):
        target_subdir = "PDFs"
    elif is_zip(file):
        taget_subdir = "ZIPs"
    elif is_office(file):
        target_subdir = "Office"
    elif is_image(file):
        if is_screenshot(file):
            target_subdir = "screenshots"
        else:
            target_subdir = "images"
    else:
        target_subdir = "other"  # For files that don't match any category

    # Construct the target path
    target_path = os.path.join("/Users/alexbanoun/Documents", target_subdir)

    # Ensure the target subdirectory exists, create if not
    if not os.path.exists(target_path):
        os.makedirs(target_path)

    # Construct the full target file path
    destination = os.path.join(target_path, file)

    # Check if the destination file already exists
    if os.path.exists(destination):
        print(f"Skipping {file} as it already exists in the destination.")
        continue

    # Move the file to the target directory
    shutil.move(file, target_path)
