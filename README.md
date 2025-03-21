Personal Library Manager
A simple and intuitive web-based personal library manager built with Streamlit. This application allows users to add, view, delete, and track books in their personal library. It stores the book details in a local library.json file, making the application lightweight and easy to use.

Features
Add a Book: Allows users to add a new book to their library with the title, author, publishing year, and read status.
View All Books: Displays a list of all books in the library, including their title, author, year of publication, and read status.
Delete a Book: Enables users to delete a book from their library by specifying the title.
Library Statistics: Provides statistics such as the total number of books and the number of books marked as "Read".
Persistent Storage: Books are stored in a library.json file, allowing the library to persist between sessions.
Installation
To run this project on your local machine, follow these steps:

1. Clone the Repository
bash
Copy
git clone https://github.com/yourusername/personal-library-manager.git
cd personal-library-manager
2. Install the Required Packages
Create a virtual environment and install the dependencies using pip.

bash
Copy
# Create virtual environment (optional but recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
3. Run the Application
After installing the dependencies, you can run the app locally using:

bash
Copy
streamlit run app.py
The app will open in your web browser.

Usage
Once the application is running, you will be presented with a simple and intuitive interface that lets you:

Add a Book: Enter the title, author, publication year, and whether you have read the book.
View All Books: View a list of all your books along with their details.
Delete a Book: Enter the title of the book you wish to delete.
Library Statistics: View statistics of your library, such as the total number of books and how many you have read.
File Structure
bash
Copy
/personal-library-manager
    ├── app.py            # The main Streamlit app file
    ├── library.json      # Stores the book data (automatically generated)
    ├── requirements.txt  # Contains the Python dependencies
    └── README.md         # This file
library.json Format
The library.json file stores the book information in the following format:

json
Copy
[
  {
    "title": "Book Title",
    "author": "Author Name",
    "year": 2023,
    "read": true
  }
]
title: The title of the book.
author: The author of the book.
year: The publication year of the book.
read: A boolean indicating whether the user has read the book.
Contributing
We welcome contributions! If you would like to contribute to the development of this project, follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -am 'Add feature').
Push to the branch (git push origin feature-branch).
Create a pull request.
License
This project is open-source and available under the MIT License.

Acknowledgements
This project uses Streamlit for building the web interface.
Thanks to all contributors and the open-source community.
You can copy and paste this README content into a README.md file for your GitHub repository.
