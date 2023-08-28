from orator.migrations import Migration


class CreateTableRmConfig(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('rm_config') as table:
            table.increments('id')
            table.string('gender', 6)
            table.string('exercise', 30)
            table.float('threshold')
            table.small_integer('points')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('rm_config')
