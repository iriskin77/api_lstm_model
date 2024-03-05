from tortoise import models
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator


class FileToUpload(models.Model):
    id = fields.IntField(pk=True, unique=True)
    filename = fields.CharField(max_length=255)
    column = fields.CharField(max_length=255)
    file = fields.CharField(max_length=10000)
    is_processed = fields.BooleanField(default=False)
    processed_at = fields.DatetimeField(default=None)
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.filename


# Test_Pydantic = pydantic_model_creator(Test)
# Test_Pydantic_Response = pydantic_model_creator(Test)

