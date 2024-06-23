import pandas as pd
from requests import get
from bs4 import BeautifulSoup as bs

def scrape1_data(url_template, num_pages):
    df = pd.DataFrame()
    page_number = 1
    
    while page_number <= num_pages:
        url = url_template.format(page_number)
        res = get(url)
        bsoup = bs(res.text, 'html.parser')
        containeurs = bsoup.find_all('div', class_='item-inner mv-effect-translate-1 mv-box-shadow-gray-1')
        if not containeurs:
            break
        
        data = []
        for containeur in containeurs:
            try:
                link = containeur.find('a', class_='mv-overflow-ellipsis')['href']
                res_c = get(link)
                bsoup_c = bs(res_c.text, 'html.parser')
                inf_gen_div = bsoup_c.find('div', style='font-weight:bold; margin-top:10px;')
                if inf_gen_div:
                    marque_text = inf_gen_div.text
                    marque = marque_text.split(':')[1].strip() if ':' in marque_text else 'NA'
                else:
                    marque = 'NA'

                prix = containeur.find('div', class_='content-price').text.replace(' ', '').replace('FCFA', '')

                adresse_span = containeur.find('span', {'style': 'color:#ce1439; font-size:15px;'})
                adresse = adresse_span.text.strip() if adresse_span else 'Adresse non disponible'

                img_tag = containeur.find('img')
                img_lien = 'https://dakarvente.com' + img_tag['src'].strip() if img_tag else 'Pas d\'image'
                if not img_lien.startswith('https://dakarvente.com/'):
                    img_lien = img_lien.replace('https://dakarvente.com', 'https://dakarvente.com/')
                    
                obj = {
                    'MARQUE': marque,
                    'PRIX': int(prix),
                    'ADRESSE': adresse,
                    'IMAGE': img_lien
                }

                data.append(obj)

            except Exception as e:
                pass

        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis=0).reset_index(drop=True)
        df = df[(df['MARQUE'] != 'Neuf') & (df['MARQUE'] != 'Occasion') & (df['MARQUE'] != 'NA')]
        
        page_number += 1
    
    return df
