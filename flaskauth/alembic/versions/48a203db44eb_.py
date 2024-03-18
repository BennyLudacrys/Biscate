"""empty message

Revision ID: 48a203db44eb
Revises: a52e7753b596
Create Date: 2024-02-08 11:41:31.311668

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48a203db44eb'
down_revision = 'a52e7753b596'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('refresh_tokens',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('token', sa.String(length=200), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('expired_at', sa.DateTime(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('refresh_tokens')
    # ### end Alembic commands ###
