#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import subprocess
import echo


class TestEcho(unittest.TestCase):
    # def setUp(self):
    #     self.parser = echo.create_parser()

    def test_help(self):
        """ Running the program without arguments should show usage. """
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()
        stdout = stdout.decode("utf-8")

        self.assertEquals(stdout, usage)

    def test_upper(self):
        """ Running the program with -u or -upper as an argument."""

        process = subprocess.Popen(
            ["python", "./echo.py", "-u", "hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout = stdout.decode("utf-8")

        self.assertEquals(stdout, 'HELLO\n')
        # args_u = ['hello', '-u']
        # namespace_u = self.parser.parse_args(args_u)
        # args_upper = ['hello', '--upper']
        # namespace_upper = self.parser.parse_args(args_upper)
        # self.assertTrue(namespace_u.upper)
        # self.assertTrue(namespace_upper.upper)

    def test_lower(self):
        """ Running the program with -l or -lower as an argument."""

        process = subprocess.Popen(
            ["python", "./echo.py", "-l", "HELLO"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout = stdout.decode("utf-8")

        self.assertEquals(stdout, 'hello\n')
        # Step 3: Test the -l/--lower option
        # Write a unit test that asserts that lower get stored inside of the namespace returned from parser.parse_args when either "-l" or "--lower" arguments are passed.

        # It should also test that "Hello" gets turned into "hello" when the program is run.
    def test_title(self):
        """ Running the program with -t or -title as an argument."""

        process = subprocess.Popen(
            ["python", "./echo.py", "-t", "hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout = stdout.decode("utf-8")

        self.assertEquals(stdout, 'Hello\n')
        # Step 4: Test the -t/--title option
        # Write a unit test that asserts that title get stored inside of the namespace returned from parser.parse_args when either "-t" or "--title" arguments are passed.

        # It should also test that "hello" gets turned into "Hello" when the program is run.
    def test_all(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "-u", "-l", "-t", "hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout = stdout.decode("utf-8")

        self.assertEquals(stdout, 'Hello\n')

    def test_none(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout = stdout.decode("utf-8")

        self.assertEquals(stdout, 'hello\n')
#         Step 6: Test for when all options are provided
# When a user provides all three options, they should be applied in the order listed in the helpful usage message that Argparse constructs from the argument definitions. Here are a few examples:

# $ python echo.py -tul "heLLo!"
# Hello!
# $ python echo.py -ul "heLLo!"
# hello!
# Note that the order that the options are provided doesn't matter, e.g. '-tul' and '-utl' and '-lut' are all equivalent inputs to Argparse. Only the final text transform result should be printed.


# Step 7: Test for no arguments
# Write a unit test that asserts that when no arguments are given, the program returns the unaltered input text.
if __name__ == '__main__':
    unittest.main()
