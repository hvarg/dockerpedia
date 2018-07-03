"""empty message

Revision ID: 1f0ecc72bfb9
Revises: b744c18d06b8
Create Date: 2018-03-20 11:17:03.902924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f0ecc72bfb9'
down_revision = 'b744c18d06b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('layer', sa.Column('parent_name', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('layer', 'parent_name')
    # ### end Alembic commands ###
