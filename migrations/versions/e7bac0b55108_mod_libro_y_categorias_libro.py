"""mod libro y categorias_libro

Revision ID: e7bac0b55108
Revises: d8e89e769ee3
Create Date: 2024-06-25 09:56:19.948468

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7bac0b55108'
down_revision = 'd8e89e769ee3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('libro',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('titulo', sa.String(length=150), nullable=False),
    sa.Column('descripcion', sa.Text(), nullable=False),
    sa.Column('fecha_publicacion', sa.Date(), nullable=False),
    sa.Column('autor_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['autor_id'], ['autor.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('categorias_libro',
    sa.Column('libro_id', sa.Integer(), nullable=False),
    sa.Column('categoria_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['categoria_id'], ['categoria.id'], ),
    sa.ForeignKeyConstraint(['libro_id'], ['libro.id'], ),
    sa.PrimaryKeyConstraint('libro_id', 'categoria_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('categorias_libro')
    op.drop_table('libro')
    # ### end Alembic commands ###