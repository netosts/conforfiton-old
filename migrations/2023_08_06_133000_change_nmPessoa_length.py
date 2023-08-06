from orator.migrations import Migration


class ChangeNmPessoaLength(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('tbl_pessoa') as table:
            table.rename_column('nmPessoa', 'nm_pessoa')

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('tbl_pessoa') as table:
            pass
