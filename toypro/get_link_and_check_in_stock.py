def check_in_stock(block):
    html_code = str(block)
    if "Add to Cart" in html_code:
        return True
    elif "Email notification" in html_code or "Out of stock" in html_code:
        return False
    else:
        return None
    
def get_product_link(block):
    link_element = block.find('a', class_='c_product-block__link h_stretched-link')
    
    if link_element:
        link = link_element['href']
        full_link = f"https://www.toypro.com{link}"
        return full_link
    return None