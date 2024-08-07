"""Added field for tvshows

Revision ID: 946caa7aef5d
Revises: 31af144e5d13
Create Date: 2024-08-07 22:07:49.763011

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op  # type: ignore

# revision identifiers, used by Alembic.
revision: str = "946caa7aef5d"
down_revision: Union[str, None] = "31af144e5d13"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("films", sa.Column("is_tvshow", sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("films", "is_tvshow")
    # ### end Alembic commands ###
