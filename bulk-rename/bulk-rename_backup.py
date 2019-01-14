#!/usr/bin/python
import argparse
import os
import logging
import string
import random
from colorama import init
import sys
from termcolor import cprint
from pyfiglet import figlet_format


init(autoreset=True)

logging.basicConfig(level=logging.NOTSET, format="%(asctime)s: [%(levelname)s]: %(message)s")

init(strip=not sys.stdout.isatty())

fig_font = ['3-d', '3x5', '5lineoblique', 'acrobatic', 'alligator', 'alligator2', 'alphabet', 'avatar', 'banner',
            'banner3-D', 'banner3', 'banner4', 'barbwire', 'basic', 'bell', 'big', 'bigchief', 'block',
            'bubble', 'bulbhead', 'calgphy2', 'caligraphy', 'catwalk', 'chunky', 'colossal', 'computer',
            'contessa', 'contrast', 'cosmic', 'cosmike', 'cricket', 'cursive', 'cyberlarge', 'cybermedium',
            'cybersmall', 'diamond', 'digital', 'doh', 'doom', 'dotmatrix', 'drpepper', 'eftichess', 'eftifont',
            'eftipiti', 'eftirobot', 'eftitalic', 'eftiwall', 'eftiwater', 'epic', 'fender', 'fourtops', 'fuzzy',
            'gothic', 'graffiti', 'invita', 'isometric2', 'isometric3',
            'isometric4', 'italic', 'ivrit', 'jazmine', 'jerusalem', 'kban', 'larry3d', 'lcd', 'lean',
            'letters', 'linux', 'lockergnome', 'madrid', 'marquee', 'maxfour', 'mini', 'mirror', 'mnemonic',
            'moscow', 'nancyj-fancy', 'nancyj-underlined', 'nancyj', 'ntgreek', 'ogre',
            'pawp', 'peaks', 'pebbles', 'pepper', 'poison', 'puffy', 'pyramid', 'rectangles',
            'rev', 'roman', 'rounded', 'rowancap', 'runic', 'runyc', 'sblood', 'script', 'serifcap',
            'shadow', 'short', 'slant', 'slide', 'slscript', 'small', 'smisome1', 'smkeyboard', 'smscript',
            'smshadow', 'smslant', 'smtengwar', 'speed', 'stampatello', 'standard', 'starwars', 'stellar', 'stop',
            'straight', 'tanja', 'term', 'thick', 'thin', 'threepoint', 'ticks', 'ticksslant',
            'tinker-toy', 'tombstone', 'trek', 'tsalagi', 'twopoint', 'univers', 'usaflag', 'wavy', 'weird']

ran_font = random.choice(fig_font)
cprint(figlet_format("bulk-rename", font=ran_font), 'red', attrs=['bold'])
print("[!] " + ran_font)
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


def rename_all_files(random_rename):
    for new_name, file_name in random_rename.items():
        os.rename(file_name, new_name)
    logging.info("Rename done!")
    exit(0)


if args.directory:
    dir_path = args.directory
    if os.path.isdir(dir_path):
        logging.info("{}".format(dir_path))
        total_file = [i for i in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, i))]
        logging.info("total files: {}".format(len(total_file)))
        total_dirs = [i for i in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, i))]
        logging.info("total directoris: {}".format(len(total_dirs)))
        random_rename = {}
        extentions = []
        for i in total_file:
            extentions.append(i.split(".")[1])
            random_rename.update({
                os.path.join(dir_path, "{}.{}".format(id_generator(), i.split(".")[1])): os.path.join(dir_path, i)
            })
        logging.info("total file format: {}".format(len(set(extentions))))
        for i in set(extentions):
            logging.info("{} file count: {}".format(i, extentions.count(i)))
        choice = raw_input("\n1. Rename all files with random name: ")
        if choice == "1":
            rename_all_files(random_rename)
    else:
        logging.error("{} not found".format(dir_path))
