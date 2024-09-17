from bs4 import BeautifulSoup
import requests as req
import pandas as pd

# Fetch the webpage
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue'
page = req.get(url)

# Parse the webpage content
soup = BeautifulSoup(page.text, 'html')

# Find the table on the page
table = soup.find_all('table')[0]

# Extract the table headers
title_column = table.find('tr')
world_titles = title_column.find_all('th')

# Extract column names and skip the first header (if it is an index column)
world_table_titles = [title.text.strip() for title in world_titles[1:]]
df = pd.DataFrame(columns = world_table_titles)

# Extract the rows of the table
columns_data = table.find_all('tr')
# Iterate through rows, skipping the first two rows
for row in columns_data[2:]: #[2:]makes it skip the first 2 rows
    # Extract table data
    row_data1 = row.find_all('th')
    row_data2 = row.find_all('td')
    # Combine row headers (if any) and data, then skip the first element (index column)
    individual_row_data = [ data.text.strip() for data in row_data1 + row_data2][1:] # Skip first column
    # Add the data to the DataFrame
    length = len(df)
    df.loc[length]= individual_row_data

#change it to csv
df.to_csv(r'C:\\Users\\Testing\\Desktop\\py\\pythonProject\\webscrapping\\Companies.csv')
# Print or display the DataFrame
print(df)