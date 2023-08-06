from orator.migrations import Migration


class CreateTblPeso(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('tbl_peso') as table:
            table.increments('id_peso')
            table.integer('id_pessoa').unsigned()
            table.foreign('id_pessoa').references('id_pessoa').on('tbl_pessoa')
            table.double('peso', 3, 2)
            table.timestamp('dt_data')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('tbl_peso')
