from orator.migrations import Migration


class CreateTblAluno(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('tbl_Aluno') as table:
            table.integer('ID_Pessoa').unsigned()
            table.foreign('ID_Pessoa').references('ID_Pessoa').on('tbl_Pessoa').unique()
            table.integer('altura')
            table.string('sexo', 15)
            table.json('fotoAluno').nullable()
    

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('tbl_Aluno')