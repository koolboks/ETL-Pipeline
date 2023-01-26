

_Author_ = "Ayobami Akinlolu-ojo"

"..............................................................................."
#Importing the use Libraries

"Import Pony Orm For committing data into the database"
from pony.orm import *

" Import csv module  to Read the User_data.csv"
import csv

"import Json module to Read the User_data.json"
import json


"Import xml module to Read the User_data.xml"
import xml.etree.ElementTree as ET

"..............................................................................."


"Display Infomation on the console "
def display_information():
    dip_ = "\033[33m" + "ETL SOFTWARE DEVELOPMENT \n" + "\033[0m"
    author= "\033[32m" + _Author_+"\n" + "\033[0m"
    student_id ="\033[33m" + "Student_bi32oj\n"+ "\033[0m"
    email_ = "\033[34m"+"bi32oj@student.sunderland.ac.uk\n"+ "\033[0m"

    red = "\033[31m" + "████████████████████████████████████████████████████████████████"*2 + "\033[0m"
    start = f"""
            ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

                                                     TITLE: .....🌹 {dip_}
                                                     BY: .....   🌹 {author}
                                                     ID: .....   🌹 {student_id}
                                                     EMAIL: .....🌹 {email_}
            {red}

    """
    starts = "\033[34m" + start + "\033[0m"
    print(starts)


"Execute Function "
display_information()




#reading the csv file
csv_data = []
"..............................................................................."
print("."*100, "\n", "\033[32m" +"1. Reading CSV Data set into a dictionary data type"+"\033[0m","\n")
import time
time.sleep(2)
with open("user_data.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        csv_data.append(row)

#reading the json file
"..............................................................................."
print("."*100, "\n", "\033[32m" +"2. Reading JSON Data set into a dictionary data type"+"\033[0m","\n")
import time
time.sleep(2)
with open("user_data.json") as json_file:
    json_data = json.load(json_file)

#reading the xml file
"..............................................................................."
print("."*100, "\n", "\033[32m" +"3. Reading XML Data set into a dictionary data type"+"\033[0m","\n")
import time
time.sleep(2)

xml_data = []
tree = ET.parse('user_data.xml')
root = tree.getroot()
for i in root:
    # print(dict(i.attrib))
    xml_data.append(dict(i.attrib))


"Read the text User_info"
"..............................................................................."
print("."*100, "\n", "\033[32m" +"4. Reading TEXT Data set into a dictionary data type"+"\033[0m","\n")
import time
time.sleep(2)

text_datas = []
print("Opening User_data.text file>>\n")
with open("user_data.txt", "r") as f:

    "Read all the data line by line "
    reader = f.readlines()

    for read_text in reader:
        text_datas.append(read_text)


new_data = []
"""
# We are going ot filter the datas to make sure we get the perfect matches in iteration
# It might be difficult to find matches and merges easily
# Without using some data structure Algorithm
# We need to filter the Sex and the Age of the csv ann the XmL data first
# We Filter the new_data and the json

"""


"""
since the Json and the xml user data are in thesame format
we will merge it first

"""

"..............................................................................."
print("."*100, "\n", "\033[32m" +"Looking for Matches in Json and Xml Data set"+"\033[0m","\n")
import time
time.sleep(2)

"Create list of merge data from the json and Xml user datas"
json_xml_datas = []

"Access the xml user datas"
print("Merging New data_set>>>>>>>\n ")
for xml in xml_data:
    xml = {k.lower(): v for k, v in xml.items()}

    "Access the json user datas"
    # print("Checking  json_data")
    for json in json_data:

        "Turn the Key values into a lower case for perfect matches"
        json = {k.lower(): v for k, v in json.items()}



        " Check if the first name and the last name of the users datas macthes"
        if xml["firstname"] == json["firstname"] and xml["lastname"] == json["lastname"] and int(xml['age'])==json['age']:


            " if they matches then merge the two data togther with Dictionary comprehension Library"
            data = {**xml | json}

            " Append the Result for further analysis and algorithm"
            json_xml_datas.append(data)


"""
We look for matches User details in the Csv_user data with the json_xml_data
"""


"..............................................................................."
print("."*100, "\n", "\033[36m" +"Looking for Matches in csv and json_xml_data Data set"+"\033[0m","\n")
import time
time.sleep(2)

"create a list of new user_datas"
new_user_datas = []

"Access csv user data info the iterating on the data"

print("Merging New data_set>>>>>>>\n")
for csv_ in csv_data[0:]:

    """
    unlike json and xml , csv datas consist of Keys that are unequal 
    we will use algorithm to clean the datas to make sure they matches and merge the data together
    """

    " Make all the keys of the csv_ data to be in lower case"
    csv_ = {k.lower(): v for k, v in csv_.items()}

    "Access the list of Dictonary in the json_xml_data"
    # print("Accessing json_xml_data>>>\n")
    for json_xml_data in json_xml_datas[0:]:


        "Turn the Key values into a lower case for perfect matches"
        json_xml_data = {k.lower(): v for k, v in json_xml_data.items()}



        " Check if the first name and the last name of the users datas macthes "
        if json_xml_data["firstname"] == csv_["first name"] and json_xml_data["lastname"] == csv_["second name"] and str(json_xml_data['age'])==csv_["age (years)"]:

            " if they matches then merge the two data together with Dictionary unpack operator Library"
            data_ = {**csv_ | json_xml_data}

            """
            Since the Key of the Csv file and the json_xml_data does not matches we delete
            the key in the json_xml_datas in other to have consice info
            """

            del data_["firstname"], data_["lastname"]

            """
            We still hvae duplicated Age the New data because the Age in the Csv data is not
            thesame with the Age key in the json_xml_datas we clean it up by removing the inconsitency
            """


            "We remove the Age from the merge data since the Age in json_xml is not sync with Csv_ "
            del data_["age"]

            " We are ready to commit to a database we titled the Keys of the data and append into a list"

            "use the title built-in to capitalise the key of the Data_"
            data_= {k.title():v for k,v in data_.items()}

            "append the datas into a new variable"
            new_user_datas.append(data_)




"We insert the Business Correspodence by name tags"
user_name_1 =["Shane", "Chambers"]
user_name_2 = "Lane"
user_name_3 = ["Suzanne","Wright"]
user_name_4= 'Hannah'
dict_text_data ={}

#Loop through the text file

for line, text_data in enumerate(text_datas):
    dict_text_data[line] = text_data

"..............................................................................."
print("."*100, "\n", "\033[36m" +"List Of User Name Found in Text Data Set","\n")
import time
time.sleep(2)


for line,  new_user_data in enumerate(new_user_datas):
    if  new_user_data["First Name"] == user_name_1[0] and  new_user_data["Second Name"] == user_name_1[1]:
        if len(dict_text_data[0])>255:
            new_user_data["User_info"] =dict_text_data[0][0:255]
            print("line >>:", line, "Firstname:", user_name_1[0], "Last Name:",  user_name_1[1],"\n" )

    elif new_user_data["First Name"] == user_name_2 or new_user_data["Second Name"] == user_name_2:

        if len(dict_text_data[1]) > 255:
            new_user_data["User_info"] = dict_text_data[1][0:225]
            print("line >>:", line, "Name:", (user_name_2), "\n")

    elif new_user_data["First Name"] == user_name_3[0] and  new_user_data["Second Name"] == user_name_3[1]:

        print("line >>:", line, "First Name:",  user_name_3[0],"Last Name:", user_name_3[1], "\n")
        new_user_data["User_info"] = dict_text_data[2]

    elif new_user_data["First Name"] == user_name_4 or new_user_data["Second Name"] == user_name_4:
        if len(dict_text_data[3]) > 255:
            print("line >>:", line, "Name:", user_name_4,"\n")
            new_user_data["User_info"] = dict_text_data[3][0:255]

    else:
        new_user_data["User_info"] = "N/A"


" we use dict to csv library to easily write on the Csv"

# fieldnames should match the keys of your dictionary
fieldnames = list(new_user_datas[0].keys()) + ["Debt"]

# File name to save the CSV
filename = "output.csv"
print(f"commiting data into a csv file for check\nYou can check {filename} for Further details\n")
with open(filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for data in new_user_datas:

        #Convert the nested dictionary into String to be writable on the sheet
        if "Debt" in data and isinstance(data["Debt"], dict):

            data['Debt'] = str(data["Debt"])

        # Writing to CSV

        writer.writerow(data)

def row_commiter():
    # Create a new dictionary with the keys in title case
    print(
        "total row to commit is 1000 rows please not that the total time depends on the server since we are user Pony ORM\n")
    for line, new_user_data in enumerate(new_user_datas):
        # print(new_user_data)
        print("\033[33m" + "Loading Data Row"+"\033[0m" , line + 1)

        if new_user_data["Dependants"] == "":
            new_user_data["Dependants"] = "N/A"

        "Note that debt only appears 158 time in user_data details"
        if "Debt" in new_user_data and isinstance(new_user_data["Debt"], dict):
            # print("new_user_data", new_user_data["Debt"])

            data = Data(first_name=new_user_data['First Name'], second_name=new_user_data['Second Name'],
                        age_years=new_user_data['Age (Years)'],
                        sex=new_user_data['Sex'], vehicle_make=new_user_data['Vehicle Make'],
                        vehicle_model=new_user_data['Vehicle Model'],
                        vehicle_year=new_user_data['Vehicle Year'], vehicle_type=new_user_data['Vehicle Type'],
                        retired=new_user_data['Retired'],
                        dependants=new_user_data['Dependants'], marital_status=new_user_data['Marital_Status'],
                        salary=new_user_data['Salary'],
                        pension=new_user_data['Pension'], company=new_user_data['Company'],
                        commute_distance=new_user_data['Commute_Distance'],
                        address_postcode=new_user_data['Address_Postcode'], iban=new_user_data['Iban'],
                        credit_card_number=new_user_data['Credit_Card_Number'],
                        credit_card_security_code=new_user_data['Credit_Card_Security_Code'],
                        credit_card_start_date=new_user_data['Credit_Card_Start_Date'],
                        credit_card_end_date=new_user_data['Credit_Card_End_Date'],
                        address_main=new_user_data['Address_Main'],
                        address_city=new_user_data['Address_City'],
                        business_coresspondence=new_user_data["User_info"],
                        debt=str(new_user_data['Debt']))

            commit()

        data = Data(first_name=new_user_data['First Name'], second_name=new_user_data['Second Name'],
                    age_years=new_user_data['Age (Years)'],
                    sex=new_user_data['Sex'], vehicle_make=new_user_data['Vehicle Make'],
                    vehicle_model=new_user_data['Vehicle Model'],
                    vehicle_year=new_user_data['Vehicle Year'], vehicle_type=new_user_data['Vehicle Type'],
                    retired=new_user_data['Retired'],
                    dependants=new_user_data['Dependants'], marital_status=new_user_data['Marital_Status'],
                    salary=new_user_data['Salary'],
                    pension=new_user_data['Pension'], company=new_user_data['Company'],
                    commute_distance=new_user_data['Commute_Distance'],
                    address_postcode=new_user_data['Address_Postcode'], iban=new_user_data['Iban'],
                    credit_card_number=new_user_data['Credit_Card_Number'],
                    credit_card_security_code=new_user_data['Credit_Card_Security_Code'],
                    credit_card_start_date=new_user_data['Credit_Card_Start_Date'],
                    credit_card_end_date=new_user_data['Credit_Card_End_Date'],
                    address_main=new_user_data['Address_Main'],
                    address_city=new_user_data['Address_City'],
                    business_coresspondence=new_user_data["User_info"], debt='N/A')
        commit()
"..............................................................................."
print("."*100, "\n", "\033[36m" +"Creating Pony ORM entities"+"\033[0m","\n")
import time
time.sleep(2)

# "We start the Pony data base "

db = Database()

class Data(db.Entity):



    first_name = Required(str)
    second_name = Required(str)
    age_years = Required(str)
    sex = Required(str)
    vehicle_make = Required(str)
    vehicle_model = Required(str)
    vehicle_year = Required(str)
    vehicle_type = Required(str)
    retired = Required(str)
    dependants = Required(str)
    marital_status = Required(str)
    salary = Required(str)
    pension = Required(str)
    company = Required(str)
    commute_distance = Required(str)
    address_postcode = Required(str)
    iban = Required(str)
    credit_card_number = Required(str)
    credit_card_security_code = Required(str)
    credit_card_start_date = Required(str)
    credit_card_end_date = Required(str)
    address_main = Required(str)
    address_city = Required(str)
    business_coresspondence=Required(str)
    debt = Required(str)


if __name__ == "__main__":

    "connect to my Sql"
    "..............................................................................."
    print("." * 100, "\n", "\033[36m" + "Connecting to my Sql Database with following Credentials\n\n1. provider= mysql, \n\n2. host= europa.ashley.work, \n\n3. user= student_bi32oj, \n\n4. passwd= iE93F2@8EhM@1zhD&u9M@K, \n\n5. db= student_bi32oj \n" + "\033[0m", "\n")
    import time

    time.sleep(2)
    print()
    db.bind(provider='mysql', host='europa.ashley.work', user='student_bi32oj', passwd='iE93F2@8EhM@1zhD&u9M@K', db='student_bi32oj')
    # Generate the mapping for the table
    # create_tables=True creates the table if it does not exist
    db.generate_mapping(create_tables=True)


    try:
        with db_session:

         number_of_rows = count(d for d in Data)
         print(number_of_rows)
         if number_of_rows >= 1000:
             print(f"The Total number of dataset in the table  is {number_of_rows}\n\nThis Script will stop For Now")
             # print("To delete please go to line ")
             in_ = input(" Do you want to delete it before Writing on it? [YES/NO/STOP]\n")
             if in_.lower() == "yes":
                 print(f"please wait while I Delete total record of  {number_of_rows} data from student_bi28ah database\nto re-write on it"  )
                 delete(d for d in Data)
                    # Commit the transaction
                 commit()
                 print("delete completed\n")
             elif in_.lower() == "no":
                 row_commiter()
             else:
                 pass
         else:
             row_commiter()

    except Exception as e:
       # We roll back effects after Error handler
        print(f"This Error is because of {e}")

        rollback()




