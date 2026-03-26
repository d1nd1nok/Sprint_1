temp_hours = '1h 45m,360s,25m,30m 120s,2h 60s'
list_hours = temp_hours.split(',')

sum_minutes = 0

for hour in list_hours:

    temp = hour.split()

    for item in temp:
        if 'h' in item:
            hours = int(item.replace('h', ''))
            sum_minutes += hours * 60
        if 'm' in item:
            minutes = int(item.replace('m', ''))
            sum_minutes += minutes  
        if 's' in item:
            seconds = int(item.replace('s', ''))
            sum_minutes += seconds / 60

print(f'Total minutes: {sum_minutes}')