"""
patefon initialization
"""

from flask import Flask


APP = Flask(__name__)

from .routers import (  # pylint: disable=wrong-import-position
    main
)
