#!/usr/bin/env python3

from gendiff import generate_diff
from gendiff.cli import parse_arguments


def main():
    first_file, second_file, format = parse_arguments()
    diff = generate_diff(first_file, second_file, format)

    print(diff)


if __name__ == '__main__':
    main()
