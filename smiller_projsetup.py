'''Start a data analytics project. '''

#Start with imports from the Python Standard Library

import pathlib
import time

#Then, import your own modules

import mass_tort_analytics

#Define your functions here
def create_project_directory(directory_name: str):
    """
    Creates a project sub-directory
    :param directory_name: Name of the directory to be created e.g.:"test"
    """
    pathlib.Path(directory_name).mkdir(exist_ok=True)

def create_folders_for_range(start_year: int, end_year: int):
    """Creates folders from the first year (parameter 1) to the last year (parameter 2)"""
    for i in range(start_year, end_year+1):
        create_project_directory(directory_name = str(start_year))
        start_year+=1

def create_folders_from_list(folder_list, make_lowercase: bool, remove_spaces: bool):
    """Makes folders from a list or names. Makes folders lowercase and removes spaces, if required."""
    if make_lowercase & remove_spaces:          #checks if we was to make lowercase AND remove spaces
        altered_list = [elem.strip().lower().replace(' ', '_') for elem in folder_list]
    elif make_lowercase:                        #if not, checks if we just want to make lowercase
        altered_list = [elem.strip().lower() for elem in folder_list]
    elif remove_spaces:                         #if not, checks if we want to remove spaces
        altered_list = [elem.strip().replace(' ', '_') for elem in folder_list]

    for name in altered_list:
        create_project_directory(directory_name = name)

def create_prefixed_folders(folder_list, prefix):
    """Makes folders from a provided list, and adds the same prefix, provided as parameter 2"""
    for name in folder_list:
        new_name = prefix + '_' + name
        create_project_directory(directory_name = new_name)

def create_folders_periodically(duration):
    """Makes a folder every (duration) amount of seconds"""
    folder_num = 0
    while(True):
        folder_name = 'folder_' + str(folder_num)
        create_project_directory(directory_name = folder_name)
        folder_num+=1
        time.sleep(duration)


#Define your main() function here
def main():
    '''Main function.'''
    print(f"Byline: {mass_tort_analytics.byline}")

    create_folders_for_range(start_year=2018, end_year=2024)

    region_list = ['Asia', 'Europe', 'South America', 'North America']
    create_folders_from_list(folder_list = region_list, make_lowercase = True, remove_spaces = True)

    project_list = ['Valsartan', 'Zantac', 'CPAP']
    create_prefixed_folders(folder_list = project_list, prefix = 'MDL')

    create_folders_periodically(duration=5)

if __name__ == '__main__':
    main()