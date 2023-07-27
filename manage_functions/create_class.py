from datetime import datetime
import pyinputplus as pyip

# initializing variables
now = datetime.now()
date = now.strftime('%d-%B-%Y')
class_name = ''
template = ''



def create_class():

    global class_name
    global template
    global date
    
    # ask user for filename
    class_name = pyip.inputStr('Enter the name of the java class without the .java extension: ', blockRegexes = [r'\.java'])
    template = f'''/**********************************************************
@Author:            Fawaaz Kamali Siddiqui                
@Date:              {date}                                
@File:              {class_name}.java                     
@Teacher:           A. Carreiro                           
@Description: 
**********************************************************/



class {class_name} 
{{ 


    public static void main(String[]args)
    {{



    }} // end of main() method
        
        
}} // end of {class_name}.java
'''