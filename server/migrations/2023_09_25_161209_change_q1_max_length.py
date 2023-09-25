from orator.migrations import Migration


class ChangeQ1MaxLength(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('anamneses') as table:
            table.string('q1', 100).change()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('anamneses') as table:
            table.string('q1').change()
