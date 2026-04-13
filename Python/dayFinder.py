def get_day_of_week(d, m, y):
    if m < 3:
        m += 12
        y -= 1
    k = y % 100
    j = y // 100
    h = (d + (13 * (m + 1)) // 5 + k + (k // 4) + (j // 4) + 5 * j) % 7
    days = ["SATURDAY", "SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]
    return days[h]
try:
    day, month, year = map(int, input().split())
    print(get_day_of_week(day, month, year))
except EOFError:
    pass
