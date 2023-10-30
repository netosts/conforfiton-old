from orator.migrations import Migration


class AddColumnFcMaxFormula(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('anamneses') as table:
            table.string('fc_max_formula', 12).nullable()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('anamneses') as table:
            table.drop_column('fc_max_formula')
