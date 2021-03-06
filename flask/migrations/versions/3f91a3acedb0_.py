"""empty message

Revision ID: 3f91a3acedb0
Revises: 44faadc0f338
Create Date: 2018-02-20 15:07:34.806919

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f91a3acedb0'
down_revision = '44faadc0f338'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'image', ['full_name'])
    op.create_unique_constraint(None, 'tag', ['image_id', 'name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tag', type_='unique')
    op.drop_constraint(None, 'image', type_='unique')
    # ### end Alembic commands ###
