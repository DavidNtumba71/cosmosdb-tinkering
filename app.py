from azure.cosmos import CosmosClient
from dotenv import load_dotenv
import os

load_dotenv()

URL = os.getenv("ACCOUNT_URI")
KEY = os.getenv("ACCOUNT_KEY")

cosmos_client = CosmosClient(URL, credential=KEY)

database_client = cosmos_client.get_database_client(database="demodb")
container_client = database_client.get_container_client(container="movies")

response = container_client.query_items(
    enable_cross_partition_query=True,
    query="SELECT * FROM c",
    populate_query_metrics=True,
)

data = list(response)
print(data)
#ru_usage = container_client.client_connection.last_response_headers['x-ms-request-charge']
#rint(f"{ru_usage} ru's used")
