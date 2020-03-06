import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}
cities = ['chicago', 'new york city', 'washington']
months = ['january','february','march','april','may','june','all']
days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
        # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which city would you like data for: Chicago, New York City, or Washington?\n").lower()
        if city in ('chicago','new york city','washington'):
            print("Alright! Lets check in on {} \n".format(city).title())
            break
        else:
            print("Hmmm. Looks like your selection didn't register. Please re-enter the city name of your choice. \
            \nData are available for Chicago, New York City or Washington only.\n")

            # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Would you like to filter the data by month? Data are available from January - June. \
        \nType 'all' if you'd like to view data for all the months \n").lower()
        if month in ('january', 'february', 'march', 'april', 'may', 'june'):
            print("Got it. {} it is!\n".format(month).title())
            break
        elif month == 'all' :
            print ("Inquisitive! Let's check out all the data on hand.\n")
            break
        else:
            print("I'm sorry. Looks like the month you entered didn't register. \
        \nPlease type out the name of the month in its entirety i.e. January, February etc.\n")

      # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Any day of the week in particular you'd like data for?\
              \nEnter the day of the week or type 'all' for all the days.\n").lower()
        if day in ('sunday','monday','tuesday','wednesday','thursday','friday','saturday'):
            print("Sure thing. {} data coming right up.\n".format(day).title())
            break
        elif day == 'all':
            print("Sunday Monday Tuesday Wednesday Thursday Friday Satuurdaaaaay - Chaka Khan\n")
            break
        else:
            print("Please try re-entering the day of the week. That last one didn't register.")

    print('-'*40)
    return city, month, day
#get_filters()

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert start time to date time
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # create new colums for hour, weekday and month from start time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter the month
    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filter the day
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_mode_stat = df['month'].mode()[0]
    print('The most frequently occuring month is {} '.format(month_mode_stat))

    # TO DO: display the most common day of week
    day_mode_stat = df['day_of_week'].mode()[0]
    print('The most frequently occuring day is {} '.format(day_mode_stat))

    # TO DO: display the most common start hour
    hour_mode_stat = df['hour'].mode()[0]
    print('The most frequently occuring hour is {} '.format(hour_mode_stat))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station_mode_stat = df['Start Station'].mode()[0]
    print('Riders most frequenty start at {} station '.format(start_station_mode_stat))
    # TO DO: display most commonly used end station
    end_station_mode_stat = df['End Station'].mode()[0]
    print('Riders most frequenty end at {} station '.format(end_station_mode_stat))

    # TO DO: display most frequent combination of start station and end station trip
    df['station_combo'] = df['Start Station'] +", "+ df['End Station']
    trip_combo = df['station_combo'].mode()[0]
    print('Looks like the most commonly used start and stop station combination is: {}'.format(trip_combo))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_time = df['Trip Duration'].sum()
    print('Cumulative travel time was {} days'.format(total_trip_time/86400))

    # TO DO: display mean travel time
    mean_trip_time = df['Trip Duration'].mean()
    print('The average trip time for your selection is {} minutes'.format(mean_trip_time/60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    type_of_user = df['User Type'].value_counts()
    print('User type count = {}'.format(type_of_user))

    # TO DO: Display earliest, most recent, and most common year of birth
    # TO DO: Display counts of gender
    if city != 'washington':
        gender_of_user = df['Gender'].value_counts()
        print('User gender count = {}'.format(gender_of_user))
    else:
        print('Gender data are not available for Washington')

    if city != 'washington':
        #Show the earliest year of birth
        eldest_person = df['Birth Year'].min()
        print('The earliest birth year on record is {}'.format(eldest_person))

        #Show the recent year of birth
        youngest_person = df['Birth Year'].max()
        print('The latest birth year on record is {}'.format(youngest_person))

        #Show most common year of birth
        birthyear_mode_stat = df['Birth Year'].mode()[0]
        print('Most people were born in the year {}'.format(birthyear_mode_stat))
    else:
        print('Birth year data not available.')
        print('-'*40)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    #See 5 rows of raw data ?

    data = 0
    while True:
        data_response = input('Care to see five rows of data? Type yes or no: ')
        if data_response.lower() == 'yes':
            print(df[data : data+5])
            data += 5
        else:
            break

def main():
    while True:
      city,month,day = get_filters()
      df = load_data(city, month, day)
      time_stats(df)
      station_stats(df)
      trip_duration_stats(df)
      user_stats(df,city)
      raw_data(df)
      restart = input('\nWould you like to restart? Enter yes or no.\n')
      if restart.lower() != 'yes':
        break

if __name__ == "__main__":
	main()
