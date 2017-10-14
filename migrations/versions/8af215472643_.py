"""empty message

Revision ID: 8af215472643
Revises: fddf127bef51
Create Date: 2017-10-14 19:24:18.072359

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8af215472643'
down_revision = 'fddf127bef51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rating',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('stars', sa.Float(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('review', sa.String(), nullable=True),
    sa.Column('doctor_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['doctor_id'], ['doctor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rating')
    # ### end Alembic commands ###
