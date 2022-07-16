"""
Utility methods for pingme.
"""

from datetime import datetime
import os


def current_time() -> str:
    """Returns the current time formatted as a string."""
    return datetime.now().strftime('%X')


def get_environment_variable(key: str) -> str:
    """Returns the environment variable value
    present at the given key. Throws an exception
    if none found."""
    var = os.environ[key]
    if not var:
        raise EnvironmentError(f'The required environment variable: {key}, was not found.')
    return var


def format_string(m: str) -> str:
    """Format a string and replace known placeholders."""
    return '' \
        if m is None or len(m) < 1 \
        else m.replace('%d', current_time())
