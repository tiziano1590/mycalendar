"""CLI entry point for the mycalendar package."""

from . import print_current_month


def main():
    """Print the current month's calendar with today's date highlighted."""
    print_current_month()


if __name__ == "__main__":
    main()
