"""Added user table

Revision ID: 04a1e0a0ac69
Revises: 
Create Date: 2024-07-07 23:51:37.407934

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '04a1e0a0ac69'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('foo', sa.Integer(), nullable=False),
    sa.Column('bar', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('foo', 'bar', name=op.f('uq_users_foo_bar')),
    sa.UniqueConstraint('username', name=op.f('uq_users_username'))
    )


def downgrade() -> None:
    op.drop_table('users')
