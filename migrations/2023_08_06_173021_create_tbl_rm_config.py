from orator.migrations import Migration


class CreateTblRmConfig(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('tbl_rm_config') as table:
            table.increments('id')
            table.string('sexo', 9)
            table.string('exercicio', 30)
            table.float('threshold')
            table.small_integer('pontos')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('tbl_rm_config')
