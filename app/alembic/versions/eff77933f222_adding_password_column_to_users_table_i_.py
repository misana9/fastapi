"""adding password column to users table i forgot

Revision ID: eff77933f222
Revises: c8eb91454490
Create Date: 2026-04-06 12:13:45.943361

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eff77933f222'
down_revision: Union[str, Sequence[str], None] = 'c8eb91454490'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users",sa.Column(
        "password",sa.String(),nullable=False
    ))
    pass


def downgrade() -> None:
    op.drop_column("users","password")
    pass
