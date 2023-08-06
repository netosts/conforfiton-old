from orator.migrations import Migration


class CreateTblAluno(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('tbl_aluno') as table:
            table.integer('id_pessoa').unsigned().unique()
            table.foreign('id_pessoa').references('id_pessoa').on('tbl_pessoa')
            table.small_integer('altura')  # limite 3
            table.string('sexo', 15)
            table.string('tm_camisa', 3).nullable()
            table.string('tm_bermuda', 3).nullable()
            table.text('foto_aluno').nullable()
            table.integer('id_empresa').unsigned()
            table.foreign('id_empresa').references('id_pessoa').on('tbl_pessoa')
            table.integer('id_personal').unsigned()
            table.foreign('id_personal').references('id_pessoa').on('tbl_pessoa')
    

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('tbl_aluno')