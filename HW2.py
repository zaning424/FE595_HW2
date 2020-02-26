import requests
from bs4 import BeautifulSoup


def dl_html(url):
    # this function download the html file to local
    for i in range(0, 50):
        get_resp = requests.get(url)
        web_content = get_resp.content
        soup = BeautifulSoup(web_content, "html.parser")
        names = soup.select('li')[0].contents[0]
        # grab file names from the web page
        file_name = names.replace('Name: ', '')
        with open(file_name + ".html", "wb") as file1:
            file1.write(web_content)
            # create and write html files


def get_source(url):
    # this function grab info and extract the name and purpose
    company_dic = []
    # company_dic is a list that each element in it is a list
    for i in range(0, 50):
        get_resp = requests.get(url)
        web_content = get_resp.content
        soup = BeautifulSoup(web_content, "html.parser")
        body_list = soup.select('li')
        # get a list from the web page including all info between <li>
        temp_list = []
        #  temp_list are the elements of company_dic
        for elem in body_list:
            if elem is None:
                continue
            elem = str(elem).replace('<li>', '')
            elem = str(elem).replace('</li>', '')
            # convert all the elements in the list into string
            if 'Name' in elem:
                temp_list.append(elem)
                continue
                # extract and append the 'Name' tag to the temp_list
            if 'Purpose' in elem:
                temp_list.append(elem)
                continue
                # extract and append the 'Purpose' tag to the temp_list
        company_dic.append(temp_list)
        # append each temp_list to the company_dic
    return company_dic


def file_generate(list):
    # this function write the Name and purpose of each company into a txt file
    file1 = open('595_HW2.txt', 'w')
    for ele in list:
        # loop the company_dic list
        for sub_ele in ele:
            # loop the temp_list which is the sublist of company_dic list
            file1.write(sub_ele)
            file1.write('\n')
        file1.write('\n')

    file1.close()


if __name__ == "__main__":
    url = "http://18.207.92.139:8000/random_company"
    dl_html(url)
    get_source(url)
    file_generate(get_source(url))