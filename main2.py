import os
import heapq

from utils import *
    
def main():
    for file in os.listdir(os.path.join(os.getcwd(), "datasets")):
        if file.endswith('txt'): #leave the last e out for now
            #read in data with python open
            with open(os.path.join("datasets", file)) as datafile:
                line = next(datafile)
                num_books, num_libraries, D = map(int, line.split())

                book_scores = next(datafile)
                book_scores  = list(map(int, book_scores.split()))

                libraries = []
                for i in range(num_libraries):
                    line = next(datafile)
                    num_books, signup_days, bpd = map(int, line.split())
                    line = next(datafile)
                    books_id = list(map(int, line.split()))
                    lib = Library(i, books_id, bpd, signup_days, book_scores)
                    libraries.append(lib)
                i=0
                scanned = set()
                libraries_to_scan = []
                libraries.sort(key=lambda x: x.score2(set())/x.signup_days, reverse=True)
                while D > 0 and libraries!=[]:
                    library = libraries.pop(0)
                    D-=library.signup_days
                    if D>0:
                        will_scan = library.books_to_scan(D, scanned)
                        scanned = scanned.union(set(will_scan))
                        libraries_to_scan.append({"id":library.id, "no_books": len(will_scan), "books_to_scan":will_scan})
                        libraries.sort(key=lambda x: x.score2(scanned)/x.signup_days, reverse=True)
            # wtite to file
                with open('submission/'+file, 'w+') as outputfile: # 'w+' means create file if it doesnt exist
                    #you can only write strings to text file
                    outputfile.write(str(len(libraries_to_scan)))
                    outputfile.write('\n')
                    for lib in libraries_to_scan:
                        outputfile.write(' '.join(map(str,[lib["id"], lib["no_books"]])))
                        outputfile.write('\n')
                        outputfile.write(' '.join(map(str, lib["books_to_scan"])))
                        outputfile.write('\n')

if __name__ == '__main__':
    main()


