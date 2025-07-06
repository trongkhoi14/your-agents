"""add agents table

Revision ID: ecc050d175f6
Revises: ddb279802120
Create Date: 2025-07-06 16:50:19.710492

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ecc050d175f6'
down_revision: Union[str, Sequence[str], None] = 'ddb279802120'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('agents',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('provider', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('category', sa.String(), nullable=False),
    sa.Column('price_tier', sa.Enum('free', 'freemium', 'paid', name='pricetier'), nullable=False),
    sa.Column('website_url', sa.String(), nullable=True),
    sa.Column('demo_url', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_agents_id'), 'agents', ['id'], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f('ix_agents_id'), table_name='agents')
    op.drop_table('agents')