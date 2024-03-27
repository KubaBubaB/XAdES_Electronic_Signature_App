import os

import psutil

def check_external_storage():
    partitions = psutil.disk_partitions(all=True)

    for partition in partitions:
        if partition.opts == 'rw,removable':
            return partition.mountpoint

    return None


def find_pem_files(root):
    pems = []
    for dirpath, dirnames, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith(".pem"):
                pems.append(dirpath + "" + filename)

    if len(pems) == 0:
        return None
    return pems