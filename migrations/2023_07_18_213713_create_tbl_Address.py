from orator.migrations import Migration


class CreateTblAddress(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('tbl_address') as table:
            table.integer('id_pessoa').unsigned().unique()
            table.foreign('id_pessoa').references('id_pessoa').on('tbl_pessoa')
            table.string('rua', 80)
            table.small_integer('numero')  # limite 5
            table.string('complemento', 80).nullable()
            table.string('bairro', 60)
            table.string('cidade', 60)
            table.string('estado', 25)
            table.string('cep', 8)
            table.string('pais', 60)
            table.timestamps()
            table.soft_deletes()
            
        

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('tbl_address')