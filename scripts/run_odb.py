import sys
import os
from os import listdir
from os.path import isfile, join
import subprocess
from pathlib import Path


mypath = sys.argv[1]
onlyfiles = [(f, join(mypath, f)) for f in listdir(mypath) if isfile(join(mypath, f))]


def run_linux_command(command):
    try:
        # Run the command and capture the output
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Check if the command was successful
        if result.returncode == 0:
            print("Command executed successfully!")
            print("Output:\n", result.stdout)
        else:
            print(f"Command failed with error code {result.returncode}")
            print("Error:\n", result.stderr)

    except Exception as e:
        print(f"An error occurred: {e}")



for f, path in onlyfiles:
    print(f)
    filename_wo_ext = Path(path).with_suffix('').name
    command = 'oss-detect-backdoor {} -f sarifv2 -o {}'.format(path, os.path.join(sys.argv[2], filename_wo_ext))
    #command = 'mal analyze {}'.format(path)
    run_linux_command(command)
