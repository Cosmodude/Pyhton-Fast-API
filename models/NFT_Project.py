import os
import asyncio
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, String, Text, ForeignKey, BigInteger, Boolean, DECIMAL,TIMESTAMP,Integer,DATETIME
from db.db_conf import Base
from sqlalchemy.dialects.mysql import INTEGER

class Project(Base):

    __tablename__ = 'NFT_PR'

    id = Column("id",Integer, primary_key=True, index=True)
    name = Column("project_name",String(30), nullable=False)
    image= Column("image_URL",String(100))
    buy_token_name=Column("buy_token_name",String(5) )
    chain_name=Column("chain_name",String(30))
    floor_price=Column("floor_price_BT",DECIMAL )
    buy_token_price=Column("BT_price",DECIMAL)
    earn_token_name=Column("earn_token_name",String(5))
    earn_token_price=Column("ET_price",DECIMAL)
    last_updated=Column("last_updated",DATETIME)
    earn_rate_ET=Column("earn_rate_ET",DECIMAL)
    contract_address=Column("contract_address",String(100))



    def __repr__(self):
        return f'{self.id}: {self.name}: floor price={self.floor_price}'
        