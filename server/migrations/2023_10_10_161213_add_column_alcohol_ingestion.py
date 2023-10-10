from orator.migrations import Migration


class AddColumnAlcoholIngestion(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('anamneses') as table:
            table.string('alcohol_ingestion', 100).nullable()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('anamneses') as table:
            table.drop_column('alcohol_ingestion')
