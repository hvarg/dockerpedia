"""empty message

Revision ID: 8fcba8c805b5
Revises: e68beb9c4255
Create Date: 2018-05-18 20:11:23.606100

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fcba8c805b5'
down_revision = 'e68beb9c4255'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('image', sa.Column('score', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('image', 'score')
    # ### end Alembic commands ###
