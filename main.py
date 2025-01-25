"""Main module for testing."""

from cli_manage_db import cli


if __name__ == "__main__":
    try:
        cli()
    except ValueError as e:
        print(e)
