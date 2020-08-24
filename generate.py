import shutil
import sys
import os


def request_value(name):
    print(f"Please enter {name}:")
    return input("> ")
    
def logging_copy2(src, dest):
    print(f"Copying {src} to {dest}...")
    shutil.copy2(src, dest)

MDK_DIR = os.path.join(sys.path[0], "mdk")
MOD_MAIN_CLASS = os.path.join(sys.path[0], "GeneratedMod.java")

print("ForgeModGenerator 1.0 Copyright (c) 2020 Tom_The_Geek")
print()
print(f"MDK DIR: {MDK_DIR}")

OUTPUT = request_value("the output directory")
print()
MODID = request_value("the modid")
print()
NAME = request_value("the name of the mod")
print()
DESCRIPTION = request_value("a short description of the mod")
print()
print(f"Generating mod in {OUTPUT}...")
print()
print("Copying files...")
shutil.copytree(MDK_DIR, os.path.join(".", OUTPUT), copy_function=logging_copy2)
java_output_dir = os.path.join(".", OUTPUT, "src", "main", "java", "me", "geek", "tom", MODID)
os.makedirs(java_output_dir)
shutil.copy2(MOD_MAIN_CLASS, java_output_dir)
print("Copying complete!")
print()

REPLACEMENT_FILES = [
    "mods.toml",
    "build.gradle",
    "pack.mcmeta",
    "GeneratedMod.java"
]

REPLACEMENTS = {
    "${modid}": MODID,
    "${displayname}": NAME,
    "${description}": DESCRIPTION
}

def make_replacements(root, filename):
    fname = os.path.join(root, filename)
    with open(fname, "r") as f:
        content = f.read()
    
    for k, v in REPLACEMENTS.items():
        content = content.replace(k, v)
    
    with open(fname, "w") as f:
        f.write(content)

print("Scanning for renames...")
for root, folders, files in os.walk(os.path.join(".", OUTPUT)):
    for filename in files:
        for test in REPLACEMENT_FILES:
            if test in filename:
                print("Replacing tokens in " + os.path.join(root, filename) + "...")
                make_replacements(root, filename)
                break
print("Done!")
