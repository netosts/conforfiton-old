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
            table.string('antropometria_protocol', 50)

            # required
            table.decimal('abdominal_circumference', 5, 2)
            table.decimal('waist_circumference', 5, 2)
            table.decimal('hip_circumference', 5, 2)
            # nullable
            table.decimal('thighs_circumference', 5, 2).nullable()
            table.decimal('right_biceps_circumference', 5, 2).nullable()
            table.decimal('right_forearm_circumference', 5, 2).nullable()
            table.decimal('chest_skin_fold', 5, 2).nullable()
            table.decimal('abdominal_skin_fold', 5, 2).nullable()
            table.decimal('thighs_skin_fold', 5, 2).nullable()
            table.decimal('triceps_skin_fold', 5, 2).nullable()
            table.decimal('suprailiac_skin_fold', 5, 2).nullable()
            table.decimal('subscapularis_skin_fold', 5, 2).nullable()
            table.decimal('midaxillary_skin_fold', 5, 2).nullable()
            table.decimal('iliac_circumference', 5, 2).nullable()

            table.decimal('imc_result', 4, 2)
            table.string('imc_class', 30)
            table.string('ca_class', 30)
            table.json('ca_risk').nullable()
            table.decimal('rcq_result', 3, 2)
            table.string('rcq_class', 30)
            table.decimal('rcae_result', 3, 2)
            table.string('rcae_class', 30)
            table.decimal('iac_result', 4, 2)
            table.string('iac_class', 30)
            table.decimal('pg_result', 3, 1)
            table.string('pg_class', 30)

            table.decimal('pg_goal', 3, 1)
            table.decimal('weight_goal', 5, 2)
            table.decimal('mig_result', 3, 1)
            table.small_integer('mig_goal')
            table.decimal('fat_weight_result', 5, 2)
            table.decimal('fat_weight_goal', 4, 2)
            table.decimal('mig_weight_result', 5, 2)
            table.decimal('mig_weight_goal', 4, 1)

            table.timestamp('created_at')
            table.soft_deletes()

            table.foreign('person_id').references(
                'id').on('persons').on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('antropometrias')
