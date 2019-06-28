"""empty message

Revision ID: 79c61673a487
Revises: 539d0567cd6c
Create Date: 2019-06-14 09:32:51.540198

"""

# revision identifiers, used by Alembic.
revision = '79c61673a487'
down_revision = '539d0567cd6c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('offer', sa.Column('accepted_accommodation_award', sa.Boolean(), nullable=True))
    op.add_column('offer', sa.Column('accepted_travel_award', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('offer', 'accepted_travel_award')
    op.drop_column('offer', 'accepted_accommodation_award')
    # ### end Alembic commands ###