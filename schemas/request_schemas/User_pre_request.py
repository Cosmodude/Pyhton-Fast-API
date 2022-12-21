from typing import List, Dict, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from datetime import datetime

class PostUser(BaseModel):
    id: int
    first_name: str
    last_name: str
    email:str
    entry_time: datetime