from orator.migrations import Migration


class CreateTblFqCardio(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('tbl_fq_cardio') as table:
            table.increments('id_fq_cardio')
            table.integer('id_pessoa').unsigned()
            table.foreign('id_pessoa').references('id_pessoa').on('tbl_pessoa')
            table.small_integer('bpm_repouso') # limite 3 
            table.small_integer('bpm_maximo')  # limite 3
            table.timestamp('dt_data')  


    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('tbl_fq_cardio')
