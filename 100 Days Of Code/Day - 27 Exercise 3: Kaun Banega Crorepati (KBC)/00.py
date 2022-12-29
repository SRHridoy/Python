'''

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_BOOKS 100
#define MAX_TITLE_LENGTH 50

struct Book {
  int id;
  char title[MAX_TITLE_LENGTH];
  char author[MAX_TITLE_LENGTH];
  int quantity;
};

struct Library {
  struct Book books[MAX_BOOKS];
  int num_books;
};

void print_menu() {
  printf("\nLibrary Management System\n\n");
  printf("1. Add a book\n");
  printf("2. Check out a book\n");
  printf("3. Return a book\n");
  printf("4. List all books\n");
  printf("5. Search for a book\n");
  printf("6. Exit\n\n");
}

void add_book(struct Library *library) {
  if (library->num_books == MAX_BOOKS) {
    printf("Error: Library is full.\n");
    return;
  }

  printf("Enter book ID: ");
  scanf("%d", &library->books[library->num_books].id);
  printf("Enter book title: ");
  scanf("%s", library->books[library->num_books].title);
  printf("Enter book author: ");
  scanf("%s", library->books[library->num_books].author);
  printf("Enter number of copies: ");
  scanf("%d", &library->books[library->num_books].quantity);

  library->num_books++;
}

void check_out_book(struct Library *library) {
  int book_id;
  printf("Enter book ID: ");
  scanf("%d", &book_id);

  for (int i = 0; i < library->num_books; i++) {
    if (library->books[i].id == book_id) {
      if (library->books[i].quantity > 0) {
        library->books[i].quantity--;
        printf("Book checked out successfully.\n");
      } else {
        printf("Error: Book is not available.\n");
      }
      return;
    }
  }

  printf("Error: Book not found.\n");
}

void return_book(struct Library *library) {
  int book_id;
  printf("Enter book ID: ");
  scanf("%d", &book_id);

  for (int i = 0; i < library->num_books; i++) {
    if (library->books[i].id == book_id) {
      library->books[i].quantity++;
      printf("Book returned successfully.\n");
      return;
    }
  }

  printf("Error: Book not found.\n");
}

void list_books(struct Library *library) {
  printf("ID\tTitle\t\t\tAuthor\t\tQuantity\n");
  for (int i = 0; i < library->num_books; i++) {
    printf("

'''