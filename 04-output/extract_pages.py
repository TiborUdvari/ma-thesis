import argparse
import re
import os
from PyPDF2 import PdfReader, PdfWriter

# Function to extract page numbers for a specific tag from an .aux file
def extract_page_numbers(aux_file_path, tag):
    page_numbers = []
    # Compile the regex pattern for matching tags in the .aux file
    tag_pattern = re.compile(r'\\newcustomtag{' + re.escape(tag) + r'}{(\d+)}')
    
    # Open and read the .aux file, searching for the tag pattern
    with open(aux_file_path, 'r') as file:
        for line in file:
            match = tag_pattern.search(line)
            if match:
                # Add the found page number to the list (as 0-indexed)
                page_numbers.append(int(match.group(1)) - 1)
    return page_numbers

# Function to add a blank page with the size of the first page in the PDF
def add_blank_page(writer, reader):
    print("ADDED BLANK PAGE")
    return
    width = reader.pages[0].mediabox.width
    height = reader.pages[0].mediabox.height
    blank_page = PdfWriter().add_blank_page(width=width, height=height)
    writer.add_page(blank_page)

# Function to create the PDF for the tagged pages
def create_tagged_pdf(reader, tagged_page_numbers, output_pdf_path, tag_name):
    writer = PdfWriter()
    for page_number in tagged_page_numbers:
        writer.add_page(reader.pages[page_number])

    with open(output_pdf_path, 'wb') as output_file:
        writer.write(output_file)

    print(f'Pages with tag "{tag_name}" have been extracted to {output_pdf_path}')

# Function to create the PDF for the untagged pages and insert blank pages if necessary
def create_untagged_pdf(reader, all_pages, tagged_pages, output_pdf_path):
    writer = PdfWriter()
    tagged_pages_set = set(tagged_pages)
    untagged_pages_set = set(all_pages) - set(tagged_pages)
    
    i = 0
    pageCount = 0
    
    # page numbers are 0 indexed
    while i < len(all_pages):
        if i in untagged_pages_set:
            writer.add_page(reader.pages[i])
            pageCount = pageCount + 1
        else:
            if pageCount % 2 != 0:
                add_blank_page(writer, reader)
                pageCount = pageCount + 1
        i = i + 1

    with open(output_pdf_path, 'wb') as output_file:
        writer.write(output_file)

    print(f'Untagged pages have been extracted to {output_pdf_path}')

# Main function to process the PDF and .aux files
def process_files(base_filename, tags, destination):
    aux_file_path = f"{base_filename}.aux"
    pdf_file_path = f"{base_filename}.pdf"
    reader = PdfReader(pdf_file_path)
    all_pages = list(range(len(reader.pages)))
    tagged_pages = []

    # Process each tag and create PDFs for tagged pages
    print("The tags are ")
    print(tags)
    for tag in tags:
        tag_page_numbers = extract_page_numbers(aux_file_path, tag)
        print(tag_page_numbers)
        tagged_pages.extend(tag_page_numbers)
        if tag_page_numbers:
            base_name = os.path.splitext(os.path.basename(base_filename))[0]
            output_pdf_path = os.path.join(destination, f"{base_name}_{tag}_extracted.pdf") if destination else f"{base_name}_{tag}_extracted.pdf"
            create_tagged_pdf(reader, tag_page_numbers, output_pdf_path, tag)

    # Create PDF for untagged pages
    base_name = os.path.splitext(os.path.basename(base_filename))[0]
    untagged_output_pdf_path = os.path.join(destination, f"{base_name}_untagged_pages.pdf") if destination else f"{base_name}_untagged_pages.pdf"
    create_untagged_pdf(reader, all_pages, tagged_pages, untagged_output_pdf_path)

# Set up the argument parser
parser = argparse.ArgumentParser(description="Extract pages from a PDF based on tags in an .aux file and adjust untagged pages for duplex printing.")
parser.add_argument("base_filename", type=str, help="The base name of the PDF and AUX files, without extension.")
parser.add_argument("tags", type=str, nargs="+", help="The list of tags to extract pages for.")
parser.add_argument("-d", "--destination", type=str, default="", help="Optional destination directory for the extracted PDF files.")

# Parse the arguments
args = parser.parse_args()

# Call the main processing function
process_files(args.base_filename, args.tags, args.destination)
