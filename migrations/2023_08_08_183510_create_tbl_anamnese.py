from orator.migrations import Migration


class CreateTblAnamnese(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('tbl_anamnese') as table:
            table.integer('id_pessoa').unsigned().unique()
            table.foreign('id_pessoa').references('id_pessoa').on('tbl_pessoa')
            table.string('q1')
            table.string('q2', 100)
            table.string('q3', 100)
            table.json('q4')
            table.string('q5')
            table.string('q6', 100)
            table.string('q7', 100)
            table.string('q8', 100)
            table.string('q9', 100)
            table.string('q10', 100)
            table.string('q11', 100)
            table.small_integer('q12')
            table.json('q13').default('[]')
            table.boolean('q14')
            table.boolean('q15')
            table.string('q16', 100)
            table.small_integer('q17')
            table.string('q18', 100)
            table.string('q19', 100)
            table.boolean('q20')
            table.string('q21')
            table.string('q22', 100)
            table.string('q23', 100)
            table.string('q24', 100)
            table.string('q25', 100)
            table.string('q26', 100)
            table.string('q27')
            table.timestamps()
            table.soft_deletes()


    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('tbl_anamnese')
