from bs4 import BeautifulSoup
import openpyxl

html_file_path = r'C:/Users/Vee/OneDrive - Goodlife Pharmacy/Desktop/MY PROJECTS/Randoms/Web Scraping/Amazon Deals/Amazon _ Deals.html'
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all divs with class="scroll-carousel_slide__1ku-E"
divs = soup.find_all('div', class_='scroll-carousel_slide__1ku-E')

# Create a new Excel workbook and add a sheet
workbook = openpyxl.Workbook()
sheet = workbook.active

# Write headers to the Excel sheet
sheet.append(['Product Name', 'Deal Price', 'List Price'])

# Loop through each div and extract information
for div in divs:
    # Extract Product Name
    product_name_div = div.find('div', class_='title--3qM6_ title--X01QH titleAnchor--2TGNn doubleLinesTitle--ATRHO')
    product_name = product_name_div.text.strip() if product_name_div else ''

    # Extract Deal Price
    deal_price_div = div.find('div', class_='dealPrice--QJhpv')
    deal_price = deal_price_div.find('span', class_='netPrice--2L7XO').text.strip() if deal_price_div else ''

    # Extract List Price
    list_price_div = div.find('div', class_='listPrice--vhN5A')
    list_price = list_price_div.find('span').text.strip() if list_price_div else ''

    # Write the data to the Excel sheet
    sheet.append([product_name, deal_price, list_price])

# Save the Excel workbook
workbook.save('Amazon_Deals_Output.xlsx')
