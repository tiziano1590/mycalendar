"""Calendar package for printing and highlighting calendars."""

from datetime import datetime
from calendar import monthrange, month as calendar_month
from .parameters import HIGHLIGHT_CHAR, WEEK_START, FIRST_WEEKDAY


def get_calendar(year: int = None, month: int = None):
    """Get a calendar object for the specified year/month.

    Args:
        year: Year number (defaults to current year)
        month: Month number 1-12 (defaults to current month)

    Returns:
        A Calendar object
    """
    if year is None:
        year = datetime.now().year
    if month is None:
        month = datetime.now().month
    return calendar_month()


def format_date_string(day: int) -> str:
    """Format a date for display with highlighting.

    Args:
        day: Day of month (0 means no day in month)

    Returns:
        Formatted string with highlighting for current day
    """
    if day == 0:  # 0 means no day in month
        return "  "
    if day == 1:  # Today
        return f"{HIGHLIGHT_CHAR}{day}"
    return f"{day}"


def print_current_month(
    year: int = None,
    month: int = None,
    day: int = None,
    format_type: str = "2"
):
    """Print the calendar for the specified year/month with today highlighted.

    Args:
        year: Year number (defaults to current year)
        month: Month number 1-12 (defaults to current month)
        day: Day of the month to highlight (defaults to current day)
        format_type: '0' for plain, '1' for two columns, '2' for six columns
    """
    if year is None:
        year = datetime.now().year
    if month is None:
        month = datetime.now().month
    if day is None:
        today = datetime.now()
        year = today.year
        month = today.month
        day = today.day
    else:
        # Use provided day as today for highlighting
        today = datetime(year, month, day)

    # Print month header using calendar.month
    cal_output = calendar_month(year, month, w=0, l=0)
    print(cal_output)
    print("-" * 40)
    print(f"Current date: {today.strftime('%B %d, %Y')} (highlighted)")
    print()

    # Print detailed calendar using calendar.month
    print(calendar_month(year, month))
    print()
    print(f"Current date: {today.strftime('%A, %B %d, %Y')}")


def print_cal_with_highlight(year: int, month: int, day: int = 1):
    """Print calendar with current day highlighted.

    Args:
        year: Year number
        month: Month number (1-12)
        day: Day to highlight (defaults to current day)
    """
    title = calendar_month(year, month, w=0, l=0)
    print(title)
    print(calendar_month(year, month))
    print()
    print(f"Current date: {day if day else 1}")
