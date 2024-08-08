"""user details updated

Revision ID: 6310b6c5b48e
Revises: 1a31ce608336
Create Date: 2024-08-05 10:18:03.029538

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = '6310b6c5b48e'
down_revision = '1a31ce608336'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('item_owner_id_fkey', 'item', type_='foreignkey')
    op.create_foreign_key(None, 'item', 'user', ['owner_id'], ['id'])
    op.add_column('user', sa.Column('username', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True))
    op.add_column('user', sa.Column('first_name', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True))
    op.add_column('user', sa.Column('last_name', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True))
    op.add_column('user', sa.Column('phone_number', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True))
    op.add_column('user', sa.Column('gender', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True))
    op.add_column('user', sa.Column('date_of_birth', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True))
    op.add_column('user', sa.Column('avatar', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True))
    op.add_column('user', sa.Column('level', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True))
    op.add_column('user', sa.Column('cgpa', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True))
    op.add_column('user', sa.Column('matric_number', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True))
    op.add_column('user', sa.Column('institution', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True))
    op.add_column('user', sa.Column('faculty', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True))
    op.add_column('user', sa.Column('department', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True))
    op.drop_column('user', 'full_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('full_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('user', 'department')
    op.drop_column('user', 'faculty')
    op.drop_column('user', 'institution')
    op.drop_column('user', 'matric_number')
    op.drop_column('user', 'cgpa')
    op.drop_column('user', 'level')
    op.drop_column('user', 'avatar')
    op.drop_column('user', 'date_of_birth')
    op.drop_column('user', 'gender')
    op.drop_column('user', 'phone_number')
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'first_name')
    op.drop_column('user', 'username')
    op.drop_constraint(None, 'item', type_='foreignkey')
    op.create_foreign_key('item_owner_id_fkey', 'item', 'user', ['owner_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###
