import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['jan', 'feb', 'mars', 'april', 'may', 'june', 'all']
days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
   
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try :
            city = input("Please choose city from: chicago, new york city, washington:\n").lower()
            if city in CITY_DATA.keys():
                break
        except:
            continue

    # get user input for month (all, january, february, ... , june)
    while True:
        try :
            month = input("Please choose month from: all, jan, feb, mars, april, may, june:\n").lower()
            if month in months:
                break
        except:
            continue

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try :
            day = input("Please choose day from: all, sun, mon, tue, wed, thu, fri, sat:\n").lower()
            if day in days:
                break
        except:
            continue

    print('-'*40)
    return city, month, day


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
    df['Trip Duration'] = pd.to_numeric(df['Trip Duration'])
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.day_of_week
    df['Hour'] = df['Start Time'].dt.hour
    if months.index(month) != len(months)-1:
        df = df[df['Month'] == months.index(month)+1]
    if days.index(day) != len(days)-1:
        df = df[df['Day'] == days.index(day)]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month is: ", months[int(df['Month'].mode())-1])

    # display the most common day of week
    print("The most common day is: ", days[int(df['Day'].mode())])

    # display the most common start hour
    print("The most common hour is: ", df['Hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most commonly used start station is: ", df['Start Station'].mode()[0])

    # display most commonly used end station
    print("The most commonly used end station is: ", df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    com = df.groupby(['Start Station','End Station']).size().sort_values(ascending=False).index[0]
    print(f"The most frequent combination of start and end stations is '{com[0]}' as start station and '{com[1]}' as end station trip")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print(f"The total travel time is: {round(df['Trip Duration'].sum()/60/60, 2)} hour/s")

    # display mean travel time
    print(f"The average travel time is: {round(df['Trip Duration'].mean()/60/60, 2)} hour/s")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("The counts of user types:")
    print(df['User Type'].value_counts().to_string())

    # Display counts of gender
    if 'Gender' in df:
        print("The counts of gender:")
        print(df['Gender'].value_counts().to_string())

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print("The most common birth year is: ", int(df['Birth Year'].mode()[0]))
        print("The earliest birth year is: ", int(df['Birth Year'].min()))
        print("The most recent birth year is: ", int(df['Birth Year'].max()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def show_data(df):
    i=0
    while True:
        show = input("Would you like to see some raws of data? (yes/no)")
        if show.lower() == 'yes':
            print(df[i:i+5])
            i += 5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()