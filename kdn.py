import click
from click import echo
from click import style


@click.group()
@click.option('--rss/--no-rss', default=False)
def kdncli():
    """ What's new on KDNuggets """
    pass


@kdncli.command(name="podcasts")
def podcasts():
    """ List podcasts """
    echo(" List podcasts ")
    pass


@kdncli.command(name="view")
def go():
    """ Go to the story on KDNuggets """
    echo(" Story: ")
    pass


@kdncli.command(name="stories")
@click.option('--sort_by', '-s', default='newest',
              type=click.Choice(['newest', 'best']), help='sort type')
@click.option('--limit', '-l', default=10, type=click.INT,
              help='number of top stories to show')
def stories(sort_by, limit):
    """ List stories """
    echo(" List stories ")
    pass


@click.command()
def usage():
    """ Simple program that reads stories from KDNuggets in a command line """
    echo(style(' KDNuggets reader v. 0.1 ', fg='yellow'))


if __name__ == '__main__':
    echo(" KDNuggets - for data hackers ")
    usage()
