def return_game_winner(score_table):
    ''' 
    Loops as long as the score table has scores inside it.
    Checks if the first character is A or B, and adds...
    the next character to the respective score (always int)
    Removes those two first characters from score table
    Checks if the score to win conditions are met
    '''
    a_score: int = 0
    b_score: int = 0
    while len(score_table) > 0:
        if score_table[0] == "A":
            a_score += int(score_table[1])
        elif score_table[0] == "B":
            b_score += int(score_table[1])
        score_table = score_table[2:]
        if abs(a_score-b_score) >= 2:
            if a_score >= 11 and a_score < b_score:
                return "A"
            if b_score >= 11:
                return  "B"

print(return_game_winner(input("Enter score table: ")))