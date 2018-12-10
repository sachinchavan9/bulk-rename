#!/usr/bin/python
import argparse
import os
import logging
import string
import random

logging.basicConfig(level=logging.CRITICAL, format="%(asctime)s: [%(levelname)s]: %(message)s")

BASE_PATH = os.path.abspath(__file__)

parser = argparse.ArgumentParser(
    description='Rename file in bulk from directory'
)

parser.add_argument("-d", "--directory", help="directory path for bulk renameing")
args = parser.parse_args()

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    """
    this will generate random name
    :param size:
    :param chars:
    :return:
    """
    return ''.join(random.choice(chars) for _ in range(size))

def check_confilict(path):
    total_files = os.listdir(path)
    digits = [str(i) for i in range(1, len(total_files)+ 1)]
    for i in total_files:
        logging.warning("Conflict with {} file".format(i))
        if str(i).split(".")[0] in digits:
            os.rename(
                os.path.join(path, i),
                os.path.join(path, "{}.{}".format(id_generator(), i.split(".")[1]))
            )
    logging.info("Conflict resolved")

def rename_all(path):
    check_confilict(path)
    total_files = os.listdir(path)
    for i in range(len(total_files)):
        os.rename(
            os.path.join(path, total_files[i]),
            os.path.join(path, str(i+1) + "." + total_files[i].split(".")[1])
        )
    logging.info("Rename done")


if args.directory:
    dir_path = args.directory
    total_file_count = len(os.listdir(dir_path))
    logging.info("Total {} file found in directory {}".format(total_file_count, dir_path))
    try:
        extentions = [i.split(".")[1] for i in os.listdir(dir_path)]
    except IndexError:
        os.system("tree {}".format(dir_path))
        logging.error("provided directory containt another directory")
        exit(0)
    logging.info(
        "{} different type of file format present in directory {}".format(len(list(set(extentions))), dir_path))
    for i in list(set(extentions)):
        logging.info("{} {} file  found".format(extentions.count(i), i))
    print("\n1 :Spilt in different directory and rename\n2 :Rename all\n")
    choice = raw_input("Press enter your choince default is 2 :")
    if not choice or choice == "2":
        rename_all(dir_path)
    elif choice == "1":
        dir_list = list()
        for i in list(set(extentions)):
            os.makedirs(os.path.join(dir_path, i))
            logging.info("New directory made: {}".format(i))
            dir_list.append(os.path.join(dir_path, i))
            command = "mv {}*.{} {}".format(dir_path,i, os.path.join(dir_path, i))
            os.system(command)
        map(rename_all, dir_list)

    else:
        logging.error("wrong choice")
        exit(0)
