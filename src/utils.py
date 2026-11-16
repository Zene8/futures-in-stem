"""Helper utilities for time conversion and validation.

Helpful for:
- Parsing strings like "09:30" or "2:00 PM" into datetime.time or integer minutes.
- Formatting minutes or datetime.time into clean display strings.
"""

from datetime import time
from typing import Tuple


def parse_time_str(time_str: str) -> time:
    """Parse a time string into a datetime.time object.

    HINT:
    - Look into `datetime.strptime(time_str, "%H:%M")`.
    - Alternatively, split by ':' and convert hours and minutes to int.
    """
    pass


def time_to_minutes(t: time) -> int:
    """Convert a datetime.time object to the number of minutes from midnight (0..1439).
    
    HINT:
    - Formula: t.hour * 60 + t.minute.
    - Converting to minutes makes interval arithmetic (sorting, finding overlaps, differences)
      very straightforward.
    """

    return t.hour*60 + t.minute    


def minutes_to_time(minutes: int) -> time:
    """Convert total minutes from midnight back into a datetime.time object.

    HINT:
    - hours = minutes // 60
    - mins = minutes % 60
    """
    pass


def format_slot(start: time, end: time) -> str:
    """Format a start and end time into a user-friendly string (e.g. '09:00 - 10:30').

    HINT:
    - Use `strftime("%H:%M")` or f-strings.
    """
    pass
