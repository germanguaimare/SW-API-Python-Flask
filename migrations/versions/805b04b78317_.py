"""empty message

Revision ID: 805b04b78317
Revises: 4530cb409c0b
Create Date: 2022-02-09 14:35:24.299243

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '805b04b78317'
down_revision = '4530cb409c0b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('favorites', 'charId',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('favorites', 'vehicleId',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('favorites', 'planetId',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('favorites', 'planetId',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('favorites', 'vehicleId',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('favorites', 'charId',
               existing_type=mysql.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
