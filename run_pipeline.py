import os

from src.shopify_connector import ShopifyConnector
from src.synthetic_data_generator import generate_orders


def run_pipeline():

    os.makedirs(
        "data/raw",
        exist_ok=True
    )

    connector = ShopifyConnector()

    products_df = connector.get_products()

    products_df.to_csv(
        "data/raw/products_raw.csv",
        index=False
    )

    print(
        f"Products saved: "
        f"{products_df.shape}"
    )

    orders_df = generate_orders(
        products_df
    )

    orders_df.to_csv(
        "data/raw/orders_raw.csv",
        index=False
    )

    print(
        f"Orders generated: "
        f"{orders_df.shape}"
    )

    print("\nPipeline completed successfully")


if __name__ == "__main__":

    run_pipeline()