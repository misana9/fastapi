"""added all the columns in the posts table

Revision ID: 64b9c327c639
Revises: e6fae53b91c2
Create Date: 2026-04-06 11:50:48.110550

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '64b9c327c639'
down_revision: Union[str, Sequence[str], None] = 'e6fae53b91c2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",sa.Column(
        "Content",sa.String(),nullable=False))
    op.add_column("posts", sa.Column(
        "published", sa.Boolean(),nullable=False,server_default='TRUE'))
    op.add_column("posts",sa.Column(
        "created_at",sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('now()')
    ))
    pass


def downgrade() -> None:
    op.drop_column("posts","content")
    op.drop_column("posts","published")
    op.drop_column("posts","created_at")
    pass
