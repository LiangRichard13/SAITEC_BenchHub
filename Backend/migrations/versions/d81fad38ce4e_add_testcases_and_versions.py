"""Add Testcases and Versions

Revision ID: d81fad38ce4e
Revises: 92100490cb18
Create Date: 2025-01-02 15:39:06.356676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd81fad38ce4e'
down_revision = '92100490cb18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('testcases',
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('data_resource', sa.String(length=50), nullable=False),
    sa.Column('data_type', sa.String(length=50), nullable=False),
    sa.Column('data_dimension', sa.String(length=50), nullable=False),
    sa.Column('path', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('uploader', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('versions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('testcase_id', sa.String(length=32), nullable=False),
    sa.Column('version', sa.String(length=20), nullable=False),
    sa.Column('update_time', sa.DateTime(), nullable=False),
    sa.Column('transform_method', sa.Text(), nullable=True),
    sa.Column('data_type', sa.String(length=50), nullable=False),
    sa.Column('data_dimension', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['testcase_id'], ['testcases.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('versions')
    op.drop_table('testcases')
    # ### end Alembic commands ###