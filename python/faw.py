from icalendar import Calendar, Event
from datetime import datetime, timedelta
import pytz

# Define fixtures
fixtures = [
    {
        "title": "Cymru vs Kazakhstan",
        "date": "2025-03-22",
        "time": "19:45",
        "location": "Cardiff City Stadium, Leckwith Rd, Cardiff CF11 8AZ",
    },
    {
        "title": "North Macedonia vs Cymru",
        "date": "2025-03-25",
        "time": "19:45",
        "location": None,
    },
    {
        "title": "Cymru vs Liechtenstein",
        "date": "2025-06-06",
        "time": "19:45",
        "location": "Cardiff City Stadium, Leckwith Rd, Cardiff CF11 8AZ",
    },
    {
        "title": "Belgium vs Cymru",
        "date": "2025-06-09",
        "time": "19:45",
        "location": None,
    },
    {
        "title": "Kazakhstan vs Cymru",
        "date": "2025-09-04",
        "time": "15:00",
        "location": None,
    },
    {
        "title": "Cymru vs Belgium",
        "date": "2025-10-13",
        "time": "19:45",
        "location": "Cardiff City Stadium, Leckwith Rd, Cardiff CF11 8AZ",
    },
    {
        "title": "Cymru vs North Macedonia",
        "date": "2025-11-18",
        "time": "19:45",
        "location": "Cardiff City Stadium, Leckwith Rd, Cardiff CF11 8AZ",
    },
    {
        "title": "Liechtenstein vs Cymru",
        "date": "2025-11-15",
        "time": "17:00",
        "location": None,
    },
]

# Create calendar
cal = Calendar()
cal.add('prodid', '-//Cymru Fixtures//UEFA//EN')
cal.add('version', '2.0')

# Add fixtures to calendar
for fixture in fixtures:
    event = Event()
    fixture_time = datetime.strptime(f"{fixture['date']} {fixture['time']}", "%Y-%m-%d %H:%M")
    event.add('summary', fixture['title'])
    event.add('dtstart', pytz.timezone('Europe/London').localize(fixture_time))
    event.add('dtend', pytz.timezone('Europe/London').localize(fixture_time + timedelta(hours=1, minutes=45)))
    if fixture["location"]:
        event.add('location', fixture["location"])
    cal.add_component(event)

# Save to file
with open("Cymru_Fixtures.ics", 'wb') as f:
    f.write(cal.to_ical())

print("Cymru_Fixtures.ics file has been created.")
