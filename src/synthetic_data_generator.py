import pandas as pd
import numpy as np


def generate_orders(products_df):

    np.random.seed(42)

    products_df = products_df[
        products_df["product_type"].fillna("")
        != "giftcard"
    ]

    dates = pd.date_range(
        start="2022-01-01",
        end="2025-01-01",
        freq="D"
    )

    rows = []

    order_id = 100000

    for _, product in products_df.iterrows():

        popularity = np.random.uniform(
            0.5,
            5.0
        )

        trend = np.random.uniform(
            0.0001,
            0.001
        )

        for day_num, date in enumerate(dates):

            seasonality = 1.0

            if date.month in [11, 12]:
                seasonality = 2.5

            elif date.month in [6, 7]:
                seasonality = 1.5

            expected_sales = (
                popularity
                * seasonality
                * (1 + trend * day_num)
            )

            quantity = np.random.poisson(
                expected_sales
            )

            if quantity == 0:
                continue

            rows.append({
                "order_id": order_id,
                "order_date": date,
                "financial_status": "paid",
                "product_id":
                product["product_id"],
                "variant_id":
                product["variant_id"],
                "sku":
                product["sku"],
                "product_title":
                product["product_title"],
                "quantity":
                quantity,
                "unit_price":
                product["price"],
                "total_price":
                quantity * product["price"]
            })

            order_id += 1

    return pd.DataFrame(rows)