"""empty message

Revision ID: dbf05fedfa2e
Revises: 55ce4560fb3f
Create Date: 2023-03-03 11:14:40.167230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbf05fedfa2e'
down_revision = '55ce4560fb3f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Goods', schema=None) as batch_op:
        batch_op.alter_column('in_stock',
               existing_type=sa.BOOLEAN(),
               type_=sa.String(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Goods', schema=None) as batch_op:
        batch_op.alter_column('in_stock',
               existing_type=sa.String(),
               type_=sa.BOOLEAN(),
               existing_nullable=True)

    # ### end Alembic commands ###
