from orator.migrations import Migration


class CreateTableLinkShares(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('link_shares') as table:
            table.increments('id')
            table.integer('personal_id').unsigned()
            table.string('salt_link')
            table.string('status', 9).default('Available')
            table.timestamps()

            table.foreign('personal_id').references(
                'person_id').on('personals')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('link_shares')
