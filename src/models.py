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


      def duration(self, otherTimeslot: TimeSlot):
        return (self.end - self.start)
    # TODO: Add validation ensuring start < end.
    # TODO: Add method or property to calculate slot duration.



@dataclass
class Member:
    """Represents a person participating in group meetings."""

    name: str
    schedule: Dict[str, List[TimeSlot]] = field(default_factory=dict)

    def add_slot(self, day: str, slot: TimeSlot) -> None:
        """Add a time slot to a specific day."""
        if day not in self.schedule:
            self.schedule[day] = []

        self.schedule[day].append(slot)

    def get_sorted_slots(self, day: str) -> List[TimeSlot]:
        """Return time slots for a day, sorted by start time."""
        return sorted(
            self.schedule.get(day, []),
            key=lambda slot: slot.start
        )

# Test for commit (TW)