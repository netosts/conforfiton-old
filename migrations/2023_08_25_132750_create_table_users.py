from orator.migrations import Migration


class CreateTableUsers(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('users') as table:
            table.integer('entity_id').unsingned()
            table.string('entity_type', 10)
            table.string('email').unique()
            table.string('hash_password')
            table.string('salt_password')
            table.timestamps()
            table.soft_deletes()

            table.index(['entity_id', 'entity_type'])

            table.foreign('entity_id').references(
                'id').on('persons').on_delete('cascade')
            table.foreign('entity_id').references(
                'id').on('companies').on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('users')
