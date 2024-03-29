from orator.migrations import Migration


class CreateTableWeights(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('weights') as table:
            table.increments('id')
            table.integer('person_id').unsigned()
            table.decimal('weight', 5, 2)
            table.timestamp('created_at')
            table.soft_deletes()
            
            table.foreign('person_id').references(
                'id').on('persons').on_delete('cascade')


    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('weights')
