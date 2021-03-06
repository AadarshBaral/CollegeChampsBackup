"""empty message

Revision ID: 178277ba59e9
Revises: f521d8915c27
Create Date: 2021-08-05 23:08:53.147548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '178277ba59e9'
down_revision = 'f521d8915c27'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('url_slug', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'url_slug')
    # ### end Alembic commands ###
