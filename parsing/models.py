from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import String


class Base(DeclarativeBase):
    pass


class ParsedDataModel(Base):
    __tablename__ = 'parsed_data'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(150))
    url: Mapped[str] = mapped_column()
    xpath: Mapped[str] = mapped_column()
    parsed_data: Mapped[str] = mapped_column()