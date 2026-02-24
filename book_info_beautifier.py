book_info = "john doe ; the art of programming ; 2020 ; ISN 978-3-16-148410-0 ; 350 ; 2500"

components = book_info.split(" ; ")

print(components)

author, book_title, year_published, isbn, no_of_pages, cost = components
print("author:", author)
print("book_title:", book_title)
print("year_published:", year_published)
print("isbn:", isbn)
print("no_of_pages:", no_of_pages)
print("cost:", cost)

author = author.title()
book_title = book_title.strip().title()
isbn = isbn.replace("ISN", "ISBN")
rounded_up = round(float(cost), 2)
cost = f"₦{rounded_up}"
# formatted_book_info = author ; book_title ; year_published ; isbn ; no_of_pages ; cost
print("formatted_book_info", formatted_book_info)
formatted_book_info = f"""The book {book_title} was written by {author} and published in {year_published}.
# It has {no_of_pages} pages and {isbn} and costs {cost}."""
# print(formatted_book_info)