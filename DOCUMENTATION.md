
## def get_filters():

Asks user to specify a city, month, and day to analyze.

Returns:
- \`(str) city\` - name of the city to analyze
- \`(str) month\` - name of the month to filter by, or "all" to apply no month filter
- \`(str) day\` - name of the day of week to filter by, or "all" to apply no day filter

## def load_data(city, month, day):

Loads data for the specified city and filters by month and day if applicable.

Args:
- \`(str) city\` - name of the city to analyze
- \`(str) month\` - name of the month to filter by, or "all" to apply no month filter
- \`(str) day\` - name of the day of week to filter by, or "all" to apply no day filter

Returns:
- \`df (DataFrame)\` - Pandas DataFrame containing city data filtered by month and day

## def time_stats(df):

Displays statistics on the most frequent times of travel.

Args:
- \`df (DataFrame)\` - The DataFrame containing the filtered data.

## def station_stats(df):

Displays statistics on the most popular stations and trip.

Args:
- \`df (DataFrame)\` - The DataFrame containing the filtered data.

## def trip_duration_stats(df):

Displays statistics on the total and average trip duration.

Args:
- \`df (DataFrame)\` - The DataFrame containing the filtered data.

## def user_stats(df):

Displays statistics on bikeshare users.

Args:
- \`df (DataFrame)\` - The DataFrame containing the filtered data.

## def categorize_age_groups(df):

Categorizes users into age groups based on birth year.

Args:
- \`df (DataFrame)\` - The DataFrame containing the filtered data.

## def most_common_age_of_users(df):

Displays the most common age of users.

Args:
- \`df (DataFrame)\` - The DataFrame containing the filtered data.
Loads data for the specified city and filters by month and day if applicable.

Args:
- \`(str) city\` - name of the city to analyze
- \`(str) month\` - name of the month to filter by, or "all" to apply no month filter
- \`(str) day\` - name of the day of week to filter by, or "all" to apply no day filter

Returns:

- \`df (DataFrame)\` - Pandas DataFrame containing city data filtered by month and day

 