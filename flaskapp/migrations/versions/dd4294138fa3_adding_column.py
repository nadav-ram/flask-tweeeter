"""adding column

Revision ID: dd4294138fa3
Revises: deb57260f843
Create Date: 2020-12-02 12:27:07.454162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd4294138fa3'
down_revision = 'deb57260f843'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('sexually_explicit', sa.Float(), nullable=True))
    op.add_column('user', sa.Column('sexually_explicit', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'sexually_explicit')
    op.drop_column('post', 'sexually_explicit')
    # ### end Alembic commands ###
