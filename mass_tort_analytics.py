''' This module provides a reusable byline for Mass Tort Analytics. '''

import math
import statistics 

def main(): #function to display byline
	print(byline)
    
company_name: str = "Mass Tort Analytics"
company_intro: str = "Our goal is to help handle your mass tort data analysis needs from intake to settlement"
num_active_cases: int = 5
money_recovered: float = 65.7 #in MM
notable_torts: list = ['3M Earplugs', 'Roundup', 'Benicar']
project_sizes: list = [16000, 225, 2200, 4500, 150, 8000, 600, 2500, 3700, 1100, 900] #all projects, including completed

#Run calculations from information above
max_size = max(project_sizes)
min_size = min(project_sizes)
total_plaintiffs = sum(project_sizes)
total_projects = len(project_sizes)
avg_project = round(statistics.mean(project_sizes))

#Make strings from variable above
active_cases_string = f'There are currently {num_active_cases} mass tort projects we are working on'
money_recovered_string = f"We've helped law firms recover {money_recovered} million dollars for their clients" 
notable_torts_string = f'A few notable cases we have worked on are {notable_torts[0]}, {notable_torts[1]}, and {notable_torts[2]}'
stats_string = f"""We have worked on a total of {total_projects} different mass torts, with projects ranging \nfrom as few as {min_size} plaintiffs to as many as {max_size} plaintiffs, with an \naverage of {avg_project} plaintiffs per project"""


#Are we accepting clients?
is_accepting_cases: bool = True
if is_accepting_cases:
	accepting_cases_string = "We are accepting new cases!"
else:
	accepting_cases_string = "We are not currently accepting new cases, but will be soon!"

byline = f'''
{company_name}
{company_intro}
{accepting_cases_string}
{active_cases_string}
{money_recovered_string}
{notable_torts_string}
{stats_string}
'''

if __name__ == '__main__':
    main()

  

