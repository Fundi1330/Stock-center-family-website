"""empty message

Revision ID: f2b8b56c1414
Revises: 36b328c93986
Create Date: 2023-03-04 21:17:20.629322

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2b8b56c1414'
down_revision = '36b328c93986'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Goods', schema=None) as batch_op:
        batch_op.add_column(sa.Column('datetime', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Goods', schema=None) as batch_op:
        batch_op.drop_column('datetime')

    # ### end Alembic commands ###
