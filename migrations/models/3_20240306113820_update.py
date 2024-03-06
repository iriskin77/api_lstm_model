from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "filetoupload" ADD "user_id" INT;
        ALTER TABLE "filetoupload" ADD CONSTRAINT "fk_filetoup_user_b2309f6c" FOREIGN KEY ("user_id") REFERENCES "user" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "filetoupload" DROP CONSTRAINT "fk_filetoup_user_b2309f6c";
        ALTER TABLE "filetoupload" DROP COLUMN "user_id";"""
