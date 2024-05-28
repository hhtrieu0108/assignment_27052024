from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pandas as pd
from time import sleep
import logging
from bs4 import BeautifulSoup


def crawl_data_feature():
    try:
        firefox_option = Options()
        driver = webdriver.Firefox(options=firefox_option)
        driver.get("https://ohitv.net/phim-le/page/1/")
        driver.fullscreen_window()
        sleep(5)
        page_html = driver.page_source
        soup = BeautifulSoup(page_html,"html.parser")
        elems_fea = soup.find_all("div",class_='data dfeatur')
        title = [elem.text for elem in elems_fea]
        links = []
        for elem in elems_fea:
            href_element = elem.find_all('a', href=True)

            for href in href_element:
                links.append(href['href'])

        data_fea = pd.DataFrame(list(zip(title,links)),columns=['title','link'])
        data_fea['feature'] = 'Yes'
        data_fea.to_csv("ohitv_film/Feature_Film.csv",index=False)
    except Exception as e:
        logging.error("Error in Crawl data feature",e)
        raise
    finally:
        driver.quit()

def crawl_data_nofeature():
    try:
        firefox_option = Options()
        driver = webdriver.Firefox(options=firefox_option)
        data = pd.DataFrame(columns=['title','link'])
        kinds = ['phim-chieu-rap','action-adventure','phim-chinh-kich','phim-hai','phim-bi-an','phim-hinh-su','phim-gia-dinh',
                'phim-lang-man','phim-hanh-dong','phim-gia-tuong','sci-fi-fantasy','phim-phieu-luu','phim-hoat-hinh']
        title = []
        links = []
        for kind in kinds:
            for i in range(1,100):
                driver.get(f"https://ohitv.net/the-loai/{kind}/page/{i}/")
                driver.fullscreen_window()
                sleep(2)
                page_html = driver.page_source
                soup = BeautifulSoup(page_html,"html.parser")
                new_elems = soup.find_all("div",class_='data')
                if len(new_elems) == 0:
                    break
                else:
                    for elem in new_elems:
                        # Find all anchor tags with an href attribute within each div
                        title_element = elem.find_all('h3')
                        for title_text in title_element:
                            title.append(title_text.text)
                    for elem in new_elems:
                        # Find all anchor tags with an href attribute within each div
                        href_element = elem.find_all('a', href=True)
                        for href in href_element:
                            links.append(href['href'])
                new_data = pd.DataFrame(list(zip(title,links)),columns=['title','link'])
                new_data['kind'] = kind.replace('-',' ')
                data = pd.concat((data,new_data),axis=0,ignore_index=True)
        data['feature'] = 'No'
        data.to_csv("ohitv_film/NoFeature_Film.csv",index=False)
    except Exception as e:
        logging.error("No feature false",e)
        raise
    finally:
        driver.quit()


def processing_data():
    try:
        feature_film = pd.read_csv("ohitv_film/Feature_Film.csv")
        nofeature_film = pd.read_csv("ohitv_film/NoFeature_Film.csv")
        def return_feature(data):
            if data in feature_film['title'].to_list():
                return 'Yes'
            else:
                return 'No'
        nofeature_film['isfeature'] = nofeature_film['title'].apply(return_feature)
        new_data = nofeature_film.drop(columns='feature')
        new_data_nodup = new_data.drop_duplicates('title')
        new_data.to_csv("dags/ohitv_film/duplicate_film.csv",index=False)
        new_data_nodup.to_csv("dags/ohitv_film/nodup_film.csv",index=False)
    except Exception as e:
        logging.error("Cant Processing",e)
        raise

if __name__ == "__main__":
    crawl_data_feature()
    crawl_data_nofeature()
    processing_data()
