import os
import heapq

class Book(object):
    def __init__(self, book_id, book_scores):
        self.id = book_id
        self.score = book_scores[self.id]
    def __repr__(self):
        return str(self.id)

class Library(object):
    def __init__(self, lib_id, books_id, books_per_day, signup_days, book_scores):
        self.books = []#[Book(i, book_scores) for i in books_id]
        for i in books_id:
            book = Book(i, book_scores)
            heapq.heappush(self.books, (-book.score, book))
        self.id = lib_id
        self.books_per_day = books_per_day
        self.signup_days = signup_days
        
        
    def __repr__(self):
        return str(self.id)
    
    def score(self, scanned):
        score = 0
        for _, book in self.books:
            score+=book.score
        return score
    
    def score2(self, scanned):
        score = 0
        self.books = list(set(self.books)-set(scanned))
        for _, book in self.books:
            score+=book.score
        return score
    
    def books_to_scan(self, days_left, scanned):
        no_books = days_left*self.books_per_day
        books=[]
        while len(books)<no_books and self.books!=[]:
            _, book = heapq.heappop(self.books)
            if book not in scanned:
                books.append(book)
        return books 