from abc import ABC, ABCMeta, abstractmethod
from collections.abc import Iterable
from dateutil.parser import parse
from datetime import datetime

class DeadlinedMetaReminder(Iterable):
    def __init__(self, ABCMeta):
        super().__init__()

    @abstractmethod
    def is_due(self):
        pass

class DeadlinedReminder(ABC, Iterable):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def is_due(self):
        pass

class DateReminder(DeadlinedReminder):
    def __init__(self, text, date):
        super().__init__()
        self.date = parse(date, dayfirst=True)
        self.text = text

    def is_due(self):
        return self.date <= datetime.now()

    def __iter__(self):
        return iter([self.text, self.date.isoformat()])