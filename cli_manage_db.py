"""Databricks CLI commands"""

import click

from dblib.manage_databricks import list_clusters, querydb


@click.group()
def cli() -> None:
    """Manage Databricks"""


# build click command
@cli.command("list-clusters")
def list_clusters_command() -> None:
    """List Databricks clusters

    Example:
    ./cli-manage-db.py list-clusters
    """
    list_clusters()


# build a click command
@cli.command("query")
@click.option(
    "--query",
    default="SELECT * FROM samples.nyctaxi.trips LIMIT 2",
    help="SQL query to execute",
)
def cli_query(query) -> None:
    """Execute a SQL query"""
    querydb(query)


# run click group
if __name__ == "__main__":
    cli()
