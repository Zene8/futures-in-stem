"""Data models for the Group Meeting Scheduler.

This module defines the basic entities used across the application:
- TimeSlot: Represents a time range (start and end).
- DaySchedule: Represents an individual's slots for a single day.
- Member: Represents a participant with their weekly schedule.
"""

from dataclasses import dataclass, field
from datetime import time
from typing import List, Dict


@dataclass
class TimeSlot:
    """Represents a discrete time interval.

    HINT:
    - You can store times as `datetime.time` (e.g., time(9, 30)) or integer minutes
      since midnight (e.g., 9*60 + 30 = 570) to simplify comparisons.
    - Consider adding helper methods/properties:
      * duration_minutes: returns end - start in minutes.
      * overlaps(other): returns True if this slot overlaps another slot.
    """
    
    
    def __init__(self,start : time, end:time):
      self.start = start
      self.end = end
      self.durations_minutes = end - start
      pass

    def overlaps(self, otherTimeslot: Timeslot):
      return (self.end < otherTimeslot.start and self.start < otherTimeslot.end)
    # TODO: Add validation ensuring start < end.
    # TODO: Add method or property to calculate slot duration.


@dataclass
class Member:
    """Represents a person participating in group meetings.

    HINT:
    - `busy_slots` or `available_slots`: Decide whether you want to track
      when this member is BUSY or when they are FREE.
      Standard calendars usually track busy slots and infer free windows.
    - The dictionary keys can be day names: 'Monday', 'Tuesday', ..., 'Sunday'.
    """
    name: str
    schedule: Dict[str, List[TimeSlot]] = field(default_factory=dict)

    # TODO: Add method to register a time slot for a given day (e.g., add_slot(day, slot)).
    # TODO: Add method to retrieve sorted slots for a specific day.


# Test for commit (TW)