# Author:     Shepard Berry
# Class:      MIS-4322
# Due:        2/8/2023
# Assignment: Dictionaries

"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons. This
information can be found in the ValueLabels file.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 50%
Display report for all universities that have a total price for in-state students living off campus over $50,000



"""

import json

def generate_report(school):
    return (f'University Name: {school["instnm"]}\n'
        f'Graduation Rate for Women: {school["Graduation rate  women (DRVGR2020)"]}%\n'
    )
def main():

    with open("school_data.json", 'r') as f:
        labels = {372 : "American Athletic Conference", 108 : "Big Twelve Conference", 107 : "Big Ten Conference", 130 : "Southeastern Conference"}
        data = json.load(f)

        # get only schools that are in the conferences looked for
        valid_schools = [school for school in data if school['NCAA']["NAIA conference number football (IC2020)"] in labels]

        # print schools that have grad rate for women of 50%
        print("---SCHOOLS WITH A GRADUATION RATE OVER 80% FOR WOMEN---\n")

        key = "Graduation rate  women (DRVGR2020)"
        for school in valid_schools:
            if school[key] > 80:
                print(generate_report(school))

        print("\n")

        print("---SCHOOLS WITH AN INSTATE TUITION PRICE OVER $50k---\n")

        key = "Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"
        for school in valid_schools:

            if school[key] and school[key] > 50000:
                print(generate_report(school))

if __name__ == "__main__":
    main()