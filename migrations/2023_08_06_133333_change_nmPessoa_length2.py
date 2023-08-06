from orator.migrations import Migration


class ChangeNmPessoaLength2(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('tbl_pessoa') as table:
            table.string('nm_pessoa', 100).change()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('tbl_pessoa') as table:
            table.string('nm_pessoa', 60).change()