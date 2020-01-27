import pandas as pd

data = "https://s3.us-east-2.amazonaws.com/bites-data/menu.csv"
# load the data in once, functions will use this module object
df = pd.read_csv(data)

pd.options.mode.chained_assignment = None  # ignore warnings


def get_food_most_calories(df=df):
    """Return the food "Item" string with most calories"""
    idx_max_calories = df[['Calories']].idxmax()[0]
    result = df.loc[idx_max_calories].Item
    return result


def get_bodybuilder_friendly_foods(df=df, excl_drinks=False):
    """Calulate the Protein/Calories ratio of foods and return the
       5 foods with the best ratio.

       This function has a excl_drinks switch which, when turned on,
       should exclude 'Coffee & Tea' and 'Beverages' from this top 5.

       You will probably need to filter out foods with 0 calories to get the
       right results.

       Return a list of the top 5 foot Item stings."""
    p_to_c_ratio = df['Protein'] / df['Calories']
    df['p_to_c_ratio'] = p_to_c_ratio
    if excl_drinks:
        result = df[
                     (df['Calories'] > 0) &
                     (df['Category'] != 'Beverages') &
                     (df['Category'] != 'Coffee & Tea')
                     ].sort_values('p_to_c_ratio', ascending=0).Item[0:5]
    else:
        result = df[df['Calories'] > 0].sort_values('p_to_c_ratio', ascending=0).Item[0:5]
    return result

g = get_bodybuilder_friendly_foods(df=df, excl_drinks=True)
print(g)