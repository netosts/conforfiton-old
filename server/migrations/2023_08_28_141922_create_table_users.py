from orator.migrations import Migration


class CreateTableUsers(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('users') as table:
            table.integer('person_id').unsingned().unique()
            table.string('hash_password')
            table.string('salt_password')
            table.timestamps()
            table.soft_deletes()

            table.foreign('person_id').references(
                'id').on('persons').on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('users')
