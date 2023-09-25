from orator.migrations import Migration


class ChangeQ2IsNullable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('anamneses') as table:
            table.string('q2', 100).nullable().change()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('anamneses') as table:
            table.string('q2', 100).change()
