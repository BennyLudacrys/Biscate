"""create users table

Revision ID: a52e7753b596
Revises: 
Create Date: 2024-02-08 11:39:56.455195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a52e7753b596'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.BigInteger(), nullable=False),
                    sa.Column('email', sa.String(length=120), nullable=False),
                    sa.Column('password', sa.String(length=200), nullable=True),
                    sa.Column('first_name', sa.String(length=200), nullable=False),
                    sa.Column('last_name', sa.String(length=200), nullable=False),
                    sa.Column('avatar', sa.String(length=250), nullable=True),
                    sa.Column('country_id', sa.Integer(), nullable=True),
                    sa.Column('is_verified', sa.Boolean(), nullable=False),
                    sa.Column('verification_code', sa.String(length=200), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.Column('deleted_at', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['country_id'], ['countries.id'], onupdate='CASCADE', ondelete='SET NULL'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )


def downgrade() -> None:
    op.drop_table('users')
