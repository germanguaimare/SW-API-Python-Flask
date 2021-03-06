"""empty message

Revision ID: 4530cb409c0b
Revises: 
Create Date: 2022-02-09 14:06:53.610341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4530cb409c0b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('charName', sa.String(length=120), nullable=False),
    sa.Column('charBirthYear', sa.String(length=15), nullable=True),
    sa.Column('charGender', sa.String(length=15), nullable=True),
    sa.Column('charHairColor', sa.String(length=15), nullable=True),
    sa.Column('charEyeColor', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('planetName', sa.String(length=120), nullable=False),
    sa.Column('planetClimate', sa.String(length=15), nullable=False),
    sa.Column('planetDiameter', sa.Integer(), nullable=False),
    sa.Column('planetPopulation', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('email')
    )
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cargoCapacity', sa.Integer(), nullable=False),
    sa.Column('consumables', sa.Integer(), nullable=False),
    sa.Column('costInCredits', sa.Integer(), nullable=False),
    sa.Column('crew', sa.Integer(), nullable=False),
    sa.Column('manufacturer', sa.String(length=30), nullable=False),
    sa.Column('maxSpeed', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=30), nullable=False),
    sa.Column('passengers', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('charId', sa.Integer(), nullable=False),
    sa.Column('vehicleId', sa.Integer(), nullable=False),
    sa.Column('planetId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['charId'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['planetId'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['user.id'], ),
    sa.ForeignKeyConstraint(['vehicleId'], ['vehicles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorites')
    op.drop_table('vehicles')
    op.drop_table('user')
    op.drop_table('planets')
    op.drop_table('characters')
    # ### end Alembic commands ###
