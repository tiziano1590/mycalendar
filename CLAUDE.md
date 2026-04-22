# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

```bash
# Install in development mode
pip install -e .

# Run the calendar CLI
mycalendar

# Run a specific test
pytest tests/

# Run linting
ruff check src/
ruff format src/ --check

# Run formatter
ruff format src/
```

## Package Structure

```
mycalendar/
|-- LICENSE
|-- README.md
|-- pyproject.toml
|-- .gitignore
|-- CLAUDE.md
`-- src
    `-- mycalendar
        |-- __init__.py           # Public API (re-exports from utils)
        |-- utils.py              # Core calendar logic and utility functions
        |-- __main__.py           # CLI entry point
        |-- parameters            # Configurable parameters
        |   |-- __init__.py
        |   `-- parameters.py     # Highlight chars, week start, etc.
        `-- notebooks             # Optional Jupyter notebooks
```

## Architecture

### Core Components

1. **`__init__.py`** - Main module containing:
   - `get_calendar()` - Returns a Python Calendar object
   - `format_date_string()` - Formats dates with highlighting
   - `print_current_month()` - Prints calendar with today highlighted
   - `print_cal_with_highlight()` - Alternative formatting

2. **`__main__.py`** - CLI entry point using `python -m mycalendar`

3. **`parameters/parameters.py`** - Configuration constants:
   - `HIGHLIGHT_CHAR` - Character to highlight current day (default: `*`)
   - `WEEK_START` - Day of week for calendar start (0=Monday, 6=Sunday)
   - `FIRST_WEEKDAY` - First week day of month

### Calendar Printing

The package uses Python's built-in `calendar` module as a base and extends it with:
- Date highlighting for current day
- Custom formatting options
- Configurable parameters

## Notes

- The package name `mycalendar` avoids conflict with Python's stdlib `calendar` module
- Use `from mycalendar import ...` to import after installation
- Today's date is automatically highlighted in the calendar output
