"""Utility functions for calendar formatting and display."""

from datetime import datetime
from calendar import month as calendar_month


def get_calendar(year: int = None, month: int = None):
    """Get a calendar object for the specified year/month.

    Args:
        year: Year number (defaults to current year)
        month: Month number 1-12 (defaults to current month)

    Returns:
        A Calendar object
    """
    from .parameters import WEEK_START
    from calendar import Calendar

    if year is None:
        year = datetime.now().year
    if month is None:
        month = datetime.now().month
    return Calendar()


def format_date_string(day: int, highlight_char: str = None) -> str:
    """Format a date for display with highlighting.

    Args:
        day: Day of month (0 means no day in month)
        highlight_char: Character to use for highlighting (defaults to * or HIGHLIGHT_CHAR)

    Returns:
        Formatted string with highlighting for current day
    """
    if highlight_char is None:
        from .parameters import HIGHLIGHT_CHAR
        highlight_char = HIGHLIGHT_CHAR

    if day == 0:  # 0 means no day in month
        return "  "
    if day == 1:  # Today
        return f"{highlight_char}{day}"
    return f"{day}"


def print_current_month(
    year: int = None,
    month: int = None,
    day: int = None,
    highlight_char: str = None
):
    """Print the calendar for the specified year/month with today highlighted.

    Args:
        year: Year number (defaults to current year)
        month: Month number 1-12 (defaults to current month)
        day: Day of the month to highlight (defaults to current day)
        highlight_char: Character to use for highlighting
    """
    if highlight_char is None:
        from .parameters import HIGHLIGHT_CHAR
        highlight_char = HIGHLIGHT_CHAR

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
    print(f"Current date: {today.strftime('%B %d, %Y')}")
    print()

    # Print detailed calendar using calendar.month
    print(calendar_month(year, month))
    print()
    print(f"Current date: {today.strftime('%A, %B %d, %Y')}")


def print_cal_with_highlight(year: int, month: int, day: int = 1, highlight_char: str = None):
    """Print calendar with current day highlighted.

    Args:
        year: Year number
        month: Month number (1-12)
        day: Day to highlight (defaults to current day)
        highlight_char: Character to use for highlighting
    """
    if highlight_char is None:
        from .parameters import HIGHLIGHT_CHAR
        highlight_char = HIGHLIGHT_CHAR

    title = calendar_month(year, month, w=0, l=0)
    print(title)
    print(calendar_month(year, month))
    print()
    print(f"Current date: {day if day else 1}")
