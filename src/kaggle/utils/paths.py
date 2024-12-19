"""
The paths (directories) utilities module.
"""
from pathlib import Path


def root_dir() -> Path:
    """Returns the root directory."""
    return Path(__file__).resolve().parent.parent.parent.parent

def data_dir() -> Path:
    """Return the path to the data/ directory."""
    return root_dir() / 'data'

