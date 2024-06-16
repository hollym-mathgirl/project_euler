import datetime

start_date = datetime.date(1901, 1, 1)
end_date = datetime.date(2000, 12, 31)

sunday_count = 0
current_date = start_date

while current_date <= end_date:
    if current_date.weekday() == 6 and current_date.day == 1:
        sunday_count += 1
    current_date += datetime.timedelta(days=1)

print(sunday_count)
