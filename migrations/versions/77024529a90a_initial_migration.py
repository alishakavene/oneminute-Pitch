"""Initial Migration

Revision ID: 77024529a90a
Revises: 74044013bb67
Create Date: 2020-08-05 00:40:38.126033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77024529a90a'
down_revision = '74044013bb67'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    op.drop_column('users', 'password_secure')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###
