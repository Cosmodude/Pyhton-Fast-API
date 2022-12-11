import os
import asyncio
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, String, Text, ForeignKey, BigInteger, Boolean, TIMESTAMP
from db.db_conf import Base
from sqlalchemy.dialects.mysql import INTEGER

class Ping(Base):

    __tablename__ = 'ping'

    id = Column(INTEGER, primary_key=True, index=True)
    text = Column(String(800), nullable=False)

    def __repr__(self):
        return '<Ping %r>' % self.id