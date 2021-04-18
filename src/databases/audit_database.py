from config import dburl, timeline
from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import datetime

engine = create_engine(dburl)
Base = declarative_base()
Session = sessionmaker(bind=engine)
s = Session()

class Audit(Base):
    __tablename__ = 'audits'
    id = Column(Integer, primary_key=True)
    team_id = Column(Integer)
    task_id = Column(Integer)
    flag = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

def find_all_audit():
    data = s.query(Audit).all()
    return data

def find_audit(audit_id):
    data = s.query(Audit).get(audit_id)
    return data

def create_audit(team_id, task_id, flag):
    audit = Audit(team_id=team_id, task_id=task_id, flag=flag)
    s.add(audit)
    s.commit()

def audit_exist(team_id, task_id):
    data = s.query(Audit).filter_by(team_id=team_id, task_id=task_id).first()
    return False if (data == None) else True

def delete_audit(audit_id):
    data = s.query(Audit).get(audit_id)
    s.delete(data)
    s.commit()

def number_of_solves():
    data = s.query(Audit).filter(Audit.task_id > 0).all()
    return [i.task_id for i in data]

def number_of_solves_team(team_id):
    data=s.query(Audit).filter_by(team_id=team_id).count()
    return data
    

def firstblood(task_id):
    data = s.query(Audit).filter_by(task_id=task_id).order_by(Audit.id).first()
    return data

def audit_before_freeze():
    data = s.query(Audit).filter(Audit.created_at < datetime.datetime.fromtimestamp(timeline.freeze, datetime.timezone.utc)).filter(Audit.task_id > 0).all()
    return data

Base.metadata.create_all(engine)
