n = int(input('Enter the number of vehicles that passed by: '))
print('Enter the speeds of the vehicles: ')
first_speed = int(input())
max_speed = first_speed
min_speed = first_speed

count_slow = 0
if first_speed <= 30:
    count_slow += 1

for i in range(n - 1):
    speed = int(input())
    
    if speed > max_speed:
        max_speed = speed
    if speed < min_speed:
        min_speed = speed
        
    if speed <= 30:
        count_slow += 1

speed_difference = max_speed - min_speed

print(speed_difference)
print(count_slow)