import click


@click.group()
def covey():
    pass


@click.command()
@click.argument('task')
def add(task):
    click.echo("add " + task)


@click.command()
def remove():
    click.echo("remove")


@click.command()
def change():
    click.echo("change")


covey.add_command(add)
covey.add_command(remove)
covey.add_command(change)

if __name__ == '__main__':
    covey()