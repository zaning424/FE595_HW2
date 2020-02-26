import requests
from bs4 import BeautifulSoup


def get_source(url):
    company_dic = []
    for i in range(0, 50):
        get_resp = requests.get(url)
        web_content = get_resp.content
        soup = BeautifulSoup(web_content, "html.parser")
        body_list = soup.select('li')
        temp_list = []
        for elem in body_list:
            if elem is None:
                continue
            elem = str(elem).replace('<li>', '')
            elem = str(elem).replace('</li>', '')
            if 'Name' in elem:
                temp_list.append(elem)
                continue
            if 'Purpose' in elem:
                temp_list.append(elem)
                continue
        company_dic.append(temp_list)
    return company_dic


def file_generate(list):
    file1 = open('595_HW2.txt', 'w')
    for ele in list:
        for sub_ele in ele:
            file1.write(sub_ele)
            file1.write('\n')
        file1.write('\n')

    file1.close()


if __name__ == "__main__":
    url = "http://18.207.92.139:8000/random_company"
    company_list = get_source(url)
    file_generate(company_list)