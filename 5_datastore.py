# Author:     Shepard Berry
# Class:      MIS-4322
# Due:        2/8/2023
# Assignment: Dictionaries


# Below is a dictionary that contains information about real estate space for
# a doctor's office. Using the dictionary, create a csv file that has details
# for each space represented as rows. Name your file 'retail_space.csv.


'''
Your final output should look like:

room-number,use,sq-ft,price
100,reception,50,75
101,waiting,250,75
102,examination,125,150
103,examination,125,150
104,office,150,100

'''

import pandas as pandas
from pandas import DataFrame


datastore = { "medical":[
      { "room-number": 100,
        "use": "reception",
        "sq-ft": 50,
        "price": 75
      },
      { "room-number": 101,
        "use": "waiting",
        "sq-ft": 250,
        "price": 75
      },
      { "room-number": 102,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 103,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 104,
        "use": "office",
        "sq-ft": 150,
        "price": 100
      }

      ]
}

def main():
    data = {"room-number":[], "use":[],"sq-ft":[], "price":[]}
    for exam in datastore['medical']:
        data["room-number"].append(exam["room-number"])
        data["use"].append(exam["use"])
        data["sq-ft"].append(exam["sq-ft"])
        data["price"].append(exam["price"])

    df = DataFrame(data)
    df.to_csv('retail_space.csv', index=False)

        



    
if __name__ == "__main__":
    main()