import os

providers = [
    "AWS",
    "Azure",
    "GCP"
]

files = [
    "main.tf",
    "variables.tf",
    "outputs.tf",
    "main.tfvars"
]

general_folder = [
    "terraform-state"
]

modules_folder =[
    "vpc",
    "cluster",
    "instance"
]

modules_files = [
    "main.tf",
    "variables.tf",
    "outputs.tf",
]

def modules():
    os.mkdir("modules")
    os.chdir("modules")
    for folder in modules_folder:
        os.mkdir(folder)
        os.chdir(folder)
        for file in modules_files:
            open(file, "w+")
        os.chdir("..")
    os.chdir("..")

