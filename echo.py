#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "???"


import sys
import argparse


def create_parser(args):
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument('-u', '--upper', action='store_true',
                        help='convert text to uppercase')
    parser.add_argument('-l', '--lower', action='store_true',
                        help='convert text to lowercase')
    parser.add_argument('-t', '--title', action='store_true',
                        help='convert text to titlecase')
    parser.add_argument('text', help='text to be manipulated')
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser(args)
    args = parser.parse_args()
    if args.upper:
        args.text = args.text.upper()
    if args.lower:
        args.text = args.text.lower()
    if args.title:
        args.text = args.text.title()
    print(args.text)
    return args.text


if __name__ == '__main__':
    main(sys.argv[1:])
