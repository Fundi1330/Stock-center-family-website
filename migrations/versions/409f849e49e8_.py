"""empty message

Revision ID: 409f849e49e8
Revises: f2b8b56c1414
Create Date: 2023-03-05 09:34:41.818678

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '409f849e49e8'
down_revision = 'f2b8b56c1414'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Goods', schema=None) as batch_op:
        batch_op.add_column(sa.Column('publish_date', sa.DateTime(), nullable=True))
        batch_op.drop_column('datetime')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Goods', schema=None) as batch_op:
        batch_op.add_column(sa.Column('datetime', sa.DATETIME(), nullable=True))
        batch_op.drop_column('publish_date')

    # ### end Alembic commands ###
