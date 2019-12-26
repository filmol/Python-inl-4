scores = []

def welcome():
    print("*"*26)
    print("Klubbmästerskap i minigolf")
    print("*"*26)

def print_menu():
    print("\nMeny")
    print("*"*4)
    print("1: Visa resultat")
    print("2: Registrera resultat")
    print("3: Radera resultat")
    print("4: Spara & avsluta")

def get_result(): 
    """
    1. Opens the txt doc in read mode and saves it as a variable "score_board".
    2. Converts the score_board to a list through the split function.
    3. loops through each row in score_board and converts it to a list aswell (score_board = now a nested list).
    4. Create a temporary dictionary of everything in each one of the nested list.
    5. Adds the dictionary to a new list in global called scores

    If it can't find the file it shows error message, and describes that you now will start with a empty text file.
    """

    try:
        score_board = open("score_board.txt", "r")
        score_board = score_board.read().split("\n")

        #Removes the last list that only contanins a \n. 
        score_board.remove(score_board[-1])

        for player in score_board:
            new_board = player.split(";")
            temp = {} 
            temp["name"] = new_board[0]
            temp["varv1"] = new_board[1]
            temp["varv2"] = new_board[2]
            temp["varv3"] = new_board[3]    
            scores.append(temp)

    except FileNotFoundError:
        print("\n Text filen existerar ej så har precis skapat en ny tom fil.") 
        print("\n Du får nu registreara ett nytt resultat till filen.") 
        add_score()

    except IndexError:
        print("\n Text filen har fel struktur och är därför ogiltigt.") 
        print("\n Du får nu registrera ett nytt resultat som skriver över det ogiltiga formatet") 
        add_score()

def main():
    """
    Main function asks for input value and as long as input value isn't 4 it asks once more when the choosen fumction is done.
    If input value is 4 the program saves and exits.
    """

    welcome()
    get_result()
    choice = None

    while choice != 4:
        print_menu()
        print("*"*5)
        try:
            choice = int(input("Val :"))
        except:
            print("Skriv siffra")
            continue
        
        if choice == 1:
            show_score()

        elif choice == 2:
            add_score()

        elif choice == 3:
            delete_score()
             
        elif choice == 4:
            save()

    print("\nTack för medverkan!")

def save():
    """
    Writes over the old scoreboard with the new from the global list of dictionaries "scores"
    """
    my_file = open("score_board.txt", "w")
    for row in scores:
        my_file.write(row["name"]+";"+row["varv1"]+";"+row["varv2"]+";"+row["varv3"]+";\n")
    my_file.close()

def add_score(): 
    """
    Adds the input to a temporary dictionary, which the scores list appends in the end of the function.
    If the number in the rounds sections is'nt an int, the ValueError will print with a explanation.
    """

    print("\nLägg till resultat")
    temp = {}
    while True:
        try:
            temp["name"] = input("Namn: ")
            temp["varv1"] = int(input("Varv 1: "))
            temp["varv2"] = int(input("Varv 2: "))
            temp["varv3"] = int(input("Varv 3: "))
            break

        except ValueError:
            print("Skriv siffror för varje varv resultat")
    
    (temp["varv1"]) = str(temp["varv1"])
    (temp["varv2"]) = str(temp["varv2"])
    (temp["varv3"]) = str(temp["varv3"])

    scores.append(temp)
    print("\n{:10}{:10}{:10}{:10}".format(temp["name"],temp["varv1"],temp["varv2"],temp["varv3"]))

def show_score(): 
    """
    1. Loops through the dictionaries in scores and creates a "total" value for each, which contains of thje return from the tot function with the rounds as parameters.
    2. Does the same as above to calculate and create the "average" value.
    3. Calls the sort function through the sort_menu function.
    4. Prints eachs row from the sorted list: sort_dict.
    """
    for i in range(len(scores)): 
        scores[i]["total"] = tot(scores[i]["varv1"],scores[i]["varv2"],scores[i]["varv3"])
        scores[i]["average"] = average(scores[i]["varv1"],scores[i]["varv2"],scores[i]["varv3"])        
    sort_dict = sort_menu()
    print("\nResultat")
    print("********")
    print("Namn       1         2        3        Totalt   Genomsnitt\n")
    
    for i in range(len(sort_dict)):
        
        print("{:10}{:10}{:10}{:10}{:10}{:10}".format(sort_dict[i]["name"],sort_dict[i]["varv1"],sort_dict[i]["varv2"],sort_dict[i]["varv3"],sort_dict[i]["total"],sort_dict[i]["average"]))

def sort_menu():
    """
    1. Prints possible sort choices.
    2. Controls that the one you have choosen is between 0-5.
    """
    print("*"*20)
    print("Hur vill du sortera resultaten?")
    print("*"*20)
    print("0) Namn")
    print("1) Varv 1")
    print("2) Varv 2")
    print("3) Varv 3")
    print("4) Totalt")
    print("5) Originalordning")

    sort_choice = None
    
    while True:
        try:
            sort_choice = int(input("Val (0-5): "))
            break
        except: 
            print("Ej giltigt värde, skriv in en siffra!")

    while sort_choice not in (0,1,2,3,4,5):
        print("Ej giltigt värde, skriv in siffra mellan 1-5!")
        sort_choice = int(input("Val (0-5): "))

    return(sort(sort_choice))

def sort(sort_choice):
    """
    Returns a sorted vesion after the choice you have done.
    If your choice were 5 (Original order), it just returns list in its current order.
    """
    sort_dict = None

    if sort_choice == 0:
        sort_dict = sorted(scores, key = lambda i: i['name'])
        return sort_dict
    if sort_choice == 1:
        sort_dict = sorted(scores, key = lambda i: int(i['varv1']))
        return sort_dict
    elif sort_choice == 2:
        sort_dict = sorted(scores, key = lambda i: int(i['varv2']))
        return sort_dict

    elif sort_choice == 3:
        sort_dict = sorted(scores, key = lambda i: int(i['varv3']))
        return sort_dict
        
    elif sort_choice == 4:
        sort_dict = sorted(scores, key = lambda i: int(i['total']))
        return sort_dict 
    
    elif sort_choice == 5:
        return scores 

def delete_score():
    """
    Loop through each row in scores list.
    If the current rows value for "name" is the same as your input (delete_player).
    It removes the whole row for that specific value.
    If the loop completes without match with your input, it prints a error message and return to menu options.
    """
    delete_player = input("Vilken spelare vill du ta bort? ")
    for obj in scores:
        if obj["name"] == delete_player:
            scores.remove(obj)
            print(delete_player + " har raderats")
            return
    print("\n {} hittas ej i resultatlistan, kontrollera om det verkligen finns".format(delete_player))
    print("Var noga med stor och liten bokstav")
           
def tot(a,b,c):
    a = int(a)
    b = int(b)
    c = int(c)
    tot = (a+b+c)
    tot = str(tot)
    return tot

def average(a,b,c):
    a = int(a)
    b = int(b)
    c = int(c)
    average = ((a+b+c)/3)
    average = round(average, 2)
    average = str(average)   
    return average

main()