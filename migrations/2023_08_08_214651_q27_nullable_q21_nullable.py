from orator.migrations import Migration


class Q27NullableQ21Nullable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('tbl_anamnese') as table:
            table.string('q21').nullable().change()
            table.string('q27').nullable().change()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('tbl_anamnese') as table:
            table.string('q21').change()
            table.string('q27').change()
