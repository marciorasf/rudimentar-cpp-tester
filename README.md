# rudimentar-cpp-tester

## Usage
This is a shell script to compile and run tests of cpp programs.
I use them when I'm solving data algorithms problems like the ones from https://www.dailycodingproblem.com/ or https://www.urionlinejudge.com.br/, for example.
The scripts written in python have a nicer approach and displays the result more clearly.

## Setup
To use these scripts on the terminal from anywhere, the folder that contains them should be on the PATH.
The following instructions are based on my personal preference:

* Currently I'm using ZShell, so maybe some adjusts have are necessary for diferent shells

1. Clone this repository on /bin. The files should be on /bin/rudimentar-cpp-tester.
2. If you want to run the Python scripts, make sure you have python 3 installed. Run **python3 -V**, it should display the version, if it is installed
3. Add this folder to the PATH.
  *  Open the /.profile file
  *  At the bottom, add "export PATH=$PATH:/home/<user>/bin/rudimentar-cpp-tester" (Remember to replace **user** with your user)
  *  Now, every time your SO start, it will add the folder to the PATH


## Scripts
* I'll explain using the python scripts, but it's the same for the shell ones

### SetupProgramFiles

#### What it does?

It takes the program name as argument and create a folder with this name. Inside this folder, it creates a cpp file, the test input file and the test expected output file

#### How to use?
1. Go to the parent folder where you want to create your program files
2. Enter **cppSetupProgramFiles.py <program_name>**. The following folder/files will be created:
  *  /<program_name>
  *  /<program_name>/<program_name>.cpp
  *  /<program_name>/test_input.txt
  *  /<program_name>/test_expected_output.txt

### RunTests

#### What is does?

* Compiles your cpp
* Run the test cases on test_input.txt
* Compare with the expected result on test_expected_output.txt
* Print the failed tests

#### How to use?
* Go to the folder where your cpp and test files are
* Enter *cppRunTests <cpp_file_name>.cpp* 
* The results of the tests will be displayed on the terminal
  *  There are some error checking on the test_files before running. If an error occurs it will display on terminal what is wrong