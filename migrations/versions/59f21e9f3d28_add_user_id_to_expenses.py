"""add user_id to expenses

Revision ID: 59f21e9f3d28
Revises: 4779e9efbade
Create Date: 2025-05-22 20:54:54.548926

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '59f21e9f3d28'
down_revision: Union[str, None] = '4779e9efbade'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('expenses', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key('expense_user_fk', 'expenses', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('expense_user_fk', 'expenses', type_='foreignkey')
    op.drop_column('expenses', 'user_id')
    # ### end Alembic commands ###
