from orator.migrations import Migration


class CreateTableCompanies(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('companies') as table:
            table.increments('id')
            table.string('name', 100)
            table.char('cnpj', 14).unique()
            table.string('email').unique()
            table.string('phone_number', 20).unique()
            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('company')
