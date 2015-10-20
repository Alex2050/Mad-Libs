# List number of blanks to answer (used for while loop)
blank=['__1__','__2__','__3__','__4__']

#Content and answers for each difficulty level
easy_content = " A __1__ can go through each element in a list. In order to __1__,however, you must first setup some __2__ to hold the current __3__ of the list and the current count.The logic is that if the __3__ number is less than the length of our list, then we can safely say that whenever we access the list with __3__, we will never create an error and will be able to access __4__ in the list with the number __3__."
easy_answer = ['loop','variables','index','elements']

medium_content = " __1__ statements control which code gets executed when. __2__ loops make code that persons the same task many times.We can use a __3__ to create a name and then reference the name in our __1__ statement and __2__ loop. We can also assign a __4__ to a __3__. A __4__ is a sequence of characters between single quotes (or double quotes)"
medium_answer = ['If','While','variable','string']

hard_content = "Similar to how strings are sequences of characters, __1__ are sequences of anything (incl. numbers & characters)! __1__ support __2__, so we can change the value of a list after we've created it. __1__ are mutable data structures, so they can change their value without an __3__ statement. As a result, two identifiers can refer to the same variable (and therefore value), this is known as __4__."
hard_answer = ['lists','mutation','assignment','alias']

#Globally defining difficulty variable
difficulty = raw_input(" Hello and welcome to a MadLibs game that tests your programming vocabulary!"+"\n Do you want to play easy, medium, or hard?")

# Replaces each blank with the appropriate answer. "Replace_level" function arguments (blank, content, and answers) derived from difficulty selection in "select_difficulty" function 
def replace_level(blank,content,answers):
    print content
    i=0 #counter for blanks and for answers
    while i<4:
        answer=raw_input("\n" + "What should go in blank "+blank[i]+"?") # question written directly inside of raw input instead of separately printed
        if answer == answers[i]:
            content=content.replace(blank[i],answers[i]) #replaces correctly answered words in the content
            print content
            i=i+1
        else:
            print "Incorrect"
    return "\n" + "Great Job! You passed " + difficulty +" difficulty!"

# User selects difficulty level and based on difficulty selection define content and answers to be put into replace_level function
def select_difficulty(difficulty): 
    if difficulty == "easy":
        difficulty=replace_level(blank,easy_content,easy_answer)
        return difficulty #Point at which the function returns the results of the calling function
    if difficulty == "medium":
        difficulty=replace_level(blank,medium_content,medium_answer)
        return difficulty #Point at which the function returns the results of the calling function
    if difficulty == "hard":
        difficulty=replace_level(blank,hard_content,hard_answer)
        return difficulty #Point at which the function returns the results of the calling function
    else:
        return "Not a correct input. Please type easy, medium, or hard."
    return

print select_difficulty(difficulty)
