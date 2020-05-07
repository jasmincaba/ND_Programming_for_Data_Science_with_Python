import time
import pandas as pd
import numpy as np
import sys

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
print ('\nHello! Let\'s explore some US bikeshare data! \n \n')
print ('-'*80)

def get_filters():
    while True:
        cities = ["chicago", "new york city", "washington"]
        print ("We have data for these cities: Chicago, New York City and Washington")
        print ("Please choose one of cities. \n ")
        city_input = input("Please enter city name: ").lower()
        if city_input in cities:
            city = city_input
            break
        else:
            print ("\nWe don't have data for your input")
            print ("Please try again \n")

    months = ['january', 'february', 'march', 'april', 'may', 'june']
    while True:
        print ("\nEnter month (January-June) or select all")
        month_input = input("Please enter month: ").lower()
        if month_input in months:
            month = month_input
            break
        elif month_input == "all":
            month = month_input
            break
        else:
            print ("\nWe don't have data for your input")
            print ("Please try again \n")

    days_of_week = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    while True:
        print("\nEnter day of week or select all")
        day_of_week = input("Please enter day of week: ").lower()
        if day_of_week in days_of_week:
            day=day_of_week
            break
        elif day_of_week == "all":
            day = day_of_week
            break
        else:
            print ("\nWe don't have data for your input")
            print ("Please try again \n")

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

        df = df[df['month'] == month.title()]


    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("\nThe most common month is: ",df.month.mode()[0])

    # TO DO: display the most common day of week
    print("\nThe most common day of week is: ",df.day_of_week.mode()[0])

    # TO DO: display the most common start hour
    print("\nThe most common start hour is: {} o'clock".format(df["Start Time"].dt.hour.mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

     # TO DO: display most commonly used start station
    print('\nMost common start station is ',df["Start Station"].mode()[0] )

    # TO DO: display most commonly used end station
    print('\nMost common end station is ',df["End Station"].mode()[0] )

    # TO DO: display most frequent combination of start station and end station trip
    df["combination"] = df["Start Station"] + "-"+df["End Station"]
    print('\nMost frequent combination of start station and end station trip is ',df["combination"].mode()[0] )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('\nTotal travel time is ',df["Trip Duration"].sum())

    # TO DO: display mean travel time
    print('\nAverage travel time is ',df["Trip Duration"].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

     # TO DO: Display counts of user types
    print('\nNumber of users by Type')
    print(df["User Type"].value_counts())

    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        print('\nNumber of users by Gender')
        print(df["Gender"].value_counts())
    else:
        print("\nNo data for Gender")

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        print("\nEarliest year of birth is {}".format(int(df["Birth Year"].min())))
        print("\nMost recent year is {}".format(int(df["Birth Year"].max())))
        print("\nMost common year is {}".format(df["Birth Year"].mode()[0].astype(int)))
    else:
        print("\nNo data for year of birth")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):

    start = 0
    end = 5
    step = 5

    while True:
        print (df[:][start:end])
        i = input("Would you like to see next 5 rows: (y/n) ")
        if i == "y":
            start += step
            end += step
        else:
            break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)


        print ("\nDisplaying data for {} \n".format(city.title()))
        display_data(df)

        print ("-"*80)
        print ("\nDescriptive statistics are available. Would you like to continue?(y/n)")
        exit = input("Continue: ")
        if exit == "n":
            sys.exit()

        time_stats(df)
        station_stats(df)

        print ("\nTo continue press any key, to exit enter exit")
        cont=input("Continue: ")
        if cont == "exit":
            sys.exit()
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
