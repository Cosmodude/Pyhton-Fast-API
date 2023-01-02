import os
import asyncio
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, String, Text, DateTime, ForeignKey, Boolean,Integer,Numeric
from db.db_conf import Base


class Projects(Base):

    __tablename__ = 'nft_pr'

    id = Column("id",Integer, primary_key=True, index=True)
    name = Column("project_name",String(30), nullable=False)
    project_image= Column("project_image_url",String(100))
    buy_token_name=Column("buy_token_name",String(5) )
    chain_name=Column("chain_name",String(30))
    floor_price=Column("floor_price_BT",Numeric(10,6) )
    earn_token_name=Column("earn_token_name",String(5))
    last_updated=Column("last_updated",DateTime)
    earn_rate_ET=Column("earn_rate_ET",Numeric(10,6))
    


    def __repr__(self):
        return f'{self.id}: {self.name}: floor price={self.floor_price}'
        

    class Project(Base):

        __tablename__ = 'nft_pr'

        id = Column("id",Integer, primary_key=True, index=True)
        name = Column("project_name",String(30), nullable=False)
        description=Column("project_description",String(1000))
        chain_name=Column("chain_name",String(30))
        earn_token_name=Column("earn_token_name",String(5))
        earn_token_image=Column("earn_token_image",String(100))
        last_updated=Column("last_updated",DateTime)
        twitter=Column("twitter_url",String(100))
        telegram=Column("telegram_url",String(100))
        site=Column("project_site_url",String(100))
        discord=Column("discord_url",String(100))
        project_image=Column("project_image",String(100))
        floor_price=Column("floor_price_BT",Numeric(10,6) )
        earn_rate_ET=Column("earn_rate_ET",Numeric(10,6))

        def __repr__(self):
            return f'{self.id}: {self.name}: floor price={self.site}'
            