import unittest
from typelog import get_logger
import typelog
from . import logtypes
from . import types
from typelog import Loggers, LogConfig
from typelog.types import LibName, LogLevel, RootLogLevel
import logging

logger = get_logger(__name__)



class TestExamples(unittest.TestCase):

    def setUp(self) -> None:
        Loggers(
            RootLogLevel(logging.DEBUG),
            LogConfig(LibName("examples"), LogLevel(logging.DEBUG)),
            add_time=True,
        ).configure()

    def test_basic(self) -> None:
        logger.warn("Writing something", logtypes.TaskID(types.TaskID(123)))

    def test_another_one(self) -> None:
        task = types.Task(smth="abc", b=4)
        logger.warn("Writing something", logtypes.Task(task))

    def test_with_fields(self) -> None:

        logger2 = logger.with_fields(logtypes.Task(types.Task(smth="aaa", b=1)))
        logger3 = logger.with_fields(typelog.String("smth", "asd"), typelog.Int("number", 2))

        logger.info("logger printed")
        logger2.info("logger2 printed")
        logger3.info("logger3 printed")
