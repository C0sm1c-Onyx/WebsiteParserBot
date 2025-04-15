from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import select

from parsing.models import ParsedDataModel
from parsing.config import settings


async_engine = create_async_engine(
    url=settings.database_url_asyncpg,
    echo=True,
)

async_session = async_sessionmaker(async_engine)


async def is_not_exist_xpath_on_db(xpath):
    async with async_session() as session:
        stmt = select(ParsedDataModel).where(
            and_(
                ParsedDataModel.xpath == xpath,
                ParsedDataModel.url == url
            )
        )
        is_exist_xpath = await session.execute(stmt)

        if is_exist_xpath.first():
            return False

        return True


async def save_data_on_db(title, url, xpath, parsed_data):
    if await is_not_exist_xpath_on_db(xpath):
        session = async_session()
        session.add(
            ParsedDataModel(
                title=title,
                url=url,
                xpath=xpath,
                parsed_data=parsed_data
            )
        )

        await session.commit()
