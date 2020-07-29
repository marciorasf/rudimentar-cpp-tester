#!/usr/bin/env python3

import sys
import os
from pathlib import Path


def createFolder(name):
    if(os.path.isdir(name)):
        print('folder "' + name + '" already exists')
        return

    os.mkdir(name)

    cpp_file = name + "/" + name + ".cpp"
    test_input = name + "/test_input.txt"
    test_expected_output = name + "/test_expected_output.txt"

    Path(cpp_file).touch()
    Path(test_input).touch()
    Path(test_expected_output).touch()


name = sys.argv[1]
createFolder(name)
