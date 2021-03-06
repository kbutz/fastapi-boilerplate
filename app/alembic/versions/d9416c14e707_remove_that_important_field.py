"""remove that important field

Revision ID: d9416c14e707
Revises: a3a1f4356e00
Create Date: 2020-04-21 21:08:30.935181

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd9416c14e707'
down_revision = 'a3a1f4356e00'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('api_logs', 'important_field')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('api_logs', sa.Column('important_field', mysql.VARCHAR(length=100), nullable=True))
    # ### end Alembic commands ###
