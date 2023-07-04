from orator.migrations import Migration


class CreateTblPessoa(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('tbl_Pessoa') as table:
            table.increments('ID_Pessoa')
            table.string('nmPessoa', 60)
            table.boolean('ativo').nullable()
            table.string('ser', 2)
            table.char('tipoPessoa', 1)
            table.string('cpfCnpj', 14).unique()
            table.string('rg', 20).nullable()
            table.char('ufRG', 2).nullable()
            table.string('dsRazaoSocial', 60).nullable()
            table.string('dsInscricaoEstadual', 30).nullable()
            table.string('dsInscricaoMunicipal', 30).nullable()
            table.boolean('isentoIE').nullable()
            table.date('dtNascimento').nullable()
            table.text('dsObs').nullable()
            table.string('dsEmail', 80).nullable()
            table.string('telefone', 11).nullable()
            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('tbl_Pessoa')