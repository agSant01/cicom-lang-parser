from project import main
from .context import project
import pytest

from project import *


def test_method():
    main.main('./tests/test_files/test1.txt')
    assert True
