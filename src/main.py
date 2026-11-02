"""Entry point for the Group Meeting Scheduler application.

Run this file to test your schedule matching logic or interact with sample data.
"""

from datetime import time
from models import Member, TimeSlot
from scheduler import MeetingScheduler
from utils import format_slot


def create_sample_data():
    """Create a sample group of members with conflicting schedules.

    HINT:
    - Instantiate 2 to 3 Member objects.
    - Add busy blocks for a day (e.g. 'Monday') to test your scheduler logic:
      * Member 1: busy 09:00 - 10:30, 13:00 - 14:00
      * Member 2: busy 10:00 - 11:30, 15:00 - 16:30
      * Member 3: busy 12:00 - 13:30
    """
    pass


def main():
    """Main CLI routine.

    HINT:
    - 1. Initialize `MeetingScheduler`.
    - 2. Load or construct sample members (or prompt for user input).
    - 3. Define target day (e.g., 'Monday') and desired meeting duration (e.g., 60 minutes).
    - 4. Call `scheduler.find_group_meeting_slots(members, day, duration)`.
    - 5. Print out the found slots using `format_slot`.
    """
    print("=== Group Meeting Scheduler ===")
    # TODO: Call your scheduler logic and display the available meeting windows.


if __name__ == "__main__":
    main()