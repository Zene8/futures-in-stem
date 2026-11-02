# Group Meeting Scheduler

A Python application designed to find optimal meeting times for a group of participants based on their individual availability and schedules.

---

## 🎯 Project Overview & Goals

When coordinating a meeting among multiple people (e.g., student project groups, club committees, study groups), finding a free slot that works for everyone can be challenging.

This project aims to:
1. Accept individual schedules or availability slots (days of the week, start and end times).
2. Represent and organize time slots (e.g., using intervals or time blocks).
3. Find common free time intervals across all members (or the maximum subset of members).
4. Rank or suggest the best meeting times based on duration and preferences.

---

## 📂 Project Structure

```text
future-in-stem/
├── README.md               # Project guide and instructions (this file)
├── req.txt                 # Dependencies list
├── src/
│   ├── __init__.py
│   ├── main.py             # Entry point / CLI interface
│   ├── models.py           # Data structures (User, TimeSlot, DaySchedule)
│   ├── scheduler.py        # Core algorithm for finding overlapping/free slots
│   └── utils.py            # Helper functions (time parsing, formatting)
└── tests/
    ├── __init__.py
    └── test_scheduler.py   # Unit test skeletons
```

---

## 🛠️ Step-by-Step Implementation Guide

### Step 1: Define Your Data Models (`src/models.py`)
- **`TimeSlot`**:
  - Represents an interval: `start_time` and `end_time` (e.g. `datetime.time` or minutes from midnight `0..1439`).
  - *Hint:* Decide whether you represent **busy intervals** (times when someone cannot meet) or **free intervals** (times when they can meet). Working with busy intervals and computing free windows is standard calendar logic!
- **`User` / `Member`**:
  - Store a member's name/ID and their schedule mapped by weekday (e.g. `"Monday"`, `"Tuesday"`).

### Step 2: Implement Time Utilities (`src/utils.py`)
- Parse string inputs like `"09:30"` or `"14:00"` into comparable objects (such as `datetime.time` or integers representing total minutes).
- Format intervals back into human-readable strings (e.g. `"09:00 - 10:30"`).

### Step 3: Implement the Scheduling Algorithm (`src/scheduler.py`)
- **Interval Merging / Sorting**:
  - If a user has overlapping busy blocks (e.g., 9:00-10:00 and 9:30-11:00), merge them into `9:00-11:00`.
- **Finding Common Free Windows**:
  - Determine common boundaries (e.g., workday bounds like 09:00 to 18:00).
  - Combine busy blocks from all participants for a specific day.
  - Invert busy blocks to find windows where *nobody* is busy.
  - Filter windows that meet the minimum required meeting duration.

### Step 4: Build the Entry Point / Interface (`src/main.py`)
- Provide a CLI or interactive script to load sample members and run the scheduler.
- (Optional Extension): Expose an API endpoint (FastAPI / Flask) or a graphical/web interface.

### Step 5: Test Your Logic (`tests/test_scheduler.py`)
- Test with simple edge cases:
  - No overlap at all.
  - Full availability.
  - Only one narrow slot matching the exact meeting duration.

---

## 🚀 Getting Started

1. **Activate Virtual Environment** (Windows PowerShell):
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
2. **Install Requirements** (if external libraries are added):
   ```powershell
   pip install -r req.txt
   ```
3. **Run the Application**:
   ```powershell
   python src/main.py
   ```
