import typer

from bible_cli.processor import QueryProcessor

app = typer.Typer()


@app.command()
def about():
    print(
        '✝️ BIBLE_CLI is simple cli app to query bible text '
        'from many bible portuguese versions'
    )


@app.command()
def query(q: str):
    """
    Get a text using query:
    [book] [chapter]:[verse/range] [version]

    Examples:
        Eclesiastes 3:15
        Eclesiastes 3:15-16
        Eclesiastes 3:15 ARA
    """

    processor = QueryProcessor()
    output = processor.process_query(q)
    typer.echo(output)


if __name__ == '__main__':
    app()
