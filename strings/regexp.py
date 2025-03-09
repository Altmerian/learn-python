import re

# Example usage:
pattern = re.compile(r"\d+")
text = "There are 123 apples and 456 oranges"
numbers = re.findall(pattern, text)  # Returns ['123', '456']
type(numbers)

match = pattern.match(text)  # This will be None since text doesn't start with digits
match = pattern.search(text)  # Returns a match object for '123'


if match:
    match.group()  # Only call group() if match is not None

    # Examples with multiple groups

    # Example 1: Extracting date components
    date_pattern = re.compile(r"(\d{2})/(\d{2})/(\d{4})")
    date_text = "Today's date is 05/23/2024 and tomorrow is 05/24/2024"

    date_match = date_pattern.search(date_text)
    if date_match:
        day = date_match.group(1)  # '05'
        month = date_match.group(2)  # '23'
        year = date_match.group(3)  # '2024'
        full_date = date_match.group(0)  # '05/23/2024'
        print(f"Day: {day}, Month: {month}, Year: {year}")

    # Example 2: Extracting name and email
    contact_pattern = re.compile(
        r"([A-Za-z\s]+)\s<([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})>"
    )
    contact_text = "Contact John Doe <john.doe@example.com> for more information"

    contact_match = contact_pattern.search(contact_text)
    if contact_match:
        name = contact_match.group(1)  # 'John Doe'
        email = contact_match.group(2)  # 'john.doe@example.com'
        print(f"Name: {name}, Email: {email}")

    # Example 3: Finding all matches with groups
    all_dates = date_pattern.findall(date_text)
    # Returns [('05', '23', '2024'), ('05', '24', '2024')]

    # Example 4: Named groups
    named_pattern = re.compile(r"(?P<day>\d{2})/(?P<month>\d{2})/(?P<year>\d{4})")
    named_match = named_pattern.search(date_text)
    if named_match:
        day = named_match.group("day")  # '05'
        month = named_match.group("month")  # '23'
        year = named_match.group("year")  # '2024'
        print(f"Using named groups - Day: {day}, Month: {month}, Year: {year}")
