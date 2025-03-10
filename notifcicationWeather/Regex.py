import re

input_string = "Mar 28 Atlanta 123, Boston 122 (OT) Murray 44 Pts Tatum 31 Pts"

pattern = r"(\w+ \d+)\s+([A-Za-z]+ \d{1,3},)\s+([A-Za-z]+ \d{1,3} \(?\w*\)?)\s+(\w+ \d+ Pts)\s+(\w+ \d+ Pts)"

match = re.match(pattern, input_string)

if match:
    date = match.group(1)
    team1_score = match.group(2)
    team2_score = match.group(3)
    top_scorer1 = match.group(4)
    top_scorer2 = match.group(5)

    print(f"Date: {date}")
    print(f"Team 1 Score: {team1_score}")
    print(f"Team 2 Score: {team2_score}")
    print(f"Top Scorer 1: {top_scorer1}")
    print(f"Top Scorer 2: {top_scorer2}")
else:
    print("The input string did not match the expected pattern.")
