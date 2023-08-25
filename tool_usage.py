import os
import platform
import psutil
import datetime
from datetime import date


def get_date():
    date_object: date = datetime.date.today()
    return date_object


def get_os():
    operating_system = os.name
    return operating_system


def get_python_version():
    python_version = platform.python_version()
    return python_version


def get_machine():
    machine = platform.machine()
    return machine


def get_system():
    system = platform.system()
    return system


def get_architecture():
    architecture = platform.architecture()
    return architecture


def get_cputimes():
    cpu_times = psutil.cpu_times()
    return cpu_times


def get_diskusage():
    disk_usage = psutil.disk_usage('/')
    return disk_usage


def get_boottime():
    boot_time = psutil.boot_time()
    return boot_time
