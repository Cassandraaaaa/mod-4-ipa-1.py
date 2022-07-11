'''Module 4: Individual Programming Assignment 1
Parsing Data
This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.
    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.
    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.
    This function describes the relationship that two users have with each other.
    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.
    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.    
    socialcircle_from = social_graph[from_member]["following"]
    socialcircle_to = social_graph[to_member]["following"]
    
    if from_member in socialcircle_to and to_member in socialcircle_from:
        return("friends")
    elif from_member in socialcircle_to:
        return("followed by")
    elif to_member in socialcircle_from:
        return("follower")
    else:
        return("no relationship")  

def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.
    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    This function evaluates a tic tac toe board and returns the winner.
    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.
    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    each_subset = 0
    character_in_subset = 0
    for i in board:
        for j in i:
            if board[each_subset][character_in_subset] == "X":
                board[each_subset][character_in_subset] = 1
            elif board[each_subset][character_in_subset] == "O":
                board[each_subset][character_in_subset] = -1
            else:
                board[each_subset][character_in_subset] = 0
    
            each_subset += 1
        each_subset = 0
        character_in_subset +=1
    
    board_size = len(board) - 1
    num_subsets = len(board)
    
    horizontal_sums = [sum(x) for x in board]
    vertical_sums = [sum(x) for x in zip(*board)]
    updown_diagonal_sum = [sum([board [i][i] for i,v in enumerate (board)])]
    downup_diagonal_sum = [sum([board [board_size-i][i] for i,v in enumerate (board)])]
    
    if max(horizontal_sums) == num_subsets or max(vertical_sums) == num_subsets or max(updown_diagonal_sum) == num_subsets or max(downup_diagonal_sum) == num_subsets:
        return ("X")
    elif min(horizontal_sums) == -num_subsets or min(vertical_sums) == -num_subsets or min(updown_diagonal_sum) == -num_subsets or min(downup_diagonal_sum) == -num_subsets:
        return ("O")
    else:
        return ("NO WINNER")

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    time = 0
    legs = route_map
    while first_stop != second_stop:
        for leg, travel_time_mins in legs.items():
            if first_stop == second_stop:
                break
            if leg[0] == first_stop:
                time += travel_time_mins['travel_time_mins']
                first_stop = leg[1]    
    return(time)

