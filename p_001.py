"""
p_001.py | Claus Pagano | Last update: 2022-9-4

Algorithms and Data Structures practice with Python

"""


# ---------------------------------------------------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------------------------------------------------

import os
import datetime


# ---------------------------------------------------------------------------------------------------------------------
# GLOBAL CONSTANTS & VARIABLES
# ---------------------------------------------------------------------------------------------------------------------

# Path of log file to process
LOG_FILE = r'C:\Users\pagan\OneDrive\Desktop\Programming\Projects\Python_Ale\p_001\ctm_add.txt'


# --------------------------------------------------------------------------------------------------
# FUNCTIONS DEFINITION
# --------------------------------------------------------------------------------------------------

def error_data(line, year):
    """Returns error data from log line in ctm_add.txt log files

        Args:
            line (str): log line from ctm_add.txt log files
                It must comply with following structure
                CONDITION:NTCAN-CDC802AMA1-0010 DATE:1209 added
                CONDITION:NTCAN-CDC802AMA2-0130 DATE:0702 added
            year (int): year of log file modification date

        Returns:
            dict: error data attributes: process, step and date
    """

    line = line.rstrip()
    if line.startswith(' CONDITION:NTCAN-') and line.endswith('added'):
        i = line.find('-', 17)
        j = line.find('DATE:', i + 1)
        if i > 17 and j > i + 5:
            return {
                'process': line[17:i],
                'step': line[i+1:i+5],
                'date':  line[j+5:j+7] + '-' + line[j+7:j+9] + '-' + str(year)
                }
    else:
        return None
    


def file_modification_year(file_path):
    """Returns year of modification date of given file

        Args:
            file_path (str): file path of file

        Returns:
            int: year of modification date of file
    """

    return datetime.datetime.fromtimestamp(os.path.getmtime(LOG_FILE)).year


# --------------------------------------------------------------------------------------------------
# MAIN PROCEDURE
# --------------------------------------------------------------------------------------------------

def main():

    # Obtain year of log file modification date
    year = file_modification_year(LOG_FILE)

    # Load file and read lines
    with open(LOG_FILE, 'r') as file:
        for line in file:
            ed = error_data(line, year)
            print(repr(line), ed)

    # Test
    # ed = error_data(' CONDITION:NTCAN-CDC802AMA1-0010 DATE:1209 added')


if __name__ == "__main__":
    main()