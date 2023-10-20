birthdays = {
    'Alice': 'Apr 1',
    'Bob': 'Dec 12',
    'Carol': 'Mar 4',
    'Dan': 'Feb 29',
    'Eve': 'Dec 24',
    'Faythe': 'Jan 1',
    'Grace': 'Feb 29',
}

name = input('Enter a name: ')

print(birthdays.get(name, 'Name not found'))
