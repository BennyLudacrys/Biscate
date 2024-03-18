"""create country table

Revision ID: 360ff74b02ee
Revises: 48a203db44eb
Create Date: 2024-02-08 12:32:17.152603

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '360ff74b02ee'
down_revision = '48a203db44eb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('countries',
                    sa.Column('id', sa.BigInteger(), nullable=False),
                    sa.Column('name', sa.String(length=120), nullable=False),
                    sa.Column('code', sa.String(length=200), nullable=True))


def downgrade() -> None:
    op.drop_table('countries')
