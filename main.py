from datetime import date

print('Który mamy rok? (np. 2021)')
year = input()

print('Jaki mamy miesiąc? (np. 12)')
month = input()

print('Jaki mamy dzień? (np. 09)')
day = input()

iso_date = date(int(year), int(month), int(day)).isocalendar()[:2]

print('Numer tygodnia zgodznie z ISO: {}'.format(str(iso_date)))
