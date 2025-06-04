BikeShare Data Analysis Project
===============================

Project Description:
--------------------
This project analyzes data from Motivate, a bike-share service provider, for three major US cities: 
- Chicago
- New York City
- Washington, D.C.

The datasets provided include randomly selected trip data for the first six months of 2017. 
The goal is to compute descriptive statistics to uncover bike share usage patterns 
such as the most common times of travel, popular stations and trips, trip durations, 
and information about users.

Dataset Files:
--------------
- chicago.csv
- new_york_city.csv
- washington.csv

Each dataset contains at least the following columns:
- Start Time
- End Time
- Trip Duration
- Start Station
- End Station
- User Type

Additionally, the Chicago and New York City datasets contain:
- Gender
- Birth Year

Functions Created:
------------------

1. load_data(city, month, day)
   - Loads the data for the specified city and filters by month and day if applicable.
   - Converts 'Start Time' to datetime and extracts month, day of week, and hour.

2. time_stats(df)
   - Displays statistics on the most frequent times of travel:
     - Most common month
     - Most common day of week
     - Most common start hour

3. station_stats(df)
   - Displays statistics on the most popular stations and trip:
     - Most commonly used start station
     - Most commonly used end station
     - Most frequent combination of start and end station trip

4. trip_duration_stats(df)
   - Displays statistics on the total and average trip duration:
     - Total travel time
     - Mean (average) travel time

5. user_stats(df)
   - Displays statistics on bikeshare users:
     - Counts of user types
     - Counts of gender (if available)
     - Earliest, most recent, and most common year of birth (if available)

6. main()
   - The main function that:
     - Asks the user for input (city, month, day)
     - Loads the appropriate dataset
     - Calls all the above analysis functions to display results

Resources and References:
--------------------------
- Official Python Documentation:
  https://docs.python.org/3/

- pandas Documentation:
  https://pandas.pydata.org/docs/

- Stack Overflow (for troubleshooting and function clarifications):
  https://stackoverflow.com/

- GeeksforGeeks (for understanding pandas methods like .mode(), .value_counts()):
  https://www.geeksforgeeks.org/

- W3Schools Python Tutorial:
  https://www.w3schools.com/python/

- BikeShare Udacity Project Description (if applicable)

Notes:
------
- The project heavily relies on pandas for data loading and analysis.
- Filtering and grouping operations are used to simplify extracting the requested statistics.
- Basic user input handling is used for city, month, and day filtering options.
- Error checking (e.g., invalid inputs) could be improved for a more robust program.

Author:
Lana Shurhabil Izzat Zaben

Date:
April,26th,2025
