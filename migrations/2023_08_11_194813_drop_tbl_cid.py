from orator.migrations import Migration


class DropTblCid(Migration):

    def up(self):
        """
        Run the migrations.
        """
        self.schema.drop('tbl_cid')

    def down(self):
        """
        Revert the migrations.
        """
