"""made posts table

Revision ID: e6fae53b91c2
Revises: 
Create Date: 2026-04-06 10:45:45.998139

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e6fae53b91c2'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("posts", sa.Column("id",sa.Integer(), nullable=False,primary_key=True),
                    sa.Column("title",sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
