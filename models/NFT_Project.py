import os
import asyncio
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, String, Text, DateTime, ForeignKey, Boolean,Integer,Numeric
from db.db_conf import Base


class Projects(Base):

    __tablename__ = 'nft_pr'

    id = Column("id",Integer, primary_key=True, index=True)
    name = Column("project_name",String(30), nullable=False) #name of the project
    project_image_url= Column("project_image_url",String(100))
    required_token_name=Column("buy_token_name",String(5) )
    chain_name=Column("chain_name",String(30))
    nft_floor_price=Column("floor_price_BT",Numeric(10,6) )
    earn_token_name=Column("earn_token_name",String(5))
    last_updated=Column("last_updated",DateTime)
    daily_earn_rate_ET=Column("earn_rate_ET",Numeric(10,6))
    


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
        webpage=Column("project_site_url",String(100))
        discord=Column("discord_url",String(100))
        project_image=Column("project_image",String(100))
        nft_floor_price=Column("floor_price_BT",Numeric(10,6) )
        daily_earn_rate_ET=Column("earn_rate_ET",Numeric(10,6))
        category=Column("project_category",String(100))
        nft_required=Column("nft_number",Integer)
        project_poster=Column("poster_url",String(100))

        def __repr__(self):
            return f'{self.id}: {self.name}: floor price={self.site}'
            