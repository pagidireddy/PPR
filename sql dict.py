import mysql.connector

con = mysql.connector.connect(
username = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)
cursor = con.cursor()
word = input("Enter the word: ")
search = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'"%word)

results = cursor.fetchall()

if results:
    for result in results:
        print(result[0])
else:
    print("no word found")