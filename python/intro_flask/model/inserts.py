from model.task import Task
from adapter.base import Session, engine, Base

Base.metadata.create_all(engine)
session=Session()

task_1=Task("do laundry")
task_2=Task("go walk with dog")
session.add(task_1)
session.add(task_2)
session.commit()
session.close()