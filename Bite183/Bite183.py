import os
from urllib.request import urlretrieve

import pandas as pd
import xlrd

TMP = os.getenv("TMP", "/tmp")
EXCEL = os.path.join(TMP, 'order_data.xlsx')
if not os.path.isfile(EXCEL):
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/order_data.xlsx',
        EXCEL
    )


def load_excel_into_dataframe(excel=EXCEL):
    """Load the SalesOrders sheet of the excel book (EXCEL variable)
       into a Pandas DataFrame and return it to the caller"""
    sales_orders = pd.read_excel(EXCEL, sheet_name='SalesOrders')
    return sales_orders

sales_orders = load_excel_into_dataframe(excel=EXCEL)

def get_year_region_breakdown(df):
    """Group the DataFrame by year and region, summing the Total
       column. You probably need to make an extra column for
       year, return the new df as shown in the Bite description"""
    df['Year'] = df['OrderDate'].dt.year
    return df.groupby(['Year', 'Region'])['Total'].agg('sum')


def get_best_sales_rep(df):
    """Return a tuple of the name of the sales rep and
       the total of his/her sales"""
    total_sales_by_rep = df.groupby(['Rep'])['Total'].agg('sum')
    best_sales_rep = total_sales_by_rep.sort_values(ascending=False).head(1)
    return best_sales_rep.index[0], best_sales_rep[0]



def get_most_sold_item(df):
    """Return a tuple of the name of the most sold item
       and the number of units sold"""
    sum_of_item_sold = df.groupby('Item')['Units'].agg('sum')
    highest_item_sold = sum_of_item_sold.sort_values(ascending=False).head(1)
    return highest_item_sold.index[0], highest_item_sold[0]