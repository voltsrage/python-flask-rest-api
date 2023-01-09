"""empty message

Revision ID: 14cfd39df9fb
Revises: 562ba912dc22
Create Date: 2023-01-08 23:05:48.366087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14cfd39df9fb'
down_revision = '562ba912dc22'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)

    # ### end Alembic commands ###
