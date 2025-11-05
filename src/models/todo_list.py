from src.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column

class TodoList(Base):
    __tablename__ = "todo_lists"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column()
    description: Mapped[str | None] = mapped_column(nullable=True)
    completed: Mapped[bool] = mapped_column(default=False)