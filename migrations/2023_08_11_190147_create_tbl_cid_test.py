from orator.migrations import Migration


class CreateTblCidTest(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('tbl_cid') as table:
            table.increments('id')
            table.string('name')

    def down(self):
        """
        Revert the migrations.
        """

