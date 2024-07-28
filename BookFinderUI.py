# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox, simpledialog
from BookFinder import BookOperation  # Import the class directly

class BookFinderUI:
    def __init__(self, root):
        self.book_operation = BookOperation("your_required_parameter")  # Replace with actual parameter value
        
        self.root = root
        
        self.root.title("BookFinder")
        
        self.root.geometry("500x500+50+50")
        
        self.iconpath = "app_logo.ico"
        
        icon = tk.PhotoImage(file=self.iconpath)
        
        root.iconphoto(False, icon)

        self.create_widgets()

    def create_widgets(self):
        # Label with heading text
        baslik_metin = "Welcome to BookFinder! Please choose your operation:"
        label = tk.Label(self.root, text=baslik_metin, width=50)
        label.pack(side="top")

        # Search button
        search_button = tk.Button(self.root, text="Search", padx=16, pady=8, width=20, cursor='hand2', command=self.search_book)  # Raised border
        search_button.pack(pady=5)

        # Insert button
        insert_button = tk.Button(self.root, text="Insert", padx=16, pady=8, width=20, cursor='hand2', command=self.insert_book)
        insert_button.pack(pady=5)

        # Delete button
        delete_button = tk.Button(self.root, text="Delete", padx=16, pady=8, width=20, cursor='hand2', command=self.delete_book)
        delete_button.pack(pady=5)

        # Change Location button
        change_location_button = tk.Button(self.root, text="Change Location", padx=16, pady=8, width=20, cursor='hand2', command=self.change_location)
        change_location_button.pack(pady=5)

        # Random Recommendation button
        random_button = tk.Button(self.root, text="Random Recommendation", padx=16, pady=8, width=20, cursor='hand2', command=self.random_recommendation)
        random_button.pack(pady=5)

        # Quit Button
        quit_button = tk.Button(self.root, text="Return to Desktop", padx=16, pady=8, width=20, cursor='hand2', command=self.quit_program)
        quit_button.pack(pady=5)

        # version 
        version = tk.Label(self.root, text="version : 1.00")
        version.pack(side="bottom")
        
    def get_utf8_input(self, title, prompt):
        """
        This method wraps simpledialog.askstring to ensure it properly handles UTF-8 input
        and performs additional processing on the input.

        Args:
            title: The title for the messagebox dialog.
            prompt: The prompt message to display to the user.

        Returns:
            The processed and UTF-8 encoded string, or None if the user cancels.
        """

        icelandic_to_turkish = {
            'ý': 'ı',
            'ð': 'ğ',
            'Ð': 'Ğ',
            'þ': 'ş',
            'Þ': 'Ş'
        }

        input_str = simpledialog.askstring(title, prompt)
        if input_str:
            # Convert Icelandic letters to Turkish letters
            converted_input = ''.join(icelandic_to_turkish.get(char, char) for char in input_str)

            # Process the input 
            input_term = converted_input.strip()
            if input_term:
                # Split input into words and capitalize the first letter of each word (excluding specific conjunctions)
                search_term_words = input_term.split()
                baglac = ["ile", "ve", "veya"]
                search_term_arranged = ' '.join(word.lower() if word.lower() in baglac else word.capitalize() for word in search_term_words)
                input_term = search_term_arranged

            return input_term.encode('utf-8').decode('utf-8')  # Encode and return
        return None


    def search_book(self):
        try:
            search_term = self.get_utf8_input("Search", "Enter book name or author:")
        except Exception as e:
            messagebox.showerror("An Error Occurred", str(e))
            return

        if self.book_operation.check_if_book_exists(search_term):
            results = self.book_operation.search_book(search_term)
            messagebox.showinfo("Search Results", f": {results}")        
        else:
            messagebox.showinfo("No Results", f"No books found for '{search_term}'.")
                
    def gather_book_info_messagebox(self):
        """
        Gathers book information from user input using separate messagebox prompts.

        Returns:
            A dictionary containing the collected book information, or None if the user cancels.
        """

        book_info = {}  # Empty dictionary to store book information

        # Prompt for each book information field
        labels = [
            "Tür:",
            "İsim:",
            "Yazar:",
            "Çeviren:",
            "Yayınevi:",
            "Yayın Tarihi:",
            "Bulunduğu Yer:",
            "Baskı:"
        ]

        for label_text in labels:
            # Use simpledialog.askstring for each field input
            value = self.get_utf8_input("Book Information", label_text)
            if value is None:  # User cancelled any individual prompt
                return None
            book_info[label_text.rstrip(":")] = value.strip()

        return book_info


    def insert_book(self):
        book_info = self.gather_book_info_messagebox()

        if not book_info:
            messagebox.showerror("Error", "Failed to insert the book.")
            return

        self.book_operation.insert_book(book_info)
        messagebox.showinfo("Success", f"The book '{book_info['İsim']}' has been added.")

    def delete_book(self):
        search_term = self.get_utf8_input("Delete", "Enter book name:")
        books_existance = self.book_operation.check_if_book_exists(search_term)

        
        if books_existance:
            deletion_input = self.get_utf8_input("Delete", f"Are you sure you want to delete '{search_term}'? (y/n)")
            if deletion_input.lower() == 'y':
                self.book_operation.delete_book(search_term, deletion_input)
                messagebox.showinfo("Success", f"The book '{search_term}' has been deleted.")
        else:
            messagebox.showerror("Fail", "The book doesnt exists")

    def change_location(self):
        search_term = self.get_utf8_input("Change Location", "Enter book name:")
        books_existance = self.book_operation.check_if_book_exists(search_term)

        if books_existance:
            location_term = self.get_utf8_input("Change Location", "Enter the new location")
            info =self.book_operation.change_book_location(search_term, location_term)
            messagebox.showinfo("Success", info)
        else:
            messagebox.showerror("Fail", "The book doesnt exists")

            

    def random_recommendation(self):
        random_rec_number, book_info = self.book_operation.random_recommendation()
        messagebox.showinfo("Recommendation", f"Your recommendation is based on number {random_rec_number}:\n{book_info}")

    def quit_program(self):
        """This function destroys the main window, effectively closing the program."""
        self.root.destroy()
        

def main():
    root = tk.Tk()
    app = BookFinderUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
