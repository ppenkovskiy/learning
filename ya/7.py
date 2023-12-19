with open('7_input.txt', 'r') as file:
    l = [i.split(' ') for i in file]

l[0][-1] = l[0][-1].rstrip('\n')

for i in range(len(l)):
    for j in range(len(l[i])):
        l[i][j] = int(l[i][j])


def lizard_existence_duration(start_date, end_date):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    seconds_in_minute = 60
    minutes_in_hour = 60
    hours_in_day = 24
    seconds_in_day = seconds_in_minute * minutes_in_hour * hours_in_day

    def calculate_days(year, month, day):
        days = 0
        for y in range(start_date[0], year):
            days += 365
        for m in range(1, month):
            days += days_in_month[m - 1]
        days += day - start_date[2]
        return days

    def calculate_seconds(hour, minute, second):
        return hour * minutes_in_hour * seconds_in_minute + minute * seconds_in_minute + second

    total_days = calculate_days(end_date[0], end_date[1], end_date[2]) - calculate_days(start_date[0], start_date[1],
                                                                                        start_date[2])

    seconds_in_incomplete_day = calculate_seconds(end_date[3], end_date[4], end_date[5]) - calculate_seconds(
        start_date[3], start_date[4], start_date[5])
    if seconds_in_incomplete_day < 0:
        total_days -= 1
        seconds_in_incomplete_day += 24 * 60 * 60

    print(total_days, seconds_in_incomplete_day)


start_date = l[0]
end_date = l[1]

lizard_existence_duration(start_date, end_date)
