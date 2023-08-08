from orator.migrations import Migration


class ChangeDoubleToDecimal(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('tbl_peso') as table:
            table.decimal('peso', 5, 2).change()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('tbl_peso') as table:
            table.double('peso', 3, 2).change()
