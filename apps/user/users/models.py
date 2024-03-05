from tortoise import models
from tortoise import fields


class User(models.Model):

    id = fields.IntField(pk=True, unique=True)
    name = fields.CharField(max_length=255, null=True)
    surname = fields.CharField(max_length=255, null=True)
    email = fields.CharField(max_length=255, null=True)
    hashed_password = fields.CharField(max_length=255, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(null=True, default=None)
    is_active = fields.BooleanField(null=True)
    #role = Column(Integer, ForeignKey("role.id"))
    #role_id = relationship("Role")


# class Role(Base):
#
#     __tablename__ = 'role'
#
#     id = Column(Integer, primary_key=True, unique=True)
#     name_role = Column(String)

    #users = relationship("User", back_populates="users")
