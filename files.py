
my_file = open("data.txt", "r")
file_content = my_file.read()
my_file.close()

print(file_content)

user_name=input("Enter your name: ")
my_file_writhing=open("data.txt","w")
my_file_writhing.write(user_name)

my_file_writhing.close()


