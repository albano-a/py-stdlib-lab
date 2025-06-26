import os
import datetime

# Define a base path
BASE_PATH = "C:/Users/Icarl/Documents/GitHub/py-stdlib-lab/"
os.chdir(BASE_PATH)

# --- Current and New Working Directory ---
print("Current working directory:", os.getcwd())

# Change directory
subdir = "File_IO_&_OS/os/ex"
os.chdir(subdir)
print("Changed to:", os.getcwd())

# --- List Directory Contents ---
items = os.listdir()
for i, item in enumerate(items):
    print(f"[{i}] {item}")

# --- Create Directories ---
if not os.path.exists("codes"):
    os.mkdir("codes")
if not os.path.exists("pythonic/Classes"):
    os.makedirs("pythonic/Classes")

# --- Check Path Types ---
print("Is 'codes' a directory?", os.path.isdir("codes"))
print("Is 'pythonic/Classes' a directory?", os.path.isdir("pythonic/Classes"))
print("Is 'pythonic/Classes' a file?", os.path.isfile("pythonic/Classes"))

# --- Remove Directories ---
os.rmdir("codes")  # Only works if empty

# --- Rename and Move Directories ---
old_path = "pythonic/Classes"
new_path = "pythonic/UpdatedClasses"
os.rename(old_path, new_path)

# Move outside 'pythonic' to current dir
final_path = "UpdatedClasses"
os.replace(new_path, final_path)

# --- File Info: Size and Last Modified Time ---
os.chdir("../../../")  # Go back to project root
readme = "README.md"

if os.path.exists(readme):
    size = os.path.getsize(readme)
    mtime = os.path.getmtime(readme)
    print(f"{readme} size:", size, "bytes")
    print("Last modified:", datetime.datetime.fromtimestamp(mtime))
else:
    print(f"{readme} not found.")
