from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "filetoupload" ALTER COLUMN "is_processed" DROP NOT NULL;
        ALTER TABLE "user" ALTER COLUMN "updated_at" DROP NOT NULL;
        ALTER TABLE "user" ALTER COLUMN "is_active" DROP NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" ALTER COLUMN "updated_at" SET NOT NULL;
        ALTER TABLE "user" ALTER COLUMN "is_active" SET NOT NULL;
        ALTER TABLE "filetoupload" ALTER COLUMN "is_processed" SET NOT NULL;"""
