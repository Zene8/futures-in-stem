"""Core scheduling engine for group meetings.

Provides algorithms to:
1. Merge overlapping busy slots for a single or multiple people.
2. Calculate the inverse (free time windows) given daily boundary limits.
3. Find overlapping free intervals across all group members.
"""

from datetime import time
from typing import List
from models import Member, TimeSlot


class MeetingScheduler:
    """Calculates optimal group meeting times given participant schedules."""

    def __init__(self, day_start: time = time(8, 0), day_end: time = time(20, 0)):
        """Initialize scheduler with operating bounds for the day.

        HINT:
        - `day_start` & `day_end` define the earliest and latest possible meeting limits
          (e.g., 08:00 to 20:00).
        """
        self.day_start = day_start
        self.day_end = day_end

    def merge_intervals(self, intervals: List[TimeSlot]) -> List[TimeSlot]:
        """Merge overlapping or consecutive time intervals into unified blocks.

        HINT:
        - Sort the intervals by start time first.
        - Iterate through sorted intervals:
          * If current interval starts before or at the end of the previous one, extend previous end.
          * Otherwise, append current interval as a new separate block.
        """
        pass

    def get_free_slots_for_member(self, member: Member, day: str) -> List[TimeSlot]:
        """Compute the free time windows for a single member on a given day.

        HINT:
        - Take all the member's busy slots for the day.
        - Merge any overlapping busy slots.
        - Look at the gaps between `self.day_start`, the busy blocks, and `self.day_end`.
        - The gaps represent available windows.
        """
        pass

    def find_group_meeting_slots(
        self,
        members: List[Member],
        day: str,
        duration_minutes: int
    ) -> List[TimeSlot]:
        """Find all available slots that work for every member in the list on `day`.

        HINT:
        - Approach A (Intersection of Free Time):
          * Compute free intervals for each member.
          * Intersect free slots pairwise until you have common slots for all members.
        - Approach B (Union of Busy Time):
          * Collect all busy intervals from all members on this day into one big list.
          * Merge all overlapping busy intervals.
          * Invert the merged busy intervals within [day_start, day_end] to get windows where
            NO member is busy.
        - Finally: Filter out any resulting free window that is shorter than `duration_minutes`.
        """
        pass

    def suggest_best_slots(
        self,
        available_slots: List[TimeSlot],
        top_k: int = 3
    ) -> List[TimeSlot]:
        """Rank or pick the best options from available meeting slots.

        HINT:
        - You could prefer slots closest to midday, slots with maximum buffer,
          or slots matching specific preferences.
        """
        pass
