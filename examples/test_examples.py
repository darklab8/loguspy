import unittest
from logus import get_logger
import logus
from . import app_logus
from . import app_types
from logus.utils import Loggers, LibName, LogLevel
import logging

logger = get_logger(__name__)


class TestExamples(unittest.TestCase):

    def setUp(self) -> None:
        Loggers(
            root_log_level=logging.DEBUG,
            log_levels={
                LibName("examples"): LogLevel(logging.DEBUG),
            }, 
            add_time=True,
        ).configure()

    def test_basic(self) -> None:
        logger.warn("Writing something", app_logus.TaskID(app_types.TaskID(123)))

    def test_another_one(self) -> None:
        task = app_types.Task(smth="abc", b=4)
        logger.warn("Writing something", app_logus.Task(task))

    def test_with_fields(self) -> None:

        logger2 = logger.with_fields(app_logus.Task(app_types.Task(smth="aaa", b=1)))
        logger3 = logger.with_fields(logus.String("smth", "asd"), logus.Int("number", 2))

        logger.info("logger printed")
        logger2.info("logger2 printed")
        logger3.info("logger3 printed")
