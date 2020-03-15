from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
import datetime

# from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    job = Column(String)
    team_leader = Column(Integer, ForeignKey('users.id'))
    work_size = Column(Integer)
    collaborators = Column(String)
    start_date = Column(DateTime, default=datetime.datetime.now)
    end_date = Column(DateTime)
    is_finished = Column(Boolean)

    # users = orm.relation("News", back_populates='user')
