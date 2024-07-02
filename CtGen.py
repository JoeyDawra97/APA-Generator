import tkinter as tk
from tkinter import ttk

def format_author_name(names):
    authors = []
    for name in names.split(','):
        parts = name.strip().split()
        if len(parts) >= 2:
            last_name = parts[-1].capitalize()
            first_name_initial = parts[0][0].upper() + '.'
            authors.append(f"{last_name} {first_name_initial}")
        else:
            authors.append(f"{parts[0].capitalize()}.")

    if len(authors) > 1:
        formatted_authors = ', '.join(authors[:-1]) + ', & ' + authors[-1]
    else:
        formatted_authors = authors[0]

    return formatted_authors

def capitalize_month(date):
    parts = date.split()
    if len(parts) == 3:
        year, month, day = parts
        month = month.capitalize()
        return f"{year}, {month} {day}"
    elif len(parts) == 2:
        year, month = parts
        month = month.capitalize()
        return f"{year}, {month}"
    elif len(parts) == 1:
        return f"{parts[0]}"
    else:
        return "n.d."

def capitalize_first_word(text):
    parts = text.split()
    if parts:
        parts[0] = parts[0].capitalize()
    return ' '.join(parts)

def title_case(text):
    words = text.split()
    minor_words = {"and", "or", "but", "nor", "yet", "so", "for", "at", "by", "in", "of", "on", "to", "up", "a", "an", "the"}
    if words:
        words[0] = words[0].capitalize()
    for i in range(1, len(words)):
        if words[i].lower() not in minor_words:
            words[i] = words[i].capitalize()
        else:
            words[i] = words[i].lower()
    return ' '.join(words)

def generate_apa_citation():
    # Get input values
    author = author_entry.get()
    date = date_entry.get()
    title = title_entry.get()
    subtitle = subtitle_entry.get()
    website_name = website_name_entry.get()
    url = url_entry.get()

    # Format author names
    formatted_author = format_author_name(author)

    # Capitalize first word of the title and subtitle
    full_title = capitalize_first_word(title)
    if subtitle:
        full_title = f"{full_title}: {capitalize_first_word(subtitle)}"

    # Format date input
    formatted_date = f"({capitalize_month(date)})"

    # Format website name in title case
    formatted_website_name = title_case(website_name)

    # Italicize title if checkbox is checked
    if italicize_title.get():
        full_title = f"<i>{full_title}</i>"

    # Generate the citation
    citation = f"{formatted_author} {formatted_date}. {full_title}. {formatted_website_name}. {url}"

    # Display the citation
    citation_output.delete("0", tk.END)
    citation_output.insert("0", citation)

def open_another_window():
    # Create another window
    another_window = tk.Toplevel(root)
    another_window.title("Quotes")

    # Display quotes
    for i, quote in enumerate(quotes):
        ttk.Label(another_window, text=quote).grid(row=i, column=0, padx=10, pady=5, sticky='w')


# Create the main window
root = tk.Tk()
root.title("APA 7th Citation Generator")

# Note for author entry
author_note = ttk.Label(root, text="*Insert a comma between each author's full name*", foreground='blue')
author_note.grid(column=1, row=0, padx=(0, 10), pady=5, sticky='w')

# Note for date entry
date_note = ttk.Label(root, text="*Insert date as YYYY Month Day with spaces in between*", foreground='red')
date_note.grid(column=1, row=1, padx=(0, 10), pady=5, sticky='w')

ital_note = ttk.Label(root, text="*Check box to add Italics indication*", foreground='green')
ital_note.grid(column=1, row=2, padx=(0, 10), pady=5, sticky='w')

# Create and place the labels and entries for input
ttk.Label(root, text="Author(s)", foreground='blue').grid(column=0, row=3, padx=10, pady=5)
author_entry = ttk.Entry(root, width=50)
author_entry.grid(column=1, row=3, padx=10, pady=5)

ttk.Label(root, text="Date", foreground='red').grid(column=0, row=4, padx=10, pady=5)
date_entry = ttk.Entry(root, width=50)
date_entry.grid(column=1, row=4, padx=10, pady=5)

ttk.Label(root, text="Title").grid(column=0, row=5, padx=10, pady=5)
title_entry = ttk.Entry(root, width=50)
title_entry.grid(column=1, row=5, padx=10, pady=5)

ttk.Label(root, text="Website Name").grid(column=0, row=7, padx=10, pady=5)
website_name_entry = ttk.Entry(root, width=50)
website_name_entry.grid(column=1, row=7, padx=10, pady=5)

ttk.Label(root, text="URL").grid(column=0, row=8, padx=10, pady=5)
url_entry = ttk.Entry(root, width=50)
url_entry.grid(column=1, row=8, padx=10, pady=5)

# Create and place the button to generate the citation
generate_button = ttk.Button(root, text="Generate Citation", command=generate_apa_citation)
generate_button.grid(column=0, row=9, columnspan=2, pady=10)

# Checkbox for italicizing title
italicize_title = tk.BooleanVar()
italicize_checkbox = tk.Checkbutton(root, text="Italicize Title", variable=italicize_title, fg='green')
italicize_checkbox.grid(column=0, row=9, padx=10, pady=5, sticky='w')

# Set color for the italicize checkbox
italicize_checkbox_label = italicize_checkbox.cget("text")
italicize_checkbox.config(text=italicize_checkbox_label)

# Create and place the entry for the output citation
citation_output = ttk.Entry(root, width=80)
citation_output.grid(column=0, row=10, columnspan=2, padx=10, pady=5)

# Start the main event loop
root.mainloop()
