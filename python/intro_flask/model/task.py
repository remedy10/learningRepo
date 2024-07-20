import string
from sqlalchemy import Column, Integer, String
from adapter.base import Base


class Task(Base):
    __tablename__ = "Tasks"
    id = Column(Integer, primary_key=True)
    task_name = Column(String)

    def __init__(self, taskname:string):
        """
        docstring
        """
        self.task_name = taskname
