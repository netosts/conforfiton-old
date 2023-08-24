from orator.migrations import Migration


class CreateTableStudents(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('students') as table:
            table.integer('person_id').unsigned().unique()
            table.integer('company_id').unsigned()
            table.integer('personal_id').unsigned()

            table.foreign('person_id').references('id').on('persons')
            table.foreign('company_id').references('id').on('companies')
            table.foreign('personal_id').references('id').on('personals')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('students')
