from orator.migrations import Migration


class CreateTblNeuromuscular(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('tbl_neuromuscular') as table:
            table.increments('id_neuromuscular')
            table.integer('id_pessoa').unsigned()
            table.small_integer('pl_bench_press')
            table.small_integer('pl_direct_thread')
            table.small_integer('pl_pull_front')
            table.small_integer('pl_leg_press')
            table.small_integer('pl_knee_extension')
            table.small_integer('pl_knee_bending')
            table.small_integer('reps_bench_press')
            table.small_integer('reps_direct_thread')
            table.small_integer('reps_pull_front')
            table.small_integer('reps_leg_press')
            table.small_integer('reps_knee_extension')
            table.small_integer('reps_knee_bending')
            table.decimal('rm_bench_press', 4, 1)
            table.decimal('rm_direct_thread', 4, 1)
            table.decimal('rm_pull_front', 4, 1)
            table.decimal('rm_leg_press', 4, 1)
            table.decimal('rm_knee_extension', 4, 1)
            table.decimal('rm_knee_bending', 4, 1)
            table.small_integer('pontos_bench_press')
            table.small_integer('pontos_direct_thread')
            table.small_integer('pontos_pull_front')
            table.small_integer('pontos_leg_press')
            table.small_integer('pontos_knee_extension')
            table.small_integer('pontos_knee_bending')
            table.small_integer('total_pontos')
            table.timestamp('created_at')

            table.foreign('id_pessoa').references('id_pessoa').on('tbl_pessoa')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('tbl_neuromuscular')
