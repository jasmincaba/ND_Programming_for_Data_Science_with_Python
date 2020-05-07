import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
print ('Hello! Let\'s explore some US bikeshare data! \n \n')
print ('-'*30)

def get_filters():
    print ("Hello")
    while True:
        cities = ["chicago", "new york city", "washington"]
        print ("We have data for these cities: Chicago, New York City and Washington")
        print ("Please choose one of cities. \n ")
        city_input = input("Please enter city name: ").lower()
        if city_input in cities:
            city = city_input
            print ("City: ", city)
            break
        else:
            print ("\n We don't have data for your input")
            print (" Please try again \n")

    months = ['january', 'february', 'march', 'april', 'may', 'june']
    while True:
        print ("Enter month (January-June) or select all")
        month_input = input("Please enter month: ").lower()
        if month_input in months:
            month = month_input
            print ("Month: ", month)
            break
        elif month_input == "all":
            month = month_input
            print ("no filter selected")
            break
        else:
            print ("\n We don't have data for your input")
            print (" Please try again \n")

    days_of_week = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    while True:
        print("Enter day of week or select all")
        day_of_week = input("Please enter day of week: ").lower()
        if day_of_week in days_of_week:
            day=day_of_week
            print("Day: ",day_of_week)
            break
        elif day_of_week == "all":
            day = day_of_week
            print("no filter selected")
            break
        else:
            print ("\n We don't have data for your input")
            print (" Please try again \n")

    return city,month,day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])


    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()


    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]


    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month


    # TO DO: display the most common day of week


    # TO DO: display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station


    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
