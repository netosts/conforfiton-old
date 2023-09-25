from orator.migrations import Migration


class CreateColumnPersonalGoal(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('students') as table:
            table.string('personal_goal', 100).nullable()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('students') as table:
            table.drop_column('personal_goal')
