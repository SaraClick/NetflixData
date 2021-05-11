# Data for Angela analysis OPTIONS 1 to 4

# https://docs.python.org/3/library/csv.html

# Read csv and extract data into lists
import csv
import datetime


with open("ViewingActivity.csv", newline="", encoding="utf-8") as data:
    reader = csv.DictReader(data, delimiter=",")
    user_list = []
    time_list = []
    duration_list = []
    title_list = []
    for row in reader:
        user_list.append(row["Profile Name"])
        time_list.append(row["Start Time"])
        duration_list.append(row["Duration"])
        title_list.append(row["Title"])


# Function to check the shows watched by each user
def shows_watched(user):
    show_titles = []
    for i in range(len(user_list)):
        if user_list[i] == user:
            raw_show = title_list[i]
            # Series shows: retrieve the show name independently of season and chapter
            show_split = raw_show.split(":")[0].title()
            # Clean up dodgy titles from Netflix database with "_" etc
            show = show_split.split("_")[0]
            if show not in show_titles:
                show_titles.append(show)

    return show_titles


# OPTION 1: Shows watched by Angela and not by Jordi&Sara
# OPTION 2: Shows watched by Jordi&Sara and not by Angela
# OPTION 3: Shows both users have watched
# user 1 = user who's watched something the other has not.
# Example → OPTION 1: user1 = Angela & user2 = "Sara&Jordi
def watched_comparison(user1, user2):
    shows_unique = []
    shows_bothwatched = []
    shows_user1 = shows_watched(user1)
    shows_user2 = shows_watched(user2)
    for show in shows_user1:
        if show not in shows_user2:
            if "Trailer" not in show \
                    and "Tráiler" not in show \
                    and "(Trailer)" not in show \
                    and "Season" not in show \
                    and "Temporada" not in show\
                    and "(Temporada)" not in show\
                    and "Teaser" not in show\
                    and "(Teaser)" not in show\
                    and "Clip" not in show\
                    and "Preview" not in show:
                shows_unique.append(show)
        elif show in shows_user2:
            if "Trailer" not in show \
                    and "Tráiler" not in show \
                    and "(Trailer)" not in show \
                    and "Season" not in show \
                    and "Temporada" not in show \
                    and "(Temporada)" not in show \
                    and "Teaser" not in show \
                    and "(Teaser)" not in show \
                    and "Clip" not in show \
                    and "Preview" not in show:
                shows_bothwatched.append(show)
    return sorted(shows_unique), sorted(shows_bothwatched)

# OPTION 1 TEST:
# print(watched_comparison("Angela", "Jordi&Sara")[0])
# OPTION 2 TEST:
# print(watched_comparison("Jordi&Sara", "Angela")[0])
# OPTION 3 TEST:
# print(watched_comparison("Angela", "Jordi&Sara")[1])

# OPTION 4: Total watch time by user in Days, Hours, Minutes.
def time_sum(time_list):
    mysum = datetime.timedelta()
    for i in time_list:
        (h, m, s) = i.split(':')
        d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        mysum += d
    return mysum

def watched_time(user):
    # Create a list for each user watch time
    time_list = []
    for i in range(len(duration_list)):
        if user_list[i] == user:
            time_list.append(duration_list[i])
    return time_list

def time_sum(list_of_times):
    mysum = datetime.timedelta()
    for i in list_of_times:
        (h, m, s) = i.split(':')
        d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        mysum += d
    return mysum

# TEST 1: total hours watched Angela
# print(time_sum(watched_time("Angela")))
# TEST 2: total hours watched Jordi&Sara
# print(time_sum(watched_time("Jordi&Sara")))

# OPTION 5: Total watch time by user in 2019 & 2020
def watch_time_year(user, year):
    year_list = []
    watched_yearly = []
    for i in range(len(time_list)):
        year_raw = time_list[i].split("-")
        year_list.append(year_raw[0])
        if user_list[i] == user:
            if year_list[i] == str(year):
                watched_yearly.append(duration_list[i])
    return time_sum(watched_yearly)

# TEST 1: Total watch time 19-20 for Angela
# print(watch_time_year("Angela", "2019") + watch_time_year("Angela", "2020"))
# TEST 2: Total watch time 19-20 for Jordi&Sara
# print(watch_time_year("Jordi&Sara", "2019") + watch_time_year("Jordi&Sara", "2020"))


# OPTION 6: 2019 vs 2020 Angela watch time & % of increase
# OPTION 7: 2019 vs 2020 Jordi&Sara watch time & % of increase
def increase(user, year1, year2):
    calculation = ((watch_time_year(user, year2) + watch_time_year(user, year1)) / watch_time_year(user, year1))*100
    return int(calculation)

# TEST 1: para user = "Angela"
# Time watched 2019
# print(watch_time_year("Angela", "2019"))
# Time watched 2020
# print(watch_time_year("Angela", "2020"))
# % increase
# print(str(increase("Angela", "2019", "2020")) + "%")
