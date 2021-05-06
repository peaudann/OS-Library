import os

# Gather file name and location from user
def file_info():
  print("WARNING: If a text file exists with the name you enter it will be overwritten.")
  file_name = input("What would you like to name the file: ")
  file_location = input("Where would you like to save the file(ex. C:\*insert folder path here*): ")

# Join the file name with the chosen path using os library
  complete_path = os.path.join(file_location, file_name + ".txt")

  # Return the path and file name created
  return complete_path


# Write the information to the file the user created
def write_file():
  # Grab information from file_info()
  user_file = file_info()

  # Create list to store user information
  user_info = []
  print("Enter your name, address and phone number.")
  user_name = input("Name: ")
  user_addy = input("Address: ")
  user_phone = input("Phone: ")

  # Append information to list
  user_info.append(user_name)
  user_info.append(user_addy)
  user_info.append(user_phone)

  # Open file created by user in write mode ("w") and write each string entered to the file separated by a comma
  with open(user_file, "w") as f:
    f.writelines(", ".join(str(data) for data in user_info))

    print("\nHere is the information you have entered: \n")

  # Open file created, written to and read ("r") that out to user as confirmation of entry
  with open(user_file, "r") as f:
    print(f.read())


def main():
  print("Hello, collecting information that will be sold to advertisers now...\n")
  write_file()


if __name__  == "__main__":
  main()
