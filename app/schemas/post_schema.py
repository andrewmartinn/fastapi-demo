from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import datetime

# post status
class PostStatus(str, Enum):
    draft = "draft"
    published = "published"
    archived = "archived"

# post schema
class Post(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str = Field(min_length=3, max_length=150)
    content: str = Field(min_length=3, max_length=500)
    img: str = Field(min_length=3, max_length=150)
    author: str = Field(min_length=3, max_length=150)
    status: PostStatus = PostStatus.draft
    created_at: datetime = Field(default_factory=datetime.now)

# post create 
class PostCreate(BaseModel):
    title: str = Field(min_length=3, max_length=150)
    content: str = Field(min_length=3, max_length=500)
    img: str = Field(min_length=3, max_length=150)
    author: str = Field(min_length=3, max_length=150)
    status: PostStatus = PostStatus.draft

# post update
class PostUpdate(BaseModel):
    title: Optional[str] = Field(default=None, max_length=150)
    content: Optional[str] = Field(default=None, max_length=500)
    img: Optional[str] = Field(default=None, max_length=150)
    author: Optional[str] = Field(default=None, max_length=150)
    status: Optional[PostStatus] = None
    