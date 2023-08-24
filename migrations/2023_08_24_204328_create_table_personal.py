from orator.migrations import Migration


class CreateTablePersonals(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('personals') as table:
            table.integer('person_id').unsigned().unique()
            table.integer('company_id').unsigned()

            table.foreign('person_id').references('id').on('persons')
            table.foreign('company_id').references('id').on('companies')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('personal')
