class TopicModel:
    def __init__(self, topic):
        self.topic = topic
        self.keyword_groups = list()

class KeywordsGroupModel:
    def __init__(self, keywords, results_number, google_news_links, yahoo_news_links):
        self.keywords = keywords
        self.results_number = results_number
        self.google_news_links = list()
        self.yahoo_news_links = list()

        # Normalizar el tamano de ambas listas te enlace
        if len(google_news_links) == len(yahoo_news_links):
            if len(google_news_links) == 0:
                self.google_news_links.append("")
                self.yahoo_news_links.append("")
        else:
            self.google_news_links = google_news_links
            self.yahoo_news_links = yahoo_news_links

            if len(google_news_links) > len(yahoo_news_links):
                for i in range(0, len(google_news_links) - len(yahoo_news_links)):
                    self.yahoo_news_links.append("")
            else:
                for i in range(0, len(yahoo_news_links) - len(google_news_links)):
                    self.google_news_links.append("")