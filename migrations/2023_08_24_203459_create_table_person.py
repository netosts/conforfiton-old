from orator.migrations import Migration


class CreateTablePersons(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('persons') as table:
            table.increments('id')
            table.string('name', 100)
            table.char('cpf', 11).unique()
            table.string('gender', 6)
            table.string('role', 10)
            table.string('email').unique()
            table.string('phone_number', 20).unique()
            table.date('birth_date')
            table.small_integer('height')  # 0 < height < 250
            table.string('shirt_size', 3)
            table.string('shorts_size', 3)
            table.text('profile_picture').nullable()
            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('person')
