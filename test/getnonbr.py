import pytest
import pandas as pd


@pytest.mark.getonbr
def test_getonboard(browser_page):
    browser_page.goto("https://www.getonbrd.com")
    text_home=browser_page.text_content("//h1")
    print("texto",text_home)
    assert text_home=="Trabajos increíbles en tecnología"
    seccion_pr=browser_page.text_content("(//div[contains(@class,'gb-tags mtb')]/child::a[contains(text,'')])[2]")
    print("texto",seccion_pr)
    assert seccion_pr == "Programación"
    browser_page.click("(//div[contains(@class,'gb-tags mtb')]/child::a[contains(text,'')])[2]")

    #titles job contiene la lista de items a recorrer
    #como estamos accediendo a este elemento, para capturar los datos que estan dentro
    #se debe agregar las clases de css o xpath de los elementos que se encuentran dentro 
    titles_jobs=browser_page.query_selector_all("//div/child::a[contains(@class,'gb-results-list__item')]")
    link_list=[]
    titles_lits=[]
    enterprises_list=[]
    for data in titles_jobs:
        links_jobs=data.get_attribute("href")
        titles=data.query_selector(".pr-3").text_content()
        enterprises=data.query_selector("//div[contains(@class,'size0')]/child::strong").text_content()
        publish=data.query_selector("//div[contains(@class,'opacity-half size0')]").text_content()
        #print(publish
        link_list.append(links_jobs)
        titles_lits.append(titles)
        enterprises_list.append(enterprises)

    
    data={
        'titles': titles_lits,
        'enterprise': enterprises_list,
        'link': link_list
    }

    # Crear DataFrame
    df = pd.DataFrame(data)
    pd.set_option('display.max_rows', 100)  # Cambia 100 al número que quieras mostrar
    pd.set_option('display.max_columns', 10) 
    # Mostrar DataFrame
    print(df)
    df.to_csv('archivo.csv', index=False)