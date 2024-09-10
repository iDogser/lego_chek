import re

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

def check_lego_design_id(block, user_input_design_id):
    # Находим все элементы <li> и фильтруем их по наличию "LEGO® Design ID:"
    li_elements = block.find_all('li')
    design_id_block = None
    for li in li_elements:
        if 'LEGO® Design ID:' in li.text:
            design_id_block = li
            break

    if design_id_block:
        # Извлекаем LEGO Design ID с помощью регулярного выражения
        design_id = re.search(r'\d+', design_id_block.text).group(0)
        # Сравниваем с кодом, введенным пользователем
        return design_id == str(user_input_design_id)
    else:
        return False