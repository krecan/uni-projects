# -----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n9954953
#    Student name: Lucas Wickham
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
# --------------------------------------------------------------------#



# -----Assignment Description-----------------------------------------#
#
#  Online Shopper
#
#  In this assignment you will combine your knowledge of HTMl/XML
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application for aggregating product data published by a variety of
#  online shops.  See the instruction sheet accompanying this file
#  for full details.
#
# --------------------------------------------------------------------#



# -----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these
# functions only.  Note that not all of these functions are
# needed to successfully complete this assignment.

# The function for opening a web document given its URL.
# (You WILL need to use this function in your solution.)
from urllib import urlopen

# Import the standard Tkinter functions. (You WILL need to use
# these functions in your solution.)
from Tkinter import *

# Functions for finding all occurrences of a pattern
# defined via a regular expression.  (You do NOT need to
# use these functions in your solution, although you will find
# it difficult to produce a robust solution without using
# regular expressions.)
from re import findall, finditer

# Import the standard SQLite functions just in case they're
# needed.
from sqlite3 import *

#
# --------------------------------------------------------------------#



# -----Student's Solution---------------------------------------------#

# Name of the invoice file. To simplify marking, your program should
# produce its results using this file name.
file_name = 'invoice.html'


# Define functions
# Print invoice to HTML file
def print_invoice():
    # Set cursor to "loading"
    window.config(cursor="wait")

    # Get item quantities
    cat1_qty = int(category1_sbx.get())
    cat2_qty = int(category2_sbx.get())
    cat3_qty = int(category3_sbx.get())
    cat4_qty = int(category4_sbx.get())

    # Download RSS feeds
    progress.set("Downloading Fashion Jewellery")
    window.update_idletasks()
    cat1_page = urlopen("http://india-shopping.khazano.com/rss/catalog/category/cid/18/store_id/1/")
    progress.set("Downloading Car DVR")
    window.update_idletasks()
    cat2_page = urlopen("https://www.seicane.com/rss/catalog/category/cid/158/store_id/1/")
    progress.set("Downloading Purse")
    window.update_idletasks()
    cat3_page = urlopen("https://www.etsy.com/shop/oktak/rss")
    progress.set("Downloading Surveillance Systems")
    window.update_idletasks()
    cat4_page = urlopen("https://www.crimezappers.com/rss/catalog/category/cid/199/store_id/1/")

    # Read pages to variables
    cat1_code = cat1_page.read()
    cat2_code = cat2_page.read()
    cat3_code = cat3_page.read()
    cat4_code = cat4_page.read()

    # Close pages
    cat1_page.close()
    cat2_page.close()
    cat3_page.close()
    cat4_page.close()

    # Remove line breaks
    cat1_code = cat1_code.replace("\n", "")
    cat2_code = cat2_code.replace("\n", "")
    cat3_code = cat3_code.replace("\n", "")
    cat4_code = cat4_code.replace("\n", "")

    # Open/create invoice file
    invoice_file = open(file_name, "w")

    # Write header to file
    invoice_file.write('''
    <link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.indigo-orange.min.css" />\n
    <style>
    img:not(.shopimage){width: 200px; height: auto;} 
    img.shopimage{width: 560px; height: auto;} 
    main{width: 100%; max-width: 720px; margin: 0 auto;}
    </style>\n
    <title>Online Shopper invoice</title>\n
    <main>\n
    <h1>Online Shopper Invoice</h1>\n
    <img class="shopimage" src="https://cdn.pixabay.com/photo/2016/12/24/15/23/online-shopping-1929002_640.png"<br>\n''')

    if check_save_order.get() == 1:
        # Create connection to DB
        connection = connect(database="shopping_trolley.db")

        # Get a pointer to the DB
        shopping_trolley_db = connection.cursor()

        # Reset DB
        shopping_trolley_db.execute("DELETE FROM Purchases")

    # Initialise total variable
    total = 0.0

    # Initialise end point variables
    name_ep = 0
    image_ep = 0
    price_ep = 0

    # Add info to file for category 1
    for item in range(cat1_qty):
        name_sp = cat1_code.find("<item>      <title><![CDATA[", name_ep) + 28
        name_ep = cat1_code.find("]]></title>", name_sp + 1)
        name = cat1_code[name_sp: name_ep]
        invoice_file.write("<h4>" + name + "</h4><br>\n")

        image_sp = cat1_code.find('<img src="', image_ep) + 10
        image_ep = cat1_code.find('"', image_sp + 1)
        invoice_file.write('<img src="' + cat1_code[image_sp: image_ep] + '"><br>\n')

        price_sp = cat1_code.find('<span class="price">', price_ep) + 24
        price_ep = cat1_code.find('</span>', price_sp + 1)
        converted_price = round((float(cat1_code[price_sp: price_ep]) * 0.02), 2)
        invoice_file.write('<h5>Price: AU$' + "{0:.2f}".format(converted_price) + '</h5><br>\n')
        total = total + converted_price

        # Save values to DB
        if check_save_order.get() == 1:
            shopping_trolley_db.execute(
                "INSERT INTO Purchases VALUES ('" + name + "', '" + ('{0:.2f}'.format(converted_price)) + "')")

    # Reset end point variables
    name_ep = 0
    image_ep = 0
    price_ep = 0

    # Add info to file for category 2
    for item in range(cat2_qty):
        name_sp = cat2_code.find("<item>      <title><![CDATA[", name_ep) + 28
        name_ep = cat2_code.find("]]></title>", name_sp + 1)
        name = cat2_code[name_sp: name_ep]
        invoice_file.write("<h4>" + name + "</h4><br>\n")

        image_sp = cat2_code.find('<img src="', image_ep) + 10
        image_ep = cat2_code.find('"', image_sp + 1)
        invoice_file.write('<img src="' + cat2_code[image_sp: image_ep] + '"><br>\n')

        price_sp = cat2_code.find('<span class="price">', price_ep) + 23
        price_ep = cat2_code.find('</span>', price_sp + 1)
        converted_price = round((float((cat2_code[price_sp: price_ep]).replace(",", "")) * 1.34), 2)
        invoice_file.write('<h5>Price: AU$' + "{0:.2f}".format(converted_price) + '</h5><br>\n')
        total = total + converted_price

        # Save values to DB
        if check_save_order.get() == 1:
            shopping_trolley_db.execute(
                "INSERT INTO Purchases VALUES ('" + name + "', '" + ('{0:.2f}'.format(converted_price)) + "')")

    # Reset end point variables
    name_ep = 0
    image_ep = 0
    price_ep = 0

    # Add info to file for category 3
    for item in range(cat3_qty):
        name_sp = cat3_code.find("<item>        <title>", name_ep) + 21
        name_ep = cat3_code.find(" by oktak</title>", name_sp + 1)
        name = cat3_code[name_sp: name_ep]
        invoice_file.write("<h4>" + name + "</h4><br>\n")

        image_sp = cat3_code.find('image&quot;&gt;&lt;img src=&quot;', image_ep) + 33
        image_ep = cat3_code.find('&quot;', image_sp + 1)
        invoice_file.write('<img src="' + cat3_code[image_sp: image_ep] + '"><br>\n')

        price_sp = cat3_code.find('class=&quot;price&quot;&gt;', price_ep) + 27
        price_ep = cat3_code.find(' USD&lt;', price_sp + 1)
        converted_price = round((float((cat3_code[price_sp: price_ep]).replace(",", "")) * 1.34), 2)
        invoice_file.write('<h5>Price: AU$' + "{0:.2f}".format(converted_price) + '</h5><br>\n')
        total = total + converted_price

        # Save values to DB
        if check_save_order.get() == 1:
            shopping_trolley_db.execute(
                "INSERT INTO Purchases VALUES ('" + name + "', '" + ('{0:.2f}'.format(converted_price)) + "')")

    # Reset end point variables
    name_ep = 0
    image_ep = 0
    price_ep = 0

    # Add info to file for category 4
    for item in range(cat4_qty):
        name_sp = cat4_code.find("<item>      <title><![CDATA[", name_ep) + 28
        name_ep = cat4_code.find("]]></title>", name_sp + 1)
        name = cat4_code[name_sp: name_ep]
        invoice_file.write("<h4>" + name + "</h4><br>\n")

        image_sp = cat4_code.find('<img src="', image_ep) + 10
        image_ep = cat4_code.find('"', image_sp + 1)
        invoice_file.write('<img src="' + cat4_code[image_sp: image_ep] + '"><br>\n')

        price_sp = cat4_code.find('<span class="price">', price_ep) + 21
        price_ep = cat4_code.find('</span>', price_sp + 1)
        converted_price = round((float((cat4_code[price_sp: price_ep]).replace(",", "")) * 1.34), 2)
        invoice_file.write('<h5>Price: AU$' + "{0:.2f}".format(converted_price) + '</h5><br>\n')
        total = total + converted_price

        # Save values to DB
        if check_save_order.get() == 1:
            shopping_trolley_db.execute("INSERT INTO Purchases VALUES ('" + name + "', '" + ('{0:.2f}'.format(converted_price)) + "')")

    if total == 0:
        # No charge invoice
        invoice_file.write("<h3>You haven't added anything to your order. Thank you for browsing.</h3><br>\n")
    else:
        # Write order total to file
        invoice_file.write("<h3>Total for purchases above: AU$" + '{0:.2f}'.format(total) + "</h3><br>\n")

    # Write source attribution to file
    invoice_file.write(
        '''Online Shopper is an unofficial reseller of the following websites:\n
        <ul>
        <li><a href="http://india-shopping.khazano.com/rss/catalog/category/cid/18/store_id/1/">http://india-shopping.khazano.com/rss/catalog/category/cid/18/store_id/1/</a></li>
        <li><a href="https://www.seicane.com/rss/catalog/category/cid/158/store_id/1/">https://www.seicane.com/rss/catalog/category/cid/158/store_id/1/</a></li>
        <li><a href="https://www.etsy.com/shop/oktak/rss">https://www.etsy.com/shop/oktak/rss</a></li>
        <li><a href="https://www.crimezappers.com/rss/catalog/category/cid/199/store_id/1/">https://www.crimezappers.com/rss/catalog/category/cid/199/store_id/1/</a></li>
        </ul>\n
        </main>''')

    # Close file
    invoice_file.close()

    # Change progress label to indicate the process has finished
    progress.set("Done!")

    if check_save_order.get() == 1:
        connection.commit()
        shopping_trolley_db.close()
        connection.close()
        progress.set("Order saved!")

    # Set cursor to normal
    window.config(cursor="")


# Create window
window = Tk()
window.configure(background="white")

# Give window a title
window.title("Online Shopper")

# Create variables for widgets
check_save_order = IntVar()
progress = StringVar()
progress.set("Ready...")

# Define widgets
title_lbl = Label(window, text="Welcome to Online Shopper", justify="center", font=("", 12))
step1_lbl = Label(window, text="Step 1. Choose your quantities", justify="left", font=("", 10))
category1_lbl = Label(window, text="Fashion Jewellery", justify="right")
category1_sbx = Spinbox(window, from_=0, to=5, width=1)
category2_lbl = Label(window, text="Car DVR", justify="right")
category2_sbx = Spinbox(window, from_=0, to=5, width=1)
category3_lbl = Label(window, text="Purse", justify="right")
category3_sbx = Spinbox(window, from_=0, to=5, width=1)
category4_lbl = Label(window, text="Surveillance Systems", justify="right")
category4_sbx = Spinbox(window, from_=0, to=5, width=1)
step2_lbl = Label(window, text="Step 2. When ready, print your invoice", justify="left", font=("", 10))
save_order_cbx = Checkbutton(window, text="Save order", variable=check_save_order)
invoice_btn = Button(window, text="Print invoice", command=print_invoice)
step3_lbl = Label(window, text="Step 3. Watch your order's progress", justify="left", font=("", 10))
progress_lbl = Label(window, textvariable=progress)

# Align widgets to grid
title_lbl.grid(row=0, columnspan=4, padx=5, pady=5)
step1_lbl.grid(row=1, sticky="w", columnspan=4, padx=5, pady=5)
category1_lbl.grid(row=2, column=0, sticky="e", padx=5, pady=5)
category1_sbx.grid(row=2, column=1, padx=5, pady=5)
category2_lbl.grid(row=2, column=2, sticky="e", padx=5, pady=5)
category2_sbx.grid(row=2, column=3, padx=5, pady=5)
category3_lbl.grid(row=3, column=0, sticky="e", padx=5, pady=5)
category3_sbx.grid(row=3, column=1, padx=5, pady=5)
category4_lbl.grid(row=3, column=2, sticky="e", padx=5, pady=5)
category4_sbx.grid(row=3, column=3, padx=5, pady=5)
step2_lbl.grid(row=4, sticky="w", columnspan=4, padx=5, pady=5)
save_order_cbx.grid(row=5, columnspan=4, padx=5, pady=5)
invoice_btn.grid(row=6, columnspan=4, padx=5, pady=5)
step3_lbl.grid(row=7, sticky="w", columnspan=4, padx=5, pady=5)
progress_lbl.grid(row=8, columnspan=4, padx=5, pady=5)

# Give white background color to widgets
title_lbl.configure(background="white")
step1_lbl.configure(background="white")
category1_lbl.configure(background="white")
category2_lbl.configure(background="white")
category3_lbl.configure(background="white")
category4_lbl.configure(background="white")
step2_lbl.configure(background="white")
save_order_cbx.configure(background="white")
step3_lbl.configure(background="white")
progress_lbl.configure(background="white")

# Start window mainloop
window.mainloop()
