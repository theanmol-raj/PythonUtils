import os
from pathlib import Path
import logging
import sys
import argparse
from time import sleep

delay = 0.5


def get_args():
    parser = argparse.ArgumentParser(description="Process key-value arguments")
    parser.add_argument("--name", type=str, required=True, help="Project Name")
    parser.add_argument("--env", type=int, required=True, help="Python version")
    return parser.parse_args()




list_of_files = [
    ".github/workflows/.gitkeep",
    "config/gonfig.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "notebook/trails.ipynb",
    "notebook/eda.ipynb",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/utils.py",
    "src/constants/__init__.py",
    "src/pipeline/__init__.py",
    "src/config/__init__.py",
    "src/config/configuration.py",
    "src/entity/__init__.py",
    "src/providers/__init__.py",
    "src/logging.py",
    "src/exception.py", 
]
def run(project_name ,env):
    os.system('cls')
    sys.stdout.write(" This Script is built by github.com/theanmol-raj : \n")
    for filepath in list_of_files:
        filepath = Path(filepath)
        filedir, filename = os.path.split(filepath)

        if filedir != "":
            os.makedirs(filedir, exist_ok=True)

        
        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath,'w') as f:
                pass
                sys.stdout.write(f"{filename} created : done\n")
                


        
        else:
            sys.stdout.write(f"{filename} is already exists\n")

    sys.stdout.write("Attempting to create an environment ...\n")
    python = env
    try:
        os.system(f'conda create -p venv python=={python} -y')
        sys.stdout.write(f"Created an environment venv with python version : {python}\n")
    except Exception as e:
        sys.stdout.write(f"Unable to create environment , try creating it manually: {python}\n")


if __name__ == "__main__":
    args = get_args()
    project_name = args.name
    
    run(project_name=project_name ,env=args.env)
    sys.stdout.write(" This Script is built by github.com/theanmol-raj : \n")
    
