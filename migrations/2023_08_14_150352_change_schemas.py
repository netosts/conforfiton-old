from orator.migrations import Migration
from orator import DatabaseManager
import yaml
import os.path as opath


class ChangeSchemas(Migration):

    def up(self):
        """
        Run the migrations.
        """
        file = opath.join('etc', 'config.yaml')
        with open(f"{file}", 'r', encoding="UTF-8") as folder:
            # safe_load because load is deprecated
            config = yaml.safe_load(folder)
            db = DatabaseManager(config["databases"])

        with self.schema.table('tbl_anamnese') as table:
            table.string('q6').change()
            table.string('q7').change()
            table.string('q16').change()
            table.string('q23').change()

            db.statement(
                "ALTER TABLE tbl_anamnese ALTER COLUMN q24 TYPE BOOLEAN USING q24::boolean")
            db.statement(
                "ALTER TABLE tbl_anamnese ALTER COLUMN q25 TYPE BOOLEAN USING q25::boolean")

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('tbl_anamnese') as table:
            table.string('q6', 100).change()
            table.string('q7', 100).change()
            table.string('q16', 100).change()
            table.string('q23', 100).change()

            table.string('q24', 100).change()
            table.string('q25', 100).change()
