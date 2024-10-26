from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field


class ServiceAccount(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sa_name_1: str
    sa_name_2: str
    last_update_date: datetime
    expiration_date: datetime
