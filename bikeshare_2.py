import time
import pandas as pd


CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

WEEK_DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    print("Hello! Let's explore some US bikeshare data!")
    while True:
        city = input("Enter the city name (chicago, new york city, washington): ").lower().strip()
        if city in CITY_DATA:
            break
        print("Invalid city name. Please enter the correct city name.")

    while True:
        month = input("Enter the month name ('all', 'january', 'february', ...): ").lower().strip()
        if month in MONTHS or month == 'all':
            break
        print("Invalid month name. Please enter the correct month name.")

    while True:
        day = input("Enter the day of week ('all', 'monday', 'tuesday', ...): ").lower().strip()
        if day in WEEK_DAYS or day == 'all':
            break
        print("Invalid day of week. Please enter the correct day of week.")

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        df = df[df['month'] == MONTHS.index(month) + 1]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print(f'Most Common Month : {MONTHS[popular_month - 1].title()}')

    # display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    popular_day = df['day_of_week'].mode()[0]
    print(f'Most Common Day of Week : {popular_day}')

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f'Most Common Start Hour : {popular_hour}\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station:', most_common_start_station)
    print('Count: {} trip(s)'.format(df['Start Station'].value_counts().max()))

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('\nMost Common End Station:', most_common_end_station)
    print('Count: {} trip(s)'.format(df['End Station'].value_counts().max()))

    # display most frequent combination of start station and end station trip
    df['Start End Station'] = df['Start Station'] + ' - to - ' + df['End Station']
    most_common_start_end_station = df['Start End Station'].mode()[0]

    print('\nMost Common Start - End Station:', most_common_start_end_station)
    print('Count: {} trip(s)'.format(df['Start End Station'].value_counts().max()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum() / 86400
    print(f'Total Travel Time: {total_travel_time:.2f} day(s)')

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean() / 60
    print(f'\nMean Travel Time: {mean_travel_time:.2f} minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    try:
        # Display counts of user types
        user_types = df['User Type'].value_counts().to_dict()
        print('User Types:')
        for user_type, count in user_types.items():
            print(f'{user_type.title()}: {count}')
    except KeyError:
        print('User Types: No data available')

    try:
        # Display counts of gender
        genders_counts = df.groupby(['Gender'])['User Type'].count().to_dict()
        print('\nGender Counts:')
        for gender, count in genders_counts.items():
            print(f'{gender.title()}: {count} rent(s)')
    except KeyError:
        print('\nGender Counts: No data available')

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = int(df['Birth Year'].min())
        print('\nEarliest Birth Year:', earliest_birth_year)
    except ValueError:
        print('\nEarliest Birth Year: No data available')
    except KeyError:
        print('\nEarliest Birth Year: No data available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def raw_data(df):
    """Displays raw data at the user's request."""

    print('\nDisplaying raw data...\n')
    start_loc = 0
    end_loc = 5

    while True:
        print(df.iloc[start_loc:end_loc].to_string())
        start_loc += 5
        end_loc += 5

        ask = input('Would you like to see more raw data? Enter yes or no.\n')
        if ask.lower() != 'yes':
            break


def most_common_times_all_cities(month, day):
    """Displays the most common month, day of week, and start hour for all cities."""
    ask = input(
        '\nWould you like to see the most common month, day of week, and start hour for all cities (yes or no)?: ')

    if ask.lower() != 'yes':
        return

    print('\nCalculating The Most Frequent Times of Travel for all cities...\n')
    start_time = time.time()

    for city, filename in CITY_DATA.items():
        df = load_data(city, month, day)
        print('-' * 40)
        print(f'Most Common in {city.title()}')
        time_stats(df)
        most_common_age_of_users(df)
    print("\nMost common times all cities took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def categorize_age_groups(df):
    """Categorizes users into age groups."""

    year_of_data = df['Start Time'].max().year

    try:
        df['Birth Year'] = df['Birth Year'].dropna().astype('int')
        df['Age'] = year_of_data - df['Birth Year']

        bins = [0, 12, 20, 40, float('inf')]
        labels = ['up to 12', '13-20', '21-40', '41 and above']
        df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

    except ValueError:
        print('\nCategorize Age Groups: No data available')
    except KeyError:
        print('\nCategorize Age Groups: No data available')

def most_common_age_of_users(df):
    try:
        categorize_age_groups(df)
        common_age_group = df.groupby(['Age Group'], observed=False)['Birth Year'].value_counts().groupby(['Age Group'], observed=False).sum()
        id_max = common_age_group.idxmax()
        print(common_age_group)
        print(f'\nMost Common Age Group of users: {id_max} age with {common_age_group[id_max]} rent(s)\n')
    except (ValueError, KeyError):
        print('\nMost Common Age: No data available')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        most_common_age_of_users(df)
        most_common_times_all_cities(month, day)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
