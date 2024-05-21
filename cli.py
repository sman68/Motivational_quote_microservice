import click
import requests

@click.group()
def cli():
    pass

@click.command()
def get_random_quote():
    """Fetch a random motivational quote"""
    response = requests.get("http://localhost:5000/quotes")
    if response.status_code == 200:
        quote = response.json()["quote"]
        click.echo(quote)
        favorite = click.confirm('Do you want to favorite this quote?', default=False)
        if favorite:
            response = favorite_quote(quote)
            if response.status_code == 201:
                click.echo("Quote favorited successfully")
            else:
                click.echo("Error: Could not favorite quote")
    else:
        click.echo("Error: Could not retrieve quote")

@click.command()
def get_category_quote():
    """Fetch a motivational quote from a specific category"""
    category = click.prompt("Please enter the category (Inspiration, Focus, Funny Motivation, Success)", type=str)
    response = requests.get(f"http://localhost:5000/quotes?category={category}")
    if response.status_code == 200:
        quote = response.json()["quote"]
        click.echo(quote)
        favorite = click.confirm('Do you want to favorite this quote?', default=False)
        if favorite:
            response = favorite_quote(quote)
            if response.status_code == 201:
                click.echo("Quote favorited successfully")
            else:
                click.echo("Error: Could not favorite quote")
    else:
        click.echo("Error: Could not retrieve quote")

@click.command()
def get_favorites():
    """Retrieve all favorite quotes"""
    response = requests.get("http://localhost:5000/quotes/favorites")
    if response.status_code == 200:
        favorites = response.json()
        for favorite in favorites:
            click.echo(favorite["quote"])
    else:
        click.echo("Error: Could not retrieve favorites")

def favorite_quote(quote):
    url = "http://localhost:5000/quotes/favorite"
    response = requests.post(url, json={"quote": quote})
    return response

cli.add_command(get_random_quote)
cli.add_command(get_category_quote)
cli.add_command(get_favorites)

if __name__ == '__main__':
    cli()
