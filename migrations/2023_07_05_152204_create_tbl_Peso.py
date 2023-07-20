from orator.migrations import Migration


class CreateTblPeso(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('tbl_peso') as table:
            table.increments('ID_peso')
            table.integer('ID_Pessoa').unsigned()
            table.foreign('ID_Pessoa').references('ID_Pessoa').on('tbl_Pessoa')
            table.double('peso', 3, 2)
            table.timestamp('dtData')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('tbl_peso')
