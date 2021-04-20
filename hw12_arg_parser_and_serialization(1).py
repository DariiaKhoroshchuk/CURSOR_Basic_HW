# In the homework directory you can find the directory arg_parser_homework where you can find 2020_june_mini.csv file.

# 1. Create a script with arguments:
# exp; required: false; default: min(exp)
# current_job_exp; required: false; default: max(current_job_exp)
# sex; required: false
# city; required: false
# position; required: false
# age; required: false
# path_to_source_files; required: true;
# destination_path; required: false; default: .
# destination_filename; required: false; default: f"2020_june_mini.csv".
# The script should read the .csv file and get the information based on your input and generate a new .csv
# file with that info
#
# Example of input:
# -exp 3 -sex female -position DevOps -city Kyiv --path_to_source_files . ...

import argparse

parser = argparse.ArgumentParser(description='The script should read the .csv file '
                                             'and get the information based on your input '
                                             'and generate a new .csv file with that info')  # creating argument parser

# adding arguments(statically indicate that we receive it)
parser.add_argument("--exp", "-e", required=False, default="min(exp)")
parser.add_argument("--current_job_exp", "-c", required=False, default="max(current_job_exp)")
parser.add_argument("--exp", "-e", required=False, default="min(exp)")
parser.add_argument("--exp", "-e", required=False, default="min(exp)")
parser.add_argument("--exp", "-e", required=False, default="min(exp)")
parser.add_argument("--exp", "-e", required=False, default="min(exp)")
parser.add_argument("--exp", "-e", required=False, default="min(exp)")
parser.add_argument("--exp", "-e", required=False, default="min(exp)")

args = parser.parse_args()  # getting arguments from command line



# 2. Create a script with arguments:
#
# source_file_path; required: true;
# start_salary; required: false; help: starting point of salary;
# end_salary; required: false; help: the max point of salary;
# position; required: false; help: position role
# age; required: false; help: Age of person
# language; required: false; help; Programming language
#
# Based on this info generate a new report of average salary.