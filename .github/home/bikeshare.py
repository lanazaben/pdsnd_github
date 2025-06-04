import time
import pandas as pd
import numpy as np

# Define city data
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

# Filter data according to how it's specified
def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df

# Popular times of travel
def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    print('Most Common Month:', df['month'].mode()[0])
    print('Most Common Day of Week:', df['day_of_week'].mode()[0])
    print('Most Common Start Hour:', df['hour'].mode()[0])

# Popular station trips
def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    print('Most Common Start Station:', df['Start Station'].mode()[0])
    print('Most Common End Station:', df['End Station'].mode()[0])
    df['Trip'] = df['Start Station'] + " to " + df['End Station']
    print('Most Common Trip:', df['Trip'].mode()[0])

# Trip duration
def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    print('Total Travel Time:', df['Trip Duration'].sum())
    print('Mean Travel Time:', df['Trip Duration'].mean())

# User information
def user_stats(df):
    print('\nCalculating User Stats...\n')
    print('User Type Counts:\n', df['User Type'].value_counts())

    if 'Gender' in df.columns:
        print('\nGender Counts:\n', df['Gender'].value_counts())

    if 'Birth Year' in df.columns:
        print('\nEarliest Year:', int(df['Birth Year'].min()))
        print('Most Recent Year:', int(df['Birth Year'].max()))
        print('Most Common Year:', int(df['Birth Year'].mode()[0]))

# Ask for city
def get_city():
    """Asks the user for a city and validates the input."""
    while True:
        city = input('Please enter a city (Chicago, New York City, Washington): ').strip().lower()
        if city in CITY_DATA:
            return city
        else:
            print("Invalid input. Please enter either Chicago, New York City, or Washington.")

# Ask for month
def get_month():
    """Asks the user for a month and validates the input."""
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input('Please enter a month (January to June) or "all": ').strip().lower()
        if month in months:
            return month
        else:
            print("Invalid input. Please enter a valid month between January and June, or 'all'.")

# Ask for day from user
def get_day():
    """Asks the user for a day of the week and validates the input."""
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input('Please enter a day of the week or "all": ').strip().lower()
        if day in days:
            return day
        else:
            print("Invalid input. Please enter a valid day of the week or 'all'.")

# Display raw data
def display_raw_data(df):
    """Displays raw data in chunks of 5 rows upon user request."""
    row = 0
    while True:
        show_data = input("Would you like to see 5 lines of raw data? Enter yes or no: ").strip().lower()
        if show_data == 'yes':
            print(df.iloc[row:row+5])
            row += 5
            if row >= len(df):
                print("No more data to display.")
                break
        elif show_data == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Main script that will be run
def main():
    """Main function running the bikeshare program."""
    print('Hello! Let\'s explore some US bikeshare data!')

    city = get_city()
    month = get_month()
    day = get_day()

    df = load_data(city, month, day)
    display_raw_data(df)  # updated, so the user can ask every 5 lines
    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)

if __name__ == "__main__":
    main()
