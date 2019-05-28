import csv

# Leer el archivo de entrada y retornar un diccionario conteniendo los temas como llaves y sus respectivas keywords en listas
def read_input_file():
    topic_dict = {}

    with open('input.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        
        for row in csv_reader:
            if row[0] not in topic_dict.keys():
                topic_dict[row[0]] = list()

            topic_dict[row[0]].append(row[1])

    return topic_dict

# Dada una lista de objetos de tema, generar el archivo de salida
def write_output_file(topic_objects):
    with open('output.csv', mode='w') as csv_file:
        fieldnames = ["Tema", "Keywords", "Resultados", "GoogleNews", "YahooNews"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, lineterminator = '\n')

        writer.writeheader()

        topic_flag = False

        for topic_object in topic_objects:
            keywords_flag = False

            for keywords_group in topic_object.keyword_groups:
                for link_index in range(0, len(keywords_group.google_news_links)):
                    output_topic = topic_object.topic
                    output_keywords = keywords_group.keywords
                    output_results_number = keywords_group.results_number
                    output_google_news_link = keywords_group.google_news_links[link_index]
                    output_yahoo_news_link = keywords_group.yahoo_news_links[link_index]

                    if not topic_flag:
                        topic_flag = True
                        keywords_flag = True
                    elif not keywords_flag:
                        output_topic = ""
                        keywords_flag = True
                    else:
                        output_topic = ""
                        output_keywords = ""
                        output_results_number = ""

                    writer.writerow({"Tema": output_topic, "Keywords": output_keywords, "Resultados": output_results_number, "GoogleNews": output_google_news_link, "YahooNews": output_yahoo_news_link})
                    
                keywords_flag = False

            topic_flag = False
