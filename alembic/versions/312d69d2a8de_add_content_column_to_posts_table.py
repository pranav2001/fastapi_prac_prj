"""add content column to posts table

Revision ID: 312d69d2a8de
Revises: 89b7f2402e1c
Create Date: 2022-11-21 14:55:42.507211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '312d69d2a8de'
down_revision = '89b7f2402e1c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts",'content')
    pass
