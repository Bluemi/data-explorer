#!/usr/bin/env python3

from pathlib import Path
from argparse import ArgumentParser

import pandas as pd

from window import Window


def parse_args():
    parser = ArgumentParser(description='Visualize data from csv file')
    parser.add_argument('input_file', type=Path, help='The file to visualize')

    return parser.parse_args()


def main():
    args = parse_args()
    df = pd.read_csv(args.input_file)

    window = Window()
    print(window)


if __name__ == '__main__':
    main()

