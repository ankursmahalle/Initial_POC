from dotenv import load_dotenv
from pprint import pprint
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


load_dotenv()

def get_disease():
    df=pd.read_csv("C:\\Users\\MCS\\Downloads\\diabetes.csv")
    print(df.head())
    sns.countplot(x='Outcome', data=df)
    plt.show









if __name__ == "__main__":
    print('\n*** Get Disease ***\n')

    Glucose = input("\nPlease enter Disease: ")

    # Check for empty strings or string with only spaces
    # This step is not required here

    # glucose_data = get_sugar_level(Glucose)
    #
    # print("\n")
    # pprint(glucose_data)