#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import subprocess
import echo


class TestEcho(unittest.TestCase):
    def setUp(self):
        self.parser = echo.create_parser()

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

        args_u = ['hello', '-u']
        namespace_u = self.parser.parse_args(args_u)
        args_upper = ['hello', '--upper']
        namespace_upper = self.parser.parse_args(args_upper)

        self.assertTrue(namespace_u.upper)
        self.assertTrue(namespace_upper.upper)

    def test_lower(self):
        """ Running the program with -l or -lower as an argument."""

        process = subprocess.Popen(
            ["python", "./echo.py", "-l", "HELLO"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout = stdout.decode("utf-8")

        self.assertEquals(stdout, 'hello\n')

        args_l = ['hello', '-l']
        namespace_l = self.parser.parse_args(args_l)
        args_lower = ['hello', '--lower']
        namespace_lower = self.parser.parse_args(args_lower)

        self.assertTrue(namespace_l.lower)
        self.assertTrue(namespace_lower.lower)

    def test_title(self):
        """ Running the program with -t or -title as an argument."""

        process = subprocess.Popen(
            ["python", "./echo.py", "-t", "hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout = stdout.decode("utf-8")

        self.assertEquals(stdout, 'Hello\n')

        args_t = ['hello', '-t']
        namespace_t = self.parser.parse_args(args_t)
        args_text = ['hello', '--title']
        namespace_text = self.parser.parse_args(args_text)

        self.assertTrue(namespace_t.text)
        self.assertTrue(namespace_text.text)

    def test_all(self):
        """ Tests to make sure we get correct output when all arguments
            are given"""
        process = subprocess.Popen(
            ["python", "./echo.py", "-u", "-l", "-t", "hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout = stdout.decode("utf-8")

        self.assertEquals(stdout, 'Hello\n')

    def test_none(self):
        """ Tests to make sure we get correct output when no arguments
            are given"""
        process = subprocess.Popen(
            ["python", "./echo.py", "hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout = stdout.decode("utf-8")

        self.assertEquals(stdout, 'hello\n')


if __name__ == '__main__':
    unittest.main()
