from ultron.actions.google_search import GoogleSearch

if __name__== '__main__':
    googleSearch = GoogleSearch('Kamaal Rashid Khan')

    googleSearch.pre_execute()
    googleSearch.execute()
    googleSearch.post_execute()

    print('\nNames -->')
    for each_name in googleSearch.get_names():
        print('\t'+each_name)

    print('\nLinks -->')
    for each_link in googleSearch.get_links():
        print('\t'+each_link)