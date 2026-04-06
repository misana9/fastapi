"""add users table and appropriate columns

Revision ID: c8eb91454490
Revises: 64b9c327c639
Create Date: 2026-04-06 12:07:42.996377

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c8eb91454490'
down_revision: Union[str, Sequence[str], None] = '64b9c327c639'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("users",
                    sa.Column(
                        "id",sa.Integer(),primary_key=True,nullable=False),
                    sa.Column(
                        "email",sa.String(),nullable=False,unique=True),
                    sa.Column(
                        "created_at",sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text("now()")
                    ))
    
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
