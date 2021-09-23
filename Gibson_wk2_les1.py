## Python Week 2 Lesson 1 Homework
## Drew Gibson
## 22 Sep 2021

## Pr 1
# Create a python script ***file*** (example: Pr1_WK2.py), that when executed prints to screen.

# ```bash
# Hello problem 1 from Week 2 Lesson 1.
# ```

problem_1_string = " \'\'\'bash \
\nHello problem 1 from Week 2 Lesson 1.\
\n\'\'\' "

print(problem_1_string)
## I'm not certain I've understood this question properly, and should have asked for clarification.  My bad!


## Pr 2
#Explain why you should ALWAYS have a .gitignore file in your repo.

# A .gitignore file tells git to not track certain files.  Some files, like generated files or private documentation,
# shouldn't be tracked all the time.  A .gitignore file allows you to specify what files or kinds of files to have git
# version control.


## Pr 3
# Using `open` , create a new file that records user input
# (min 1, max 4 inputs) and then opens that files and APPENDS the following
# "Received User Input"
output_file = open('output_file.txt','a')
num_user_inputs = 1
for i in range(num_user_inputs):
    output_file.write(input("Stuff to write to file: ") + "\n")
output_file.write("Received User Input\n")
output_file.close()


## Pr 4
# Repeat #3 with a `with`
with open("output_file.txt", "a") as output_file:
    num_user_inputs = 1
    for i in range(num_user_inputs):
        output_file.write(input("Stuff to write to file: ") + "\n")
    output_file.write("Received User Input\n")


## Pr 5
# Create a new git repo in github.
# Populate it with typical files and directories (.gitignore and README.md)
# Commit your changes.
# Push it to your repository
