from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Task():
    title: str
    tag: Optional[str]
    content: Optional[str]
    creation_date: datetime
