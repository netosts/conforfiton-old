from orator.migrations import Migration


class CreateTblAuth(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('tbl_auth') as table:
            table.integer('id_pessoa').unsigned().unique()
            table.foreign('id_pessoa').references('id_pessoa').on('tbl_pessoa')
            table.string('username', 30).unique()
            table.string('hash')
            table.string('salt')
            table.timestamps()
            table.soft_deletes()


    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('tbl_auth')
