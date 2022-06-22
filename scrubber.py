import requests
import os.path
import numpy as np
from bs4 import BeautifulSoup as BS


# The information will be taken over 2007 to current day
# Justification: split of Serbia and Montenegro into 2 distinct countries is the last country split recognized internationally.


def scrub_un_docs (from_year = 2007, until_year = 2023):
    years = range(from_year,until_year)
    # For each year
    # Get the search record with 100 results shown
    format_search_url = "https://digitallibrary.un.org/search?c=Voting+Data&jrec={}&cc=Voting+Data&ln=en&rg=100&fct__3={}&fct__2=General+Assembly&fct__9=Vote"
    format_record_url = "https://digitallibrary.un.org/record/{}"
    format_search_file = "./search/year_{}_from_{}.html"
    format_record_file = "./record/{}.html"
    starting_page_jrec = 1;
    # Extract info from class="searchresultsboxheader searchresultsrecsfound" by matching it against "results found"
    # If greater than 100, get the other search pages
    # For each of search pages extract links that link to /record
    # Jump into the record
    # extract the list from class="value col-xs-12 col-sm-9 col-md-10"
    # Split into lines based <br>
    # If first character is space, look at second. If third character is also a space, it's a vote indicator.
    # Otherwise, look if second character is space, if so, it is also a vote indictor.
    additional_requests = list()
    record_urls = list()
    for year in years:
        print("Getting voting records from year ", year)
        search_file = format_search_file.format(year,starting_page_jrec)
        pagetext = str()
        if os.path.exists(search_file):
            page = open(search_file,'r')
            pagetext = page.read()
            page.close()
        else:
            print("No backup found, getting from server")
            request_url = format_search_url.format(starting_page_jrec,year)
            page = requests.get(request_url)
            print("Response code ", page)
            pagetext = page.text
            backup = open(search_file,'w')
            backup.write(pagetext)
            backup.close()
        soup = BS(pagetext,'html.parser')
        results_count = int(soup.find('td',class_='searchresultsboxheader searchresultsrecsfound').strong.get_text())
        if results_count > 100:
            for jrec in range(101,results_count,100):
                additional_requests.append([year, jrec])
        for link in soup.find_all('a'):
            dest = link.get('href')
            if dest != None:
                if dest[:8] == '/record/':
                    record_urls.append(dest[8:])
    for add_req in additional_requests:
        print("Getting additional voting records for year ", year)
        search_file = format_search_file.format(add_req[0],add_req[1])
        if os.path.exists(search_file):
            page = open(search_file,'r')
            pagetext = page.read()
            page.close()
        else:
            request_url = format_search_url.format(add_req[1],add_req[0])
            page = requests.get(request_url)
            print ("Response code ", page)
            pagetext = page.text
            backup = open(search_file,'w')
            backup.write(pagetext)
            backup.close()
        soup = BS(pagetext,'html.parser')
        for link in soup.find_all('a'):
            dest = link.get('href')
            if dest != None:
                if dest[:8] == '/record/':
                    record_urls.append(dest[8:])
    countries_votes = {}                                                    
    record_cnt = 0;                                                    
    for record_url in record_urls:
        print("Processing voting record ", record_url)
        record_file = format_record_file.format(record_url)
        pagetext = str()
        if os.path.exists(record_file):
            page = open(record_file)
            pagetext = page.read()
            page.close()
        else:
            request_url = format_record_url.format(record_url)
            page = requests.get(request_url)
            print ("Response code ", page)
            pagetext = page.text
            backup = open(record_file,'w')
            backup.write(pagetext)
            backup.close()
        soup = BS(pagetext,'html.parser')
        voting_record = soup.find_all('span',class_='value col-xs-12 col-sm-9 col-md-10')
        metadata = soup.find_all('span',class_='title col-xs-12 col-sm-3 col-md-2')
        record_len = len(voting_record)
        meta_len = len(metadata)
        votes = voting_record[record_len - 2].stripped_strings
        vote_title = metadata[meta_len - 2].string
        if vote_title == "Vote date":
            continue
        for vote in votes:
            if vote[2] == ' ' and vote[:2] != "EL":
                print(record_url, vote)
                country = vote[3:]
                print(country)

                if country not in countries_votes:
                    countries_votes[country] = (record_cnt * ('E')) + vote[0]
                else:
                    countries_votes[country] += vote[0]
            elif vote[1] == ' ':
                country = vote[2:]
                # A bunch of hardcoding the political exceptions
                if country[:7] == "BOLIVIA":
                    country = "BOLIVIA"                                                                        
                elif country[:10] == "THE FORMER":
                    country = "NORTH MACEDONIA"                                                                      
                elif country[:4] == "CAPE":
                    country = "CABO VERDE"
                elif country[:5] == "SWAZI":
                    country = "ESWATINI"
                elif country[:6] == "LIBYAN":
                    country = "LIBYA"
                elif country[:7] == "CZECHIA":
                    country = "CZECH REPUBLIC"
                elif country == "CENTRAL AFRICAN EMPIRE":
                    country = "CENTRAL AFRICAN REPUBLIC"
                elif country == "UNITED ARAB REPUBLIC":
                    country = "EGYPT"
                elif country == "DEMOCRATIC KAMPUCHEA":
                    country = "CAMBODIA"
                elif country == "CEYLON":
                    country = "SRI LANKA"
                elif country == "CONGO (LEOPOLDVILLE)":
                    country = "CONGO (DEMOCRATIC REPUBLIC OF)"
                elif country == "CONGO (BRAZZAVILLE)":
                    country = "CONGO"
                elif country[:3] == "LAO":
                    country = "LAOS"
                elif country == "DAHOMEY":
                    country = "BERIN"
                elif country[:8] == "MALDIVES":
                    country = "MALDIVES"
                elif country == "KHMER REPUBLIC":
                    country = "CAMBODIA"
                elif country == "DEMOCRATIC YEMEN":
                    country = "SOUTHERN YEMEN"
                elif country[:5] == "SYRIA":
                    country = "SYRIA"
                elif country == "ZAIRE":
                    country = "CONGO (DEMOCRATIC REPUBLIC OF)"
                elif country == "UNITED REPUBLIC OF CAMEROON":
                    country = "CAMEROON"
                elif country == "SURINAM":
                    country = "SURINAME"
                
                                                                                
                if country not in countries_votes:
                    countries_votes[country] = (record_cnt * ('E')) + vote[0]
                else:
                    countries_votes[country] += vote[0]
            else:
                country = vote
                if country[:7] == "BOLIVIA":
                    country = "BOLIVIA"                                                
                elif country[:10] == "THE FORMER":
                    country = "NORTH MACEDONIA"
                elif country[:4] == "CAPE":
                    country = "CABO VERDE"
                elif country[:5] == "SWAZI":
                    country = "ESWATINI"
                elif country[:6] == "LIBYAN":
                    country = "LIBYA"
                elif country[:7] == "CZECHIA":
                    country = "CZECH REPUBLIC"
                elif country == "CENTRAL AFRICAN EMPIRE":
                    country = "CENTRAL AFRICAN REPUBLIC"
                elif country == "UNITED ARAB REPUBLIC":
                    country = "EGYPT"
                elif country == "DEMOCRATIC KAMPUCHEA":
                    country = "CAMBODIA"
                elif country == "CEYLON":
                    country = "SRI LANKA"
                elif country == "CONGO (LEOPOLDVILLE)":
                    country = "CONGO (DEMOCRATIC REPUBLIC OF)"
                elif country == "CONGO (BRAZZAVILLE)":
                    country = "CONGO"
                elif country[:3] == "LAO":
                    country = "LAOS"
                elif country == "DAHOMEY":
                    country = "BERIN"
                elif country[:8] == "MALDIVES":
                    country = "MALDIVES"
                elif country == "KHMER REPUBLIC":
                    country = "CAMBODIA"
                elif country == "DEMOCRATIC YEMEN":
                    country = "SOUTHERN YEMEN"
                elif country[:5] == "SYRIA":
                    country = "SYRIA"
                elif country == "ZAIRE":
                    country = "CONGO (DEMOCRATIC REPUBLIC OF)"
                elif country == "UNITED REPUBLIC OF CAMEROON":
                    country = "CAMEROON"
                elif country == "SURINAM":
                    country = "SURINAME"
                                                                                    
                if country not in countries_votes:
                    countries_votes[country] = (record_cnt * ('E')) + 'E'
                else:
                    countries_votes[country] += 'E'
                                                                                            
        record_cnt += 1
                #A very stupid balancing algorithm
        for country in countries_votes:
            if len(countries_votes[country]) < record_cnt:
                countries_votes[country] += 'E'
                                                                                                    
    print("Amount of countries:",len(countries_votes))
    print("Amount of votes held:",record_cnt)
                                                                                                    
    country_cnt = 0
    vote_matrix = np.zeros((len(countries_votes),record_cnt))
    country_list = list()
                                                                                                    
    for country in countries_votes:
        for i in range(record_cnt):
            if countries_votes[country][i] == 'Y':
                vote_matrix[country_cnt][i] = 1
            if countries_votes[country][i] == 'N':
                vote_matrix[country_cnt][i] = -1
        print("{} had voted {} times".format(country, np.linalg.norm(vote_matrix[country_cnt])))
        if np.linalg.norm(vote_matrix[country_cnt],1) != 0:
            country_list.append(country)
            country_cnt += 1
        else:
            vote_matrix = np.delete(vote_matrix,country_cnt,0)

    return vote_matrix, country_list
                
# That's the scrapping done
