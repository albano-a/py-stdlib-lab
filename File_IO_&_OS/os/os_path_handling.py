"""
Deal with file paths cross-platform.

    os.path.join()

    os.path.abspath(), os.path.relpath()

    os.path.basename(), os.path.dirname()

    os.path.splitext()

    os.path.samefile()
"""
import os

# Joining paths (cross-platform)
path = os.path.join("folder", "subfolder", "file.txt")

# Absolute and relative paths
abs_path = os.path.abspath(path)
rel_path = os.path.relpath(abs_path, start="folder")

# Getting file name and directory
basename = os.path.basename(path)
dirname = os.path.dirname(path)

# Splitting extension
name, ext = os.path.splitext(basename)

# Check if two paths refer to the same file
# same = os.path.samefile(abs_path, os.path.abspath(os.path.join("folder", "subfolder", "file.txt")))

print("Path:", path)
print("Absolute:", abs_path)
print("Relative:", rel_path)
print("Basename:", basename)
print("Dirname:", dirname)
print("Name:", name)
print("Ext:", ext)
# print("Same file?", same)
