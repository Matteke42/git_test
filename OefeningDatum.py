# Indien nodig: pip install datetime
import datetime
import sys
# List with days of the week
daysoftheweek = ['Maandag','Dinsdag','Woensdag','Donderdag','Vrijdag','Zaterdag','Zondag']
# Get today's date
today = datetime.date.today()

# Extract the day, month, year, and weekday
todayweekday = today.weekday()
todayday = today.day
todaymonth = today.month
todayyear = today.year

# Print the results
print(f"Datum van vandaag: {todayday}/{todaymonth}/{todayyear}")
print(f"Het is vandaag: {daysoftheweek[todayweekday]}")
print()
print("Geef een datum in.")

# The user must give in a date. Any date between 1 March 1900 and 1 Jan 2100 is allowed
day = int(input("Dag: "))
month = int(input("Maand: "))
year = int(input("Jaar: "))

# TODO: Check dat de datum geldig is en binnen het toegelaten bereik
# Als de datum niet geldig is, print een error message en verlaat het programma

if not 2100 > year >= 1900:
    print("error")
    sys.exit()

if year == 1900:
    if month < 3:
        print("error")
        sys.exit()
    if month == 3 and day in [1,2]:
        print("error")
        sys.exit()
        
# Als de datum juist is:
print(f"De datum die je ingaf: {day}/{month}/{year}")

# Bereken en print het aantal dagen tussen vandaag en en de ingegeven datum. Tip: werk met lijsten want niet alle maanden hebben evenveel dagen ...
def days_since(d, m, y):
    schrikkeljaren = [1904+i*4 for i in range(49)]
    days_in_month = [0,31, 28, 31, 30 ,31, 30, 31, 31 ,30 ,31, 30 ,31]
    year_count = 1900
    month_count = 1
    days= 0
    while True:
        #print(days)
        if  year_count == y:
            if month_count == m:
                days+=d
                return days
            else:
                if month_count == 2 and year_count in schrikkeljaren:
                    days+= days_in_month[month_count]+1
                else:
                    days+= days_in_month[month_count]
                month_count+=1
                
        else:
            if year_count in schrikkeljaren:
                days+=366
            else:
                days+=365
            year_count+=1






schrikkeljaren = [1900+i*4 for i in range(50)]
days_in_month = [31, 28, 31, 30 ,31, 30, 31, 31 ,30 ,31, 30 ,31]

today_days = days_since(todayday,todaymonth,todayyear)
date_days = days_since(day,month,year)
diffirence = abs(today_days-date_days)
print(diffirence)


    


# Bereken welke dag de ingegeven datum is
print((todayweekday+diffirence%7))
if today_days < date_days:
    if todayweekday+diffirence%7 > 6:
        print(daysoftheweek[(todayweekday+diffirence%7)-7])
    else:
        print(daysoftheweek[todayweekday+diffirence%7])
elif today_days > date_days:
    print(daysoftheweek[todayweekday-diffirence%7])
elif today_days == date_days:
    print(daysoftheweek[todayweekday])