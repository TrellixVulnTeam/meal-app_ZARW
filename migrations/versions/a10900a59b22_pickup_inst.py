"""pickup-inst

Revision ID: a10900a59b22
Revises: b1d416a5a3c1
Create Date: 2021-02-28 21:43:08.649704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a10900a59b22'
down_revision = 'b1d416a5a3c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('offer', sa.Column('pickup', sa.String(length=140), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('offer', 'pickup')
    # ### end Alembic commands ###