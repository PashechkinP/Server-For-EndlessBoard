"""empty message

Revision ID: 171815f5f775
Revises: 01035c2f67b6
Create Date: 2024-07-24 18:07:18.786964

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '171815f5f775'
down_revision: Union[str, None] = '01035c2f67b6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userki',
                    sa.Column('userokname', sa.String(), nullable=False),
                    sa.Column('userokpass', sa.String(), nullable=False),
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userki')
    # ### end Alembic commands ###