from orator.migrations import Migration


class CreateTblFqCardio(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('tbl_fqCardio') as table:
            table.increments('ID_fqCardio')
            table.integer('ID_Pessoa').unsigned()
            table.foreign('ID_Pessoa').references('ID_Pessoa').on('tbl_Pessoa')
            table.small_integer('bpmRepouso') # limite 3 
            table.small_integer('bpmMaximo')  # limite 3
            table.timestamp('dtData')  


    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('tbl_fqCardio')
