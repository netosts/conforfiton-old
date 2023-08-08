from orator.migrations import Migration


class ChangeTmBermudaName(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('tbl_aluno') as table:
            table.rename_column('tm_bermuda', 'tm_shorts')

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('tbl_aluno') as table:
            table.rename_column('tm_shorts', 'tm_bermuda')
