#Dustin Erickson
#12-7-2021
#Final Project


#Importing csv reader and tkinter
import csv
import tkinter as tk

#csv reader operation. Input the saved location of the csv containing the list of movie information. The next comment is the location it is
#saved to my laptop.
#C:\Users\dusti\OneDrive\Documents\Linn Benton Classes\CS 161\IMDB-Movie-Data.csv
csvLocation = input("Please copy the location including name of the csv: ")
file =  open(csvLocation)
csvreader = csv.reader(file)
header = next(csvreader)

#Creating two empty lists. One for titles and one for descriptions.
rowsOfTitles = []
rowsOfDesc = []

#Locating the index for the title and description in the header.
titleIndex = header.index("Title")
descIndex = header.index("Description")

#This itterates through and creates and fills each of the empty lists with all of the values with the corresponding indexes.
for row in csvreader:
    title = row[titleIndex]
    desc = row[descIndex]
    rowsOfTitles.append([title])
    rowsOfDesc.append([desc])

#This closes the csv file.
file.close()
print(rowsOfTitles[0])
print(rowsOfDesc[0])
#Creates two empty lists for the names of movies that are "liked".
matches1 = []
matches2 = []


#I created a class to store the match lists, the name of the lists, and the index value of the name. I attempted to create a function to
#through the names of the movies that will be called via a button in tkinter.
class movieMatcher:
    def __init__(self, matches, NameList, rowsOfDesc, Ivalue):
        self.Ivalue = Ivalue
        self.matches = matches
        self.NameList = NameList
        self.DescList = rowsOfDesc
        self.Name = self.NameList[Ivalue]
        self.Desc = self.DescList[Ivalue]

    def Pass(self):
        self.Ivalue += 1
    
    def Like(self):
        self.Ivalue += 1
        self.matches.append(self.Name)

#Creating instances of the class with the value for their corresponding match list, the list of titles, and their own index value.
Index1 = movieMatcher(matches1, rowsOfTitles, rowsOfDesc, 0)
Index2 = movieMatcher(matches2, rowsOfTitles, rowsOfDesc, 0)

#Creates a tkinter window.
window = tk.Tk()

#This sets the tkinter window information
frame = tk.Frame(master=window, width=1350, height=800)
frame.pack()

#This is a label for the name of the movie on the left.
MovieTitle1 = tk.Label(
    width=55,   #Width of the label
    height=2,   #Hight of the label
    foreground="black",  # Set the text color to white
    background="white",  # Set the background color to black
    text = Index1.Name  #Name of the movie(set to the name in the class)
)

#This is the label for the name of the movie on the right.
MovieTitle2 = tk.Label(
    width=55,   #Width of the label
    height=2,   #Hight of the label
    foreground="black",  # Set the text color to white
    background="white",  # Set the background color to black
    text = Index2.Name  #Name of the movie(set to the name in the class)
)

#This is label for the description of the movie on the left.
MovieDesc1 = tk.Label(
    text = Index1.Desc, #Text for the label, this is set to the index matching the name of the movie.
    width=75,   #Width of the label
    height=6,   #Hight of the label
    wraplength=400,     #This makes it so the text wraps.
    justify = "left",   #This justifies the text to the left.
    foreground="black",  # Set the text color to white
    background="white"  # Set the background color to black
)

#This is the label for the description of the movie on the right.
MovieDesc2 = tk.Label(
    text=rowsOfDesc[0], #Text for the label, this is set to the index matching the name of the movie.
    width=75,   #Width of the label
    height=6,   #Hight of the label
    wraplength=400,     #This makes it so the text wraps.
    justify = "left",   #This justifies the text to the left.
    foreground="black",  # Set the text color to white
    background="white"  # Set the background color to black
)

#This creates the watch button for the first movie
WatchButton1 = tk.Button(
    master=frame,   #This sets the parent of the button to the current frame.
    text="Watch!", #This sets the text of the button to "Watch!"
    width=25,   #Width of the label
    height=5,   #Hight of the label
    bg="green",     #This sets the background to green.
    fg="white",     #Sets the text to white.
    command = Index1.Like()     #Sets the command to the like function in the index1 iteration of the Movie Matcher class.
)
#This creates the pass button for the first movie
PassButton1 = tk.Button(
    master=frame,   #This sets the parent of the button to the current frame.
    text="Pass!",   #This sets the text of the button to "Pass!"
    width=25,   #Width of the label
    height=5,   #Hight of the label
    bg="red",   #This sets the backfround to red.
    fg="white",     #Sets the text to white.
    command=Index1.Pass()   #Sets the command to the Pass function in the index1 iteration of the Movie Matcher class.
)

#This creates the watch button for the second movie
WatchButton2 = tk.Button(
    master=frame,   #This sets the parent of the button to the current frame.
    text="Watch!",  #This sets the text of the button to "Watch!"
    width=25,   #Width of the label
    height=5,   #Hight of the label
    bg="green",     #This sets the background to green.
    fg="white",     #Sets the text to white.
    command= Index2.Like()      #Sets the command to the like function in the index2 iteration of the Movie Matcher class.
)

#This creates the pass button for the first movie
PassButton2 = tk.Button(
    master=frame,   #This sets the parent of the button to the current frame.
    text="Pass!",   #This sets the text of the button to "Pass!"
    width=25,   #Width of the label
    height=5,   #Hight of the label
    bg="red",       #This sets the backfround to red.
    fg="white",     #Sets the text to white.
    command=Index2.Pass()   #Sets the command to the Pass function in the index2 iteration of the Movie Matcher class.
)


    

#Locations of all of the labels and buttons.
WatchButton1.place(x=150,y=600)
PassButton1.place(x=350,y=600)

WatchButton2.place(x=850,y=600)
PassButton2.place(x=1050,y=600)

MovieTitle1.place(x=150,y=300)
MovieTitle2.place(x=850,y=300)

MovieDesc1.place(x=75,y=400)
MovieDesc2.place(x=750,y=400)


#Creates a basic function to test if their is a match within two lists
def intersection(likes1, likes2):
    matches = [value for value in likes1 if value in likes2]
    return matches
#Calls the function and determines the match between them. This will continue to run until a match has been made.
matched = False
while matched == False:
    match = intersection(matches1,matches2)
    if isinstance(match, list):
        matched = True

#Prints match
print(match)




#Sets the window to loop until exited.
window.mainloop()


