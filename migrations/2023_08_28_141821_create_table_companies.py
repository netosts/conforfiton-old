from orator.migrations import Migration


class CreateTableCompanies(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('companies') as table:
            table.increments('id')
            table.string('brand_name', 100)
            table.string('business_name', 100)
            table.char('cnpj', 14).unique()
            table.boolean('exempt_sr')
            table.string('state_registration', 14).unique()
            table.char('uf', 2)
            table.string('email').unique()
            table.char('phone_number', 11).unique()
            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('companies')
