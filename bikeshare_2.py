import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    cities=["","chicago","new york city","washington"]

    months = ['all','January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']

    days=['all','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    print('Hello! Let\'s explore some US bikeshare data!')


    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("Enter city number 1.Chicago,  2.New york city, 3.washington")

    while(True):
        city_no=int(input())
        if(city_no>0 and city_no<4):
            break
        else:
            print("Enter valid input")



    # get user input for month (all, january, february, ... , june)
    print("Enter month number 1.January, 2.February, 3.March, 4.April, 5.May, 6.June, 7.July, 8.August, 9.September, 10.October, 11.November, 12.December  or 0 for all")

    while(True):
        month_no=int(input())
        if((month_no>0 and month_no<13) or month_no==0):
            break
        else:
            print("Enter valid input")



    # get user input for day of week (all, monday, tuesday, ... sunday)
    print(" Enter day number 1.Monday, 2.Tuesday, 3.Wednesday, 4.Thursday, 5.Friday, 6.Saturday, 7.Sunday or 0 for all")

    while(True):
        day_no=int(input())
        if((day_no>0 and day_no<8) or day_no==0):
            break
        else:
            print("Enter valid input")




    print('-'*40)
    return cities[city_no], months[month_no], days[day_no]


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

    df=pd.read_csv(CITY_DATA.get(city))

    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month_name()

    df['day']=df['Start Time'].dt.day_name()

    if(month=="all" and day=="all"):
        df=df

    elif(month=="all"):
        df=df[(df['day']==day)]

    elif(day=="all"):
        df=df[df['month']==month]

    else:
        df=df[(df['month']==month) & (df['day']==day)]
        
    return df

        
        
def display_raw_data(df):
    
    st_loc=0;
    end_loc=5;

    
    flag=input("Do you wish to see first five rows of data   Type-  yes  or no ")

    while(flag=="yes"):
        
        if(flag=="yes"):
            print(df.iloc[st_loc:end_loc])
            st_loc+=5
            end_loc+=5
            flag=input("Do you wish to see next five rows of data   Type-  yes  or no ")
        else:
            break
        
       


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month=df['month'].mode()[0]
    print("The most common month",common_month)


    # display the most common day of week
    common_day=df['day'].mode()[0]
    print("The most common day",common_day)

    # display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    common_hour=df['hour'].mode()[0]
    print("The most common hour",common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station=df['Start Station'].mode()[0]
    print("The most common  start station",common_start_station)


    # display most commonly used end station
    common_end_station_=df['End Station'].mode()[0]
    print("The most common end station",common_end_station_)


    # display most frequent combination of start station and end station trip

    common_start_end_stations = df.groupby(['Start Station'])['End Station'].value_counts().mode
    print('Most common start and end station: ', common_start_end_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    total_time=df["Trip Duration"].sum()

    total_sec=total_time%60
    total_time=int(total_time/60)

    total_min=total_time%60
    total_time=int(total_time/60)

    total_hr=total_time%24
    total_time=int(total_time/24)

    total_days=total_time%30
    total_time=int(total_time/30)

    total_months=total_time%12
    total_time=int(total_time/12)

    total_years=total_time

    print(total_years,"yrs ",total_months,"mn ",total_days,"dys ",total_hr,"hrs ",total_min,"min  ",total_sec,"sec ")



    # display mean travel time

    mean_time=df["Trip Duration"].mean()

    mean_sec=mean_time%60
    mean_time=int(mean_time/60)

    mean_min=mean_time%60
    mean_time=int(mean_time/60)

    mean_hr=mean_time%24
    mean_time=int(mean_time/24)

    mean_days=mean_time%30
    mean_time=int(mean_time/30)

    mean_months=mean_time%12
    mean_time=int(mean_time/12)

    mean_years=mean_time
   

    print(mean_years,"yrs ",mean_months,"mn ",mean_days,"dys ",mean_hr,"hrs ",mean_min,"min  ",mean_sec,"sec ")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    # Display counts of user types
    user_types=df['User Type'].value_counts().to_frame()
    print("no of user types is:",user_types)

    
    try:
        # Display counts of gender
        gender_count=df['Gender'].value_counts().to_frame()
        print("Gender count is:",gender_count)

        # Display earliest, most recent, and most common year of birth
        earliest_yob=df['Birth Year'].min()
        print("Earliest year of birth:",earliest_yob)

        most_recent_yob=df['Birth Year'].max()
        print("Most recent year of birth is:",most_recent_yob)

        most_commom_yob=df['Birth Year'].mode()[0]
        print("Most commom year of birth is:",most_commom_yob)
        
    except:
        print("In wahington there is no gender and date of birth data")

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
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

