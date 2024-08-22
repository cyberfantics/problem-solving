def minion_game(string):
    # Initialize scores
    kevin_score = 0
    stuart_score = 0
    length = len(string)
    
    # Vowels
    vowels = 'AEIOU'
    
    # Iterate over each character in the string
    for i in range(length):
        if string[i] in vowels:
            kevin_score += length - i  # Points for Kevin
        else:
            stuart_score += length - i  # Points for Stuart
    
    # Determine the winner
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")



if __name__ == '__main__':
    s = input()
    minion_game(s)