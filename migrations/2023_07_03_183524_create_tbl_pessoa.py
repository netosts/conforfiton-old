from orator.migrations import Migration


class CreateTblPessoa(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('tbl_pessoa') as table:
            table.increments('id_pessoa')
            table.string('nm_pessoa', 100)
            table.string('ser', 20)
            table.char('tipo_pessoa', 2)
            table.string('cpf_cnpj', 14).unique()
            table.string('rg', 20).nullable()
            table.char('uf_rg', 2).nullable()
            table.string('ds_razao_social', 60).nullable()
            table.string('ds_inscricao_estadual', 30).nullable()
            table.string('ds_inscricao_municipal', 30).nullable()
            table.boolean('isento_ie').nullable()
            table.boolean('emp_personal')
            table.date('dt_nascimento').nullable()
            table.text('ds_obs').nullable()
            table.string('ds_email', 80).unique()
            table.string('telefone', 11).nullable()
            table.timestamps()
            table.soft_deletes()
            

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('tbl_pessoa')