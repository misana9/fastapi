"""added owner_id-foreign key on table post

Revision ID: b90d04000390
Revises: eff77933f222
Create Date: 2026-04-06 12:58:47.407292

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b90d04000390'
down_revision: Union[str, Sequence[str], None] = 'eff77933f222'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",sa.Column(
        "owner_id",sa.Integer(),nullable=False))
    op.create_foreign_key("post_users_fk",source_table="posts",referent_table="users",
                          local_cols=["owner_id"],remote_cols=["id"],ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint("post_user_fk","posts")
    op.drop_column("posts","owner_id")
    pass
