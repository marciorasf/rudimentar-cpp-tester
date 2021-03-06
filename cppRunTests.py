#!/usr/bin/env python3

import sys
import os
from pathlib import Path
import subprocess


def compile(cpp_file, program_name):
    subprocess.run(["c++", "-o", program_name, cpp_file])


def is_test_files_same_length(input_file, output_file):
    input_lines = count_file_lines(input_file)
    output_lines = count_file_lines(output_file)
    return input_lines == output_lines


def count_file_lines(file_name):
    file = open(file_name, "r")
    num_lines = sum(1 for line in file)
    file.close()
    return num_lines


def run_test(program_name, test_input_file):
    input_file = open(test_input_file, "r")
    result = []

    for line in input_file:
        process = subprocess.run(["/bin/zsh", "-c", "./program", "<<<", "'1 3'"],
                                 stdout=subprocess.PIPE, input=line.rstrip(), encoding='ascii')
        result.append(float(process.stdout.rstrip()))

    input_file.close()
    return result


def check_test(test_result, expected_output_file):
    output_file = open(expected_output_file, "r")
    failed_tests = []

    for index, line in enumerate(output_file, start=0):
        expected_value = float(line.rstrip())
        if(expected_value != test_result[index]):
            message = "Test " + str(index+1) + ": expected(" + str(
                expected_value) + "), found(" + str(test_result[index]) + ")"
            failed_tests.append(message)

    return failed_tests


def print_result(check_result):
    test_qty = len(check_result)
    print(test_qty, "test(s) failed")
    print("--------------------------------------------")
    print("failed tests:")
    for test in check_result:
        print(test)


def remove_program(program_name):
    os.remove(program_name)


def main():
    cpp_file = sys.argv[1]
    program_name = "program"
    test_input_file = "test_input.txt"
    test_expected_output_file = "test_expected_output.txt"

    check_lines = is_test_files_same_length(
        test_input_file, test_expected_output_file)
    if not check_lines:
        print("Failed testing: " + test_input_file + " and " +
              test_expected_output_file + " have different lengths.")
        return

    compile(cpp_file, program_name)

    test_result = run_test(program_name, test_input_file)
    check_result = check_test(test_result, test_expected_output_file)
    print_result(check_result)

    remove_program(program_name)


main()
