from orator.migrations import Migration


class CreateTableRmlForNeuromusculars(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('neuromusculars_rml') as table:
            table.increments('id')
            table.integer('person_id').unsingned()

            table.string('neuromuscular_protocol', 21)

            table.small_integer('sit_up').nullable()
            table.small_integer('push_up').nullable()
            table.small_integer('jump').nullable()

            table.string('sit_up_result', 15).nullable()
            table.string('push_up_result', 15).nullable()
            table.string('jump_result', 15).nullable()

            table.timestamp('created_at')
            table.soft_deletes()

            table.foreign('person_id').references(
                'id').on('persons').on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('neuromusculars_rml')
