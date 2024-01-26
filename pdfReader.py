import pdfplumber
import pandas as pd

def extract_tables_to_dataframe(pdf_file: str) -> pd.DataFrame:
    """
    Extracts all tables from a PDF file and returns them as a Pandas DataFrame.

    Args:
        pdf_file (str): The path to the PDF file.

    Returns:
        pd.DataFrame: A Pandas DataFrame containing the extracted tables.

    Raises:
        ValueError: If the input PDF file is not valid.

    """
    import pdfplumber
    import pandas as pd

    # Check if the input PDF file exists
    if not os.path.exists(pdf_file):
        raise ValueError(f"Input PDF file '{pdf_file}' does not exist.")

    # Import the PDF file using pdfplumber
    with pdfplumber.open(pdf_file) as pdf:
        # Initialize variables to store the extracted tables and their headers
        all_data = []
        headers = []

        # Loop through each page in the PDF file
        for page in pdf.pages:
            # Extract all tables from the current page
            tables = page.extract_tables()

            # Loop through each table on the current page
            for table in tables:
                # Initialize variables to track merged cells
                merged_cells = set()

                # Loop through each row in the table
                for i, row in enumerate(table):
                    # Initialize a list to store the current row's data
                    current_row = []

                    # Loop through each cell in the row
                    for j, cell in enumerate(row):
                        # Check if the current cell is part of a merged cell
                        if (i, j) in merged_cells:
                            continue

                        # Check if this row is the header row
                        if headers:
                            # If so, add the header to the current row
                            current_row.append(headers[j])

                        # Process and append the cell content
                        current_row.append(cell)

                        # Check for merged cells in the same row
                        rowspan = 1
                        colspan = 1
                        while j + colspan < len(row) and row[j + colspan] == "":
                            colspan += 1
                        while i + rowspan < len(table) and table[i + rowspan][j] == "":
                            rowspan += 1

                        # Mark merged cells to skip in the next iteration
                        for r in range(i, i + rowspan):
                            for c in range(j, j + colspan):
                                merged_cells.add((r, c))

                    # Add the current row to the table data
                    all_data.append(current_row)

                # Get the header row from the table
                header_row = table[0]

                # Add the header row to the list of headers
                headers.append(header_row)

        # Convert the table data to a Pandas DataFrame
        df = pd.DataFrame(all_data, columns=headers)

    return df

# Replace 'your_pdf_file.pdf' with the path to your PDF file
pdf_file_path = 'D:\Python_WA\git001\debigit001_ws\SamplePdf.pdf'
table_df = extract_tables_to_dataframe(pdf_file_path)

# Print the DataFrame in tabular format
print(table_df)
