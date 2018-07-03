"""empty message

Revision ID: 2306f0ee0b23
Revises: a5c98ff98141
Create Date: 2018-04-16 21:09:46.069285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2306f0ee0b23'
down_revision = 'a5c98ff98141'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag_featureversion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.Column('featureversion_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['featureversion_id'], ['featureversion.id'], ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tag_featureversion_featureversion_id'), 'tag_featureversion', ['featureversion_id'], unique=False)
    op.create_index(op.f('ix_tag_featureversion_tag_id'), 'tag_featureversion', ['tag_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tag_featureversion_tag_id'), table_name='tag_featureversion')
    op.drop_index(op.f('ix_tag_featureversion_featureversion_id'), table_name='tag_featureversion')
    op.drop_table('tag_featureversion')
    # ### end Alembic commands ###
