
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

DATABASE_URL = "postgresql+asyncpg://optorder_user:4tMsMLtBbJyGgjRZc1H95Vv6khRHx774@dpg-cvq3929r0fns73ega5e0-a.oregon-postgres.render.com/optorder"

engine = create_async_engine(DATABASE_URL, echo=False)
SessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def get_session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session
