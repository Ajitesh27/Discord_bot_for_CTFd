from config import dburl
from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(dburl)
Base = declarative_base()
Session = sessionmaker(bind=engine)
s = Session()

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    description = Column(String)
    files = Column(String)
    flag = Column(String)
    visible = Column(Boolean)

def find_all_task():
    data = s.query(Task).all()
    return data

def find_task(task_id):
    data = s.query(Task).get(task_id)
    return data

def create_task(name, category, description, files, flag):
    task = Task(
        name=name, 
        category=category,
        description=description,
        files=files,
        flag=flag,
        visible=False
        )
    s.add(task)
    s.flush()
    s.refresh(task)
    s.commit()
    return task

def task_exist(name):
    data = s.query(Task).filter_by(name=name).first()
    return False if (data == None) else True

def release_task(task_id):
    data = s.query(Task).get(task_id)
    data.visible = True
    s.commit()

def hide_task(task_id):
    data = s.query(Task).get(task_id)
    data.visible = False
    s.commit()

def delete_task(task_id):
    data = s.query(Task).get(task_id)
    s.delete(data)
    s.commit()

def correct_flag(flag):
    data = s.query(Task).filter_by(flag=flag).first()
    return data

def not_unique_flag(flag):
    data = s.query(Task).filter_by(flag=flag).first()
    return False if (data == None) else True

def find_all_visible_task():
    data = s.query(Task).filter_by(visible=True).all()
    return data

def find_visible_task(name):
    data = s.query(Task).filter_by(visible=True, name=name).first()
    return data

Base.metadata.create_all(engine)