#1st part
#putting some functions in separate file called printing_functions.py
#write an import statement at the top of printing_fucntions.py
#modify the file to use imported functions

#2nd part
#using program you wrote that has one function in it store it in a separate file
#import the function into your main program file
#call the function using the approach we saw last class
#for instance import module_name
#import module_name as mn
#from module_name import *  

def print_models(unprinted_designs, completed_models):
    """The purpose of this function is to stimulate the process of creating on 3D printer"""
    """It is simulating printing of each design until there are no left in queue"""
    """Move each design to completed_models after printing"""

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        #simulate creating the 3D print from design
        print(f"Printing models: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """The purpose of this function is to display completed models"""
    print("The following models have been printed")
    for completed_model in completed_models:
        print(f"{completed_model}")
