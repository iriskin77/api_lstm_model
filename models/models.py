from tortoise.models import Model
from tortoise import fields


class File(Model):
    id = fields.IntField(pk=True, unique=True)
    filename = fields.CharField(max_length=255)
    column = fields.CharField(max_length=255)
    file = fields.CharField(max_length=10000)
    is_processed = fields.BooleanField()
    processed_at = fields.DatetimeField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.filename

