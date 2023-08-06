from orator.migrations import Migration


class RenameTblPessoa(Migration):

    def up(self):
        """
        Run the migrations.
        """
        self.schema.rename('tbl_Pessoa', 'tbl_pessoa')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.rename('tbl_pessoa', 'tbl_Pessoa')
