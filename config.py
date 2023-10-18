from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class Config:
    username: Optional[str] = None
    email: Optional[str] = None


config = Config()
