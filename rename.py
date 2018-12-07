#!/usr/bin/python

import argparse
import os
import logging

logging.basicConfig(level=logging.NOTSET, format="%(asctime)s: [%(levelname)s]: %(message)s")

BASE_PATH = os.path.abspath(__file__)

parser = argparse.ArgumentParser(
    description='Rename file in bulk from directory'
)

parser.add_argument("-d", "--directory", help="directory path for bulk renameing")
args = parser.parse_args()


def rename_all(path):
    total_files = os.listdir(path)
    for i in range(len(total_files)):
        os.rename(
            os.path.join(path, total_files[i]),
            os.path.join(path, str(i+1) + "." + total_files[1].split(".")[1])
        )
    logging.info("Rename done")


if args.directory:
    dir_path = args.directory
    total_file_count = len(os.listdir(dir_path))
    logging.info("Total {} file found in directory {}".format(total_file_count, dir_path))
    extentions = [i.split(".")[1] for i in os.listdir(dir_path)]
    logging.info(
        "{} different type of file format present in directory {}".format(len(list(set(extentions))), dir_path))
    for i in list(set(extentions)):
        logging.info("{} {} file  found".format(extentions.count(i), i))
    print("\n1 :Spilt in different directory and rename\n2 :Rename all\n")
    choice = raw_input("Press enter your choince default is 1 :")
    if not choice or choice == "2":
        rename_all(dir_path)
    else:
        print("another choice")
