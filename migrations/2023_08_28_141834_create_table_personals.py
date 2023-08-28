from orator.migrations import Migration


class CreateTablePersonals(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('personals') as table:
            table.integer('person_id').unsigned().unique()
            table.integer('company_id').unsigned()
            table.char('cref', 11).unique()
            table.string('status', 8)  # PENDING | DENIED | ACCEPTED
            table.soft_deletes()

            table.foreign('person_id').references(
                'id').on('persons').on_delete('cascade')
            table.foreign('company_id').references('id').on('companies')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('personals')
