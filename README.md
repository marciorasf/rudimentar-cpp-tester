# Basic C++ Tester

## Overview
This is a shell script to compile and run tests of cpp programs.
I use them when I'm solving data algorithms problems like the ones from https://www.dailycodingproblem.com/ or https://www.urionlinejudge.com.br/, for example.

The scripts written in python have a nicer approach and displays the result more clearly. So i recommend to use them and delete the shell ones.

```diff
! Currently I'm using ZShell, so maybe some adjusts have are necessary for diferent shells.
```

## Setup
To use these scripts on the terminal from anywhere, the folder that contains them should be on the PATH.

The following instructions are based on my personal preference:

1. Clone this repository on /bin. The files should be on /bin/rudimentar-cpp-tester
1. If you want to run the Python scripts, make sure you have python 3 installed. Run `python3 -V`, it should display the version, if it is installed
1. Add the folder to the  PATH
   1. Open **/.profile** file
   1. At the bottom, add `export PATH=$PATH:/home/user/bin/rudimentar-cpp-tester` (remember to replace **user** with your user)
   1. Now, every time your SO start, it will add the folder to the PATH


## Scripts
The below tutorial uses the python scripts, but it's the same for the shell ones.

### SetupProgramFiles

#### What it does?

It takes **program_name** as argument and create the program folder and files.

#### How to use?
1. Go to the folder where you want to create your program files
1. Enter `cppSetupProgramFiles.py <program_name>`
1. The following folder/files will be created:
   *  /<program_name>
   *  /<program_name>/<program_name>.cpp
   *  /<program_name>/test_input.txt
   *  /<program_name>/test_expected_output.txt


### RunTests

#### What is does?
1. Compiles your cpp
1. Run the test cases on test_input.txt
1. Compare with the expected result on test_expected_output.txt
1. Print the failed tests

#### How to use?
1. Go to the folder where the cpp and test files are located
1. Enter `cppRunTests <cpp_file_name>.cpp` 
1. The results of the tests will be displayed on the terminal
    * There are some error checking on the test_files before running.
