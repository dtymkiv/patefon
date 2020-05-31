"""
Test routes
"""

from app import APP


@APP.route('/')
def main():
    """

    :return:
    """

    return "I'm working!"
