"""empty message

Revision ID: 84e9a517417d
Revises: 
Create Date: 2024-12-06 17:06:15.294740

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '84e9a517417d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bookmodel')
    op.add_column('usermodel', sa.Column('role', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usermodel', 'role')
    op.create_table('bookmodel',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('isbn', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('author', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['author'], ['usermodel.id'], name='bookmodel_author_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='bookmodel_pkey'),
    sa.UniqueConstraint('isbn', name='bookmodel_isbn_key')
    )
    # ### end Alembic commands ###
