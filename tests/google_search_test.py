from ultron.actions.google_search import GoogleSearch

if __name__ == '__main__':
    search_google = GoogleSearch('Kamaal Rashid Khan')
    search_google.pre_execute()
    search_google.execute()
    search_google.post_execute()
