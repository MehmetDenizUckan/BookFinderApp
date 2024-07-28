# Author: Uckan
# -*- coding: utf-8 -*-
import pandas as pd
import random
import LocationVisiauliser
import Handler 
import tkinter as tk


# This is a code that does multiple operations on an excel sheet based on user input
class BookOperation:
    def __init__(self, param) -> None:
        self.param = param
        try:
            self.books = pd.read_excel('Lbrary_v6.xlsx')
            
        except FileNotFoundError as e:
            print(f"Couldn't find the file. Make sure the file is in the same directory as the app. {e}")
            self.books = pd.DataFrame(columns=['İsim', 'Yazar', 'Çeviren', 'Yayınevi', 'Yayın Tarihi', 'Bulunduğu Yer', 'Okunacaklar', 'Basım'])

    def check_if_book_exists(self, param):
      try:
        if param in self.books['İsim'].values:
          return True
        else:
          return False
      except Exception:
        return
    def delete_book(self, param, deletion_input):
        try:
            print(f"Searching for {param}")
            # Check if param is a book name
            if param in self.books['İsim'].values:
                if deletion_input.lower() == 'y':
                    self.books = self.books[self.books['İsim'] != param].reset_index(drop=True)
                    print(f"The book '{param}' has been deleted.")
                    self.write_to_excel()  # Save changes to Excel
                else:
                    print("Quitting the operation")
            else:
                print(f"No book found with the name '{param}'")

        except KeyError:
            print(f"Invalid search parameter: {param}")

    def search_book(self, param):
        try:
            print(f"Searching for {param}")
            # Check if param is a book name
            if param in self.books['İsim'].values:  # Search by 'Title' column
                # Row-based search: filter rows matching the book name
                results = self.books[self.books['İsim'] == param]
                print(results)
                print(f"Location: {results.iloc[0]['Bulunduğu Yer']}")
                location = results.iloc[0]['Bulunduğu Yer']
        
                # Extract letter and number from the location string
                letter = location[0]  # First character is the letter ('G' for example)
                str_number = location[1:]  # Remaining characters are the number as a string ('4' for example)
                number = int(str_number)
                coordinates = Handler.get_coordinates(letter , number)
                x_coordinate  = coordinates[0] 
                y_coordinate = coordinates[1]
                position = LocationVisiauliser.position_arranger(x_coordinate , y_coordinate , letter)
                LocationVisiauliser.merge_images("A-B-C_Lib.jpg", "D-E-F_Lib.jpg", "arrow.png", "glib.jpg" , position)
                return f"Title: {results.iloc[0]['İsim']}\nAuthor: {results.iloc[0]['Yazar']}\nLocation: {results.iloc[0]['Bulunduğu Yer']}\nGenre: {results.iloc[0]['Tür']}"

            elif param in self.books['Yazar'].values:
                results = self.books[self.books['Yazar'] == param]
                print(f"Location: {results.iloc[0]['Bulunduğu Yer']}")
                location = results.iloc[0]['Bulunduğu Yer']
                
                # Extract letter and number from the location string
                letter = location[0]  # First character is the letter ('G' for example)
                str_number = location[1:]  # Remaining characters are the number as a string ('4' for example)
                number = int(str_number)
                coordinates = Handler.get_coordinates(letter , number)
                x_coordinate  = coordinates[0] 
                y_coordinate = coordinates[1]
                position = LocationVisiauliser.position_arranger(x_coordinate , y_coordinate , letter)
                LocationVisiauliser.merge_images("A-B-C_Lib.jpg", "D-E-F_Lib.jpg", "arrow.png", "glib.jpg" , position)

            else:
                print(f"No book found with the name '{param}'")

        except KeyError:
            print(f"Invalid search parameter: {param}")
    
    #def gather_book_info_one_by_one(self):
    #    book_info = {}
    #    book_info["Tür"] = input("Enter Book Type: ")
    #    book_info['İsim'] = input("Enter book name(remember to use uppercase for the first letter): ")
    #    book_info['Yazar'] = input("Enter author name: ")
    #    book_info['Çeviren'] = input("Enter translator: ")
    #    book_info['Yayınevi'] = input("Enter publisher: ")
    #    book_info['Yayın Tarihi'] = input("Enter publication date: ")
    #    book_info['Bulunduğu Yer'] = input("Enter location: ")
    #    book_info['Okunacaklar'] = input("Enter to-read status: ")
    #    book_info['Basım'] = input("Enter edition: ")
    #    return book_info

    def gather_book_info_formatted(self):
        example_format = "Tür, İsim, Yazar, Çeviren, Yayınevi, Yayın Tarihi, Bulunduğu Yer, Okunacaklar, Basım"
        print(f"Enter the book information in the following format:\n{example_format}")
        book_info_str = input("Enter book info: ")
        fields = example_format.split(", ")
        values = book_info_str.split(", ")
        print(fields , values)

        if len(values) != len(fields):
            print("Error: Incorrect number of fields. Please follow the format exactly.")
            return None

        book_info = dict(zip(fields, values))
        return book_info

    def insert_book(self , book_info):
        
        # UNCOMMENT THIS IF YOU WANNA RUN THIS WITHOUT UI
        #book_info = self.gather_book_info_formatted()
        #if book_info is None:
        #    print("Failed to insert the book due to format error.")
        #    return
        
        new_book_df = pd.DataFrame([book_info])  # Create a DataFrame from the book info dictionary
        self.books = pd.concat([self.books, new_book_df], ignore_index=True)  # Concatenate with existing DataFrame
        print(f"The book '{book_info['İsim']}' has been added.")
        self.write_to_excel()  # Save changes to Excel

    def write_to_excel(self):
        try:
            with pd.ExcelWriter('Lbrary_v6.xlsx', engine='openpyxl', mode='w') as writer:
                self.books.to_excel(writer, index=False)
                print("Changes have been saved to 'Lbrary_v6.xlsx.")
        except Exception as e:
            print(f"Failed to write to Excel: {e}")


    def random_recommendation(self):
        randinteger = random.randint(0, len(self.books) - 1)
        book_info = f"\nTitle: {self.books.iloc[randinteger]['İsim']}\nAuthor: {self.books.iloc[randinteger]['Yazar']}\nLocation: {self.books.iloc[randinteger]['Bulunduğu Yer']}\nGenre: {self.books.iloc[randinteger]['Tür']}"
        print(f"Your random recommendation for today is based on number {randinteger + 1}:\n{book_info}")
        
        location = self.books.iloc[randinteger]['Bulunduğu Yer']
        
        # Extract letter and number from the location string
        letter = location[0]  # First character is the letter ('G' for example)
        str_number = location[1:]  # Remaining characters are the number as a string ('4' for example)
        number = int(str_number)
        coordinates = Handler.get_coordinates(letter , number)
        x_coordinate  = coordinates[0] 
        y_coordinate = coordinates[1]
        position = LocationVisiauliser.position_arranger(x_coordinate , y_coordinate , letter)
        print("Loading the image...")
        LocationVisiauliser.merge_images("A-B-C_Lib.jpg", "D-E-F_Lib.jpg", "arrow.png", "glib.jpg" , position)
        return randinteger , book_info 
        
    def change_book_location(self, param, new_location):
        if param in self.books['İsim'].values:  # Search by 'Title' column
            # Row-based search: filter rows matching the book name
            results = self.books[self.books['İsim'] == param]
            print(results)
            print(f"Location: {results.iloc[0]['Bulunduğu Yer']}")
            old_location = results.iloc[0]['Bulunduğu Yer']
                
            book_location = {}
            book_location['Bulunduğu Yer'] = new_location
            new_book_df = pd.DataFrame([book_location])  # Create a DataFrame from the book info dictionary
            self.books = pd.concat([self.books, new_book_df], ignore_index=True)  # Concatenate with existing DataFrame
            f_string = f"The book was in {old_location} now it is in {book_location['Bulunduğu Yer']} changes has been added."
            self.write_to_excel()  # Save changes to Excel
            return f_string
        else:
            print("failed to find the book")
        

def user_interaction():
  """
  IMPORTANT NOTE: This function is redacted and only used for debugging purpuses. Use BookFinderUI.py for operation selection
  
  This function handles user interaction for book operations without the GUI.

  It prompts the user for input, processes it, and calls the appropriate methods of the BookOperation class.

  Returns:
      None
  """
  while True:
    try:
      inpt = input("Input the operation (1: Search, 2: Insert, 3: Delete, 4: change location , r: Random Recommendation, q: Quit): ").strip().lower()
      if inpt == 'q':
        print("Quitting the program.")
        break
      if inpt in ['1', '3', 'r']:
        inpt2 = input("Input the parameter: ").strip()  # Get the input parameter

        # Split input into words and capitalize the first letter of each word (excluding specific conjunctions)
        inpt2_words = inpt2.split()
        baglac = ["ile", "ve" , "veya"]
        inpt2_arranged = ' '.join(word.lower() if word.lower() in baglac else word.capitalize() for word in inpt2_words)
        inpt2 = inpt2_arranged

      else:
        inpt2 = None
    except ValueError:
      print("Invalid input. Please try again.")
      continue  # Go back to the beginning of the loop

    obj = BookOperation(inpt2)

    if inpt == '1':
      obj.search_book(inpt2)
    elif inpt == '2':
      book_info = obj.gather_book_info_formatted()
      obj.insert_book(book_info)
    elif inpt == '3':
      print(f"Are you sure you want to delete:\n{inpt2}\n(y or n)")
      del_inpt = input().strip().lower()
      if del_inpt == 'n':
        print("not deleting anything")
      else:
        obj.delete_book(inpt2, del_inpt)
    elif inpt == '4':
      obj.change_book_location(inpt2)
    elif inpt == 'r':
      obj.random_recommendation()
    else:
      print("Invalid operation. Please enter a valid operation code (1, 2, 3, 4,r, q).")



#user_interaction()