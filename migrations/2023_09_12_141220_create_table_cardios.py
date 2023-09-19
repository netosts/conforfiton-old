from orator.migrations import Migration


class CreateTableCardios(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('cardios') as table:
            table.increments('id')
            table.integer('person_id').unsingned()

            table.decimal('weight', 5, 2)
            table.string('cardio_protocol', 50)

            table.small_integer('l1_ellestad_conconi').nullable()  # bpm
            table.small_integer('l2_ellestad_conconi').nullable()  # bpm
            table.decimal('l1_fc_max_percentage', 5, 2).nullable()
            table.decimal('l2_fc_max_percentage', 5, 2).nullable()
            table.small_integer('distance').nullable()  # meters
            table.small_integer('time').nullable()  # minutes
            table.small_integer('fc_5min').nullable()  # bpm
            table.decimal('vo2max', 5, 1).nullable()
            table.decimal('vo2max_absolute', 4, 1).nullable()
            table.decimal('vo2max_mets', 5, 1).nullable()
            table.decimal('vvo2max', 5, 2).nullable()  # km/h
            table.decimal('vvo2max_pace', 4, 2).nullable()
            table.decimal('vl1', 5, 2).nullable()  # km/h
            table.decimal('vl1_pace', 4, 2).nullable()  # min/km
            table.decimal('vl2', 5, 2).nullable()  # km/h
            table.decimal('vl2_pace', 4, 2).nullable()  # min/km
            table.string('elder_aerobic_power',
                         18).nullable()  # classification
            table.small_integer('weekly_caloric_expenditure')  # kcal
            table.small_integer('daily_caloric_expenditure')  # kcal

            table.timestamp('created_at')
            table.soft_deletes()

            table.foreign('person_id').references(
                'id').on('persons').on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('cardios')
