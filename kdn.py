import click
from click import echo
from click import style
import feedparser


class Config(object):

    def __init__(self):
        self.verbose = False
        self.rss = False


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--rss/--no-rss', default=False)
@click.option('--verbose', is_flag=True)
@click.option('--save-directory', type=click.Path())
@pass_config
def cli(config, verbose, rss, save_directory):
    """ What's new on KDNuggets """
    """ Simple program that reads stories from KDNuggets in a command line """
    if verbose:
        echo(" Verbose mode enabled")
    if not rss:
        echo(" Parsing pure HTML for content")
    if save_directory is None:
        save_directory = '.'
    config.verbose = verbose
    config.save_directory = save_directory
    config.rss = rss


@cli.command(name="podcasts")
def podcasts():
    """ List podcasts """
    echo(" List podcasts")
    pass


@cli.command(name="view")
def go():
    """ Go to the particular story on KDNuggets """
    echo(" Story:")
    pass


@cli.command(name="stories")
@click.option('--sort_by', '-s', default='newest',
              type=click.Choice(['newest', 'best']),
              help='How news should be sorted')
@click.option('--limit', '-l', default=10, type=click.INT,
              help='number of top stories to show')
@pass_config
def stories(config, sort_by, limit):
    """ List stories """
    echo(" Listing KDN stories...")
    if (config.verbose):
        echo("Running stories(sort_by=" + str(sort_by) +
             ", limit=" + str(limit) + ")")
        echo("Save directory is %s" % config.save_directory)
    if (config.rss):
        feeds = feedparser.parse('http://feeds.feedburner.com/kdnuggets-data-mining-analytics?format=xml')
        if (config.verbose):
            echo(feeds.feed.title)
            echo(feeds.feed.link)
            echo(feeds.feed.description)
            try:
                echo(feeds.feed.published)
            except AttributeError:
                echo('Feed RSS xml without \'published\' attribute')
            try:
                echo(feeds.feed.published_parsed)
            except AttributeError:
                echo('Feed RSS xml without \'published_parsed\' attribute')
        echo('Entries in feedparser:' + str(len(feeds.entries)))
        for x in range(0, limit):
            echo('Item no. :' + str(x))
            echo(feeds.entries[x].title)
            echo(feeds.entries[x].summary)
    pass


@cli.command(name="jobs")
def jobs():
    """ List jobs """
    echo(style(' Listing news on jobs as seen on KDNuggets...', fg='yellow'))


@cli.command(name="academic")
def academic():
    """ List academic topics """
    echo(style(' KDNuggets academic', fg='yellow'))


if __name__ == '__main__':
    echo(" KDNuggets - command line tool for data hackers")
    cli()
