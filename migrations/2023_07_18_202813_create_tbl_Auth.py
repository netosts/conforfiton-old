from orator.migrations import Migration


class CreateTblAuth(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('tbl_Auth') as table:
            table.integer('ID_Pessoa').unsigned().unique()
            table.foreign('ID_Pessoa').references('ID_Pessoa').on('tbl_Pessoa')
            table.string('username', 30).unique()
            table.string('hash')
            table.string('salt')
            table.timestamps()
            table.soft_deletes()


    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('tbl_Auth')
