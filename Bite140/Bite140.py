import pandas as pd

data = "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"


def athletes_most_medals(data=data):
    olympic_data = pd.read_csv(data)
    olympic_data_gold_men = olympic_data[(olympic_data['Gender'] == 'Men')]\
        .groupby(['Athlete']).agg('count').sort_values(by=['Medal'], ascending=False).head(1)
    olympic_data_gold_men = olympic_data_gold_men['Medal']
    olympic_data_gold_women = women = olympic_data[(olympic_data['Gender'] == 'Women')]\
        .groupby(['Athlete']).agg('count').sort_values(by=['Medal'], ascending=False).head(1)
    olympic_data_gold_women = olympic_data_gold_women['Medal']

    return pd.concat([olympic_data_gold_men, olympic_data_gold_women])

a = athletes_most_medals()
print(a['LATYNINA, Larisa'])
print(a['PHELPS, Michael'])
print(len(a))