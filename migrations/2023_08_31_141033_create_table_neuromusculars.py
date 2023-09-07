from orator.migrations import Migration


class CreateTableNeuromusculars(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('neuromusculars') as table:
            table.increments('id')
            table.integer('person_id').unsingned()

            table.string('neuromuscular_protocol', 21)

            table.small_integer('bench_press_lifted')
            table.small_integer('bench_press_reps')
            table.decimal('bench_press_rm', 5, 1)
            table.small_integer('bench_press_points')
            table.small_integer('barbell_curl_lifted')
            table.small_integer('barbell_curl_reps')
            table.decimal('barbell_curl_rm', 5, 1)
            table.small_integer('barbell_curl_points')
            table.small_integer('pull_down_lifted')
            table.small_integer('pull_down_reps')
            table.decimal('pull_down_rm', 5, 1)
            table.small_integer('pull_down_points')
            table.small_integer('leg_press_lifted')
            table.small_integer('leg_press_reps')
            table.decimal('leg_press_rm', 5, 1)
            table.small_integer('leg_press_points')
            table.small_integer('leg_extension_lifted')
            table.small_integer('leg_extension_reps')
            table.decimal('leg_extension_rm', 5, 1)
            table.small_integer('leg_extension_points')
            table.small_integer('leg_curl_lifted')
            table.small_integer('leg_curl_reps')
            table.decimal('leg_curl_rm', 5, 1)
            table.small_integer('leg_curl_points')

            table.small_integer('total_points')

            table.timestamp('created_at')
            table.soft_deletes()

            table.foreign('person_id').references(
                'id').on('persons').on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('neuromusculars')
