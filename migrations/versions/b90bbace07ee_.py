"""empty message

Revision ID: b90bbace07ee
Revises: b37c31c05b9b
Create Date: 2021-07-30 16:00:51.613210

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b90bbace07ee'
down_revision = 'b37c31c05b9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('others1', sa.String(length=20), nullable=True))
    op.add_column('post', sa.Column('others2', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'others2')
    op.drop_column('post', 'others1')
    # ### end Alembic commands ###
