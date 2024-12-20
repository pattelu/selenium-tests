import pytest
import os
import sys

def main():
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'tests')))

    pytest_args = [
        '--maxfail=1',
        '--disable-warnings',
        '--verbose',
        '-s',
        'tests'
    ]

    pytest.main(pytest_args)

if __name__ == "__main__":
    main()