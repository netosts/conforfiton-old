from orator.migrations import Migration


class CreateTblAluno(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('tbl_Aluno') as table:
            table.integer('ID_Pessoa').unsigned().unique()
            table.foreign('ID_Pessoa').references('ID_Pessoa').on('tbl_Pessoa')
            table.small_integer('altura')  # limite 3
            table.string('sexo', 15)
            table.string('tmCamisa', 3).nullable()
            table.text('fotoAluno').nullable()
            table.integer('ID_Empresa').unsigned()
            table.foreign('ID_Empresa').references('ID_Pessoa').on('tbl_Pessoa')
            table.integer('ID_Personal').unsigned()
            table.foreign('ID_Personal').references('ID_Pessoa').on('tbl_Pessoa')
    

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('tbl_Aluno')