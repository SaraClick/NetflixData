# PROJECT DEFINITION
# Use Netflix data to analyze the watching time during Covid year (2020) and prior to Covid (2019)
# including some data from years since opening the accounts
# Create an interactive dialogue with user giving the below options (OPTION 1-6)
# The user shall select what they want to know and info shall be printed
# After each call, we shall ask the user if they want to query any further and print options.
# Print message when the user no longer wants to query.
# Each row of reader is a dictionary containing the value for each key (column)
# Example of a row: {'Profile Name': 'Jordi&Sara', 'Start Time': '2014-08-26 16:50:25', 'Duration': '00:22:39', 'Attributes': '', 'Title': 'The Office (U.S.): Season 1: Pilot (Episode 1)', 'Supplemental Video Type': '', 'Device Type': 'PC', 'Bookmark': '00:22:38', 'Latest Bookmark': '00:22:38', 'Country': 'GB (United Kingdom)'}

from ShowAnalysis import *

def options():
    return("OPTION 1: Shows watched by Angela and not by Jordi&Sara. \n"
    "OPTION 2: Shows watched by Jordi&Sara and not by Angela. \n"
    "OPTION 3: Shows both users have watched. \n"
    "OPTION 4: Total watch time by user since beginning. \n"
    "OPTION 5: 2019 vs 2020 Angela. \n"
    "OPTION 6: 2019 vs 2020 Jordi&Sara. \n"
    "OPTION 7: 2019 vs 2020 comparison. \n")


def stop_query():
    print("Do you want to see other options ? ")
    stop_input = input("Respond Y or N: ").upper()
    if stop_input == "Y":
        select_query()
    elif stop_input == "N":
        print("I hope you are happy with the data, continue watching! :)")
    else:
        print("Make sure you respond Y for Yes or N for No")
        stop_query()


def select_query():
    available_opt = ["1","2","3","4","5","6", "7"]
    select_opt = input("Input here the OPTION number: \n")
    if select_opt not in available_opt:
        print("Please ensure you input a number between 1 and 6")
        select_query()
    else:
        if select_opt == "1":
            output = watched_comparison("Angela", "Jordi&Sara")[0]
            print("OPTION 1: Shows watched by Angela and not by Jordi&Sara.")
            for i in range(len(output)):
                print(output[i])
            stop_query()
        elif select_opt == "2":
            output = watched_comparison("Jordi&Sara", "Angela")[0]
            print("OPTION 2: Shows watched by Jordi&Sara and not by Angela.")
            for i in range(len(output)):
                print(output[i])
            stop_query()
        elif select_opt == "3":
            output = watched_comparison("Angela", "Jordi&Sara")[1]
            print("OPTION 3: Shows both users have watched.")
            for i in range(len(output)):
                print(output[i])
            stop_query()
        elif select_opt == "4":
            print("OPTION 4: Total watch time by user since beginning.")
            print("***********************************")
            print("* Angela     → " + str(time_sum(watched_time("Angela"))) + "  *")
            print("* Jordi&Sara → " + str(time_sum(watched_time("Jordi&Sara"))) + "  *")
            print("***********************************\n")
            stop_query()
        elif select_opt == "5":
            print("OPTION 5: 2019 vs 2020 Angela.")
            print("***********************************")
            print("* Angela 2019 → " + str(watch_time_year("Angela", "2019")) + "  *")
            print("* Angela 2020 → " + str(watch_time_year("Angela", "2020")) + " *")
            print("***********************************\n")
            stop_query()
        elif select_opt == "6":
            print("OPTION 6: 2019 vs 2020 Jordi&Sara.")
            print("***************************************")
            print("* Jordi&Sara 2019 → " + str(watch_time_year("Jordi&Sara", "2019")) + "  *")
            print("* Jordi&Sara 2020 → " + str(watch_time_year("Jordi&Sara", "2020")) + "  *")
            print("***************************************\n")
            stop_query()
        elif select_opt == "7":
            print("OPTION 7: 2019 vs 2020 comparison.")
            print("**********************************************************************")
            print("* Usuario            2019                  2020          Incremento  *")
            print("* Angela        "
                  + str(watch_time_year("Angela", "2019"))
                  + "     " + str(watch_time_year("Angela", "2020"))
                  + "     " + str(increase("Angela", "2019", "2020")) + "%" + "      *")
            print("* Jordi&Sara    "
                  + str(watch_time_year("Jordi&Sara", "2019"))
                  + "     " + str(watch_time_year("Jordi&Sara", "2020"))
                  + "      " + str(increase("Jordi&Sara", "2019", "2020")) + "%" + "      *")
            print("**********************************************************************")
            print("\n"
                  "Wohoooooo \n"
                  "ANGELA ES LA CLARA GANADORA \n")
            stop_query()


print("\n"
      "Welcome to the Netflix analysis for the data \n"
      "of Angela and Jordi&Sara. You can retrieve the following data: \n")
print(options())

select_query()
