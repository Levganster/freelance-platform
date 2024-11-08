from core.database import Base
import sqlalchemy as sa

class Users(Base):
    __tablename__ = 'Users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, nullable=False)
    username = sa.Column(sa.String, nullable=False)
    email = sa.Column(sa.String, nullable=False)
    password = sa.Column(sa.String, nullable=False)
    role = sa.Column(sa.String, nullable=False, default="freelancer")
    is_verified = sa.Column(sa.Boolean, default=False)