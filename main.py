"""Wanted to refresh myself on how Python can be used for system utilities"""
import os
import platform
import psutil
import datetime
import argparse
import sys

# create parser
parser = argparse.ArgumentParser()
# Ask for a name for the user before running program
parser.add_argument('--name', type=str, required=True)
args = parser.parse_args()
print("Hi " + args.name)

if args.name == "Seth":
    print("Today's date is: ", datetime.date.today())
    print("Your operating system is: ", os.name)
    print("Python version is: ", platform.python_version())
    print("Your machine is", platform.machine())
    print("Your platform is: ", platform.system())
    print("Your architecture is: ", platform.architecture())
    print("Your cpu times are: ", psutil.cpu_times())
    print("Your disk usage is: ", psutil.disk_usage('/'))
    print("Your boot time is: ", psutil.boot_time())
    print("Python information: ", sys.copyright)
else:
    print("Get lost creep!!")
