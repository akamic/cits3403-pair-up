"""empty message

Revision ID: f481ab58feae
Revises: 9474f3dc4cf4
Create Date: 2019-05-08 13:53:05.527664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f481ab58feae'
down_revision = '9474f3dc4cf4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('token', sa.String(length=32), nullable=True))
    op.add_column('students', sa.Column('token_expiration', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_students_token'), 'students', ['token'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_students_token'), table_name='students')
    op.drop_column('students', 'token_expiration')
    op.drop_column('students', 'token')
    # ### end Alembic commands ###