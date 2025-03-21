import streamlit as st
import json
def load_library():
    try:
        with open('library.json', 'r') as f:
            library = json.load(f)
            for book in library:
                if 'read' not in book:
                    book['read'] = False  
                if 'year' not in book:
                    book['year'] = 2000  
            return library
    except:
        return []
def save_library(library):
    with open('library.json', 'w') as f:
        json.dump(library, f)

def main():
    st.title("Welcome to your Personal Library Manager!")
    st.markdown("---")
    library = load_library()
    option = st.sidebar.selectbox("Choose an option", ["Add a Book", "View All Books", "Delete a Book", "Library Statics", "Exit"])
    if option == "Add a Book":
        st.subheader("Add a New Book")
        title = st.text_input("Write the Title of Your Book")
        author = st.text_input("Who is the Author of Your Book")
        year = st.number_input("Publishing Year of Your Book", min_value=1000, max_value=2025, step=1)
        read = st.radio("Have you read this book?", ["Yes", "No"])

        if st.button("Add Book"):
            if title and author:
                new_book = {"title": title, "author": author, "year": year, "read": read == "Yes"}
                library.append(new_book)
                save_library(library)
                st.success("Book added!")
    elif option == "View All Books":
        st.subheader("All Books")
        if not library:
            st.warning("No books in your library.")
        else:
            for idx, book in enumerate(library, 1):
                status = "Read" if book.get("read", False) else "Unread"  
                year = book.get("year", 2000)  
                st.write(f"{idx}. {book['title']} by {book['author']} ({year}) - {status}")
    elif option == "Delete a Book":
        st.subheader("Delete a Book")
        title = st.text_input("Title to delete")
        if st.button("Delete"):
            library = [book for book in library if book["title"].lower() != title.lower()]
            save_library(library)
            st.success(f"Book '{title}' is Succesfully Removed!")

    elif option == "Library Statics":
        st.subheader("Library Statics")
        total = len(library)
        read_count = sum(1 for book in library if book.get("read", False))  
        st.write(f"Books read: {read_count}")

    elif option == "Exit":
        save_library(library)
        st.write("Goodbye, Thank You!!")
    st.markdown("---")
    st.markdown("Developed By **Shah Mir Usman**")

if __name__ == "__main__":
    main()