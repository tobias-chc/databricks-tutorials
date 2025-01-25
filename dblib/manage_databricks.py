"""Interact with Databricks clusters."""

import os

from databricks import sql
from databricks.sql.types import Row
from databricks_cli.clusters.api import ClusterApi
from databricks_cli.sdk.api_client import ApiClient


def list_clusters() -> list:
    """List all clusters in the Databricks workspace."""
    # Ensure the environment variables are set
    if not os.getenv("DATABRICKS_HOST") or not os.getenv("DATABRICKS_TOKEN"):
        raise EnvironmentError(
            "DATABRICKS_HOST and DATABRICKS_TOKEN must be set as environment variables."
        )
    api_client = ApiClient(
        host=os.getenv("DATABRICKS_HOST"), token=os.getenv("DATABRICKS_TOKEN")
    )
    clusters_api = ClusterApi(api_client)
    clusters_list = clusters_api.list_clusters()

    print(f"{'Cluster Name':<20} {'Cluster ID':<20}")
    print("-" * 40)
    for cluster in clusters_list["clusters"]:
        print(f"{cluster['cluster_name']:<20} {cluster['cluster_id']:<20}")

    return clusters_list


def querydb(query: str = "SELECT * FROM samples.nyctaxi.trips LIMIT 2") -> list[Row]:
    """Execute a SQL query on the Databricks workspace."""
    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()

        for row in result:
            print(row)

    return result
