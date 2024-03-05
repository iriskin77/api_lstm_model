from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "filetoupload" ALTER COLUMN "is_processed" SET DEFAULT False;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "filetoupload" ALTER COLUMN "is_processed" DROP DEFAULT;"""
