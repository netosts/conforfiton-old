from orator.migrations import Migration


class CreateTableAnamneses(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('anamneses') as table:
            table.integer('person_id').unsigned().unique()
            table.string('q1')
            table.string('q2', 100)
            table.string('q3', 100)
            table.json('q4')
            table.string('q5')
            table.string('q6')
            table.string('q7')
            table.string('q8', 100)
            table.string('q9', 100)
            table.string('q10', 100)
            table.string('q11', 100)
            table.small_integer('q12')
            table.json('q13').default('[]')
            table.boolean('q14')
            table.boolean('q15')
            table.string('q16')
            table.small_integer('q17')
            table.string('q18', 100)
            table.string('q19', 100)
            table.boolean('q20')
            table.string('q21').nullable()
            table.string('q22', 100)
            table.string('q23')
            table.boolean('q24')
            table.boolean('q25')
            table.string('q26', 100)
            table.string('q27').nullable()
            table.timestamps()
            table.soft_deletes()

            table.foreign('person_id').references(
                'id').on('persons').on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('anamneses')
