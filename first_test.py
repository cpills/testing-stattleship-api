"""
First tests
1/28/17
Access token: 9b4d8b9984d30c07c060a62990282be6
"""
from stattlepy import Stattleship

def main():
    print("hello")
    New_query = Stattleship()
    Token = New_query.set_token("9b4d8b9984d30c07c060a62990282be6")
    Output = New_query.ss_get_results(sport='basketball',league='nba',ep='game_logs',player_id='nba-stephen-curry')

    """
    for item in Output:
        for item2 in item.keys():
            print "########", item2
            for item3 in item[item2][0]:
                print item3
    print Output["players"]["last_name"]
    """

    """
    for item in Output:
        for key, val in item.items():
            print(key, val)
    """
    #print(Output[0].keys())
    print(Output[0]["teams"][0]["name"])

main()
