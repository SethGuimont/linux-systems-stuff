"""Wanted to refresh myself on how Python can be use for system utilities"""
from tool_usage import *
import argparse

# create parser
parser = argparse.ArgumentParser()
# Ask for a name for the user before running program
parser.add_argument('--name', type=str, required=True)
args = parser.parse_args()
print("Hi " + args.name)

if args.name == "Seth":
    print("Today's date is: ", get_date())
    print("Your operating system is: ", get_os())
    print("Python version is: ", get_python_version())
    print("Your machine is", get_machine())
    print("Your platform is: ", get_system())
    print("Your architecture is: ", get_architecture())
    print("Your cpu times are: ", get_cputimes())
    print("Your disk usage is: ", get_diskusage())
    print("Your boot time is: ", get_boottime())
else:
    print("Get lost creep!!")
