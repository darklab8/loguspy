import unittest
from logus import get_logger
from . import app_logus
from . import app_types

logger = get_logger(__name__)


class TestExamples(unittest.TestCase):
    def test_basic(self):
        logger.warn("Writing something", app_logus.TaskID(123))

    def test_another_one(self):
        task = app_types.Task(smth="abc", b=4)
        logger.warn("Writing something", app_logus.Task(task))
