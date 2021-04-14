from config import dburl
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(dburl)
Base = declarative_base()
Session = sessionmaker(bind=engine)
s = Session()

class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class UserSession(Base):
    __tablename__ = 'user_sessions'
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    team_id = Column(Integer, ForeignKey('teams.id'))

def find_all_team(team_id):
    data = s.query(Team).all()
    return data

def find_team_data(team_id):
    data = s.query(Team).get(team_id)
    return data

def create_team(name):
    team = Team(name=name)
    s.add(team)
    s.flush()
    s.refresh(team)
    s.commit()
    return team

def team_exist(name):
    data = s.query(Team).filter_by(name=name).first()
    return False if (data == None) else True

def create_user_session(user_id, team_id):
    user_session = UserSession(user_id=user_id, team_id=team_id)
    s.add(user_session)
    s.commit()

def find_team(user_id):
    data = s.query(UserSession).filter_by(user_id=user_id).first()
    return data


Base.metadata.create_all(engine)