from orator.migrations import Migration


class CreateTableAntropometrias(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('antropometrias') as table:
            table.increments('id')
            table.integer('person_id').unsingned()

            table.decimal('weight', 5, 2)

            table.string('antropometria_protocol', 21)
            table.decimal('abs', 5, 2)
            table.decimal('waist', 5, 2)
            table.decimal('hip', 5, 2)
            table.decimal('thighs', 5, 2).nullable()
            table.decimal('right_biceps', 5, 2).nullable()
            table.decimal('right_forearm', 5, 2).nullable()
            table.decimal('chest', 5, 2).nullable()
            table.decimal('triceps', 5, 2).nullable()
            table.decimal('suprailiac', 5, 2).nullable()
            table.decimal('subcapularis', 5, 2).nullable()
            table.decimal('midaxillary', 5, 2).nullable()

            table.decimal('imc_result', 4, 2)
            table.string('imc_class', 30)
            table.string('ca_class', 30)
            table.json('ca_risk').nullable()
            table.decimal('rcq_result', 3, 2)
            table.string('rcq_class', 30)
            table.string('rcae_class', 30)
            table.decimal('iac_result', 4, 2)
            table.string('iac_class', 30)
            table.decimal('pg_result', 4, 1)
            table.string('pg_class', 30)

            table.timestamp('created_at')
            table.soft_deletes()

            table.foreign('person_id').references(
                'id').on('persons').on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('antropometrias')
