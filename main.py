from data_models import TopicModel, KeywordsGroupModel
import file_manager
import search_engines

print("Inicio de la ejecución del programa")

# Obtener la lista de temas y keywords del archivo de entrada
print("Obteniendo temas")

topics = file_manager.read_input_file()
topics_number = len(topics.keys())

print("Se encontraron {} temas.".format(topics_number))

# Analizar todos los temas y sus respectivas keywords
topic_objects = list()
topic_index = 0

for topic in topics.keys():
    topic_index = topic_index + 1
    topic_model = TopicModel(topic)
    keywords = topics[topic]
    keywords_index = 0
    keywords_number = len(keywords)

    for group in keywords:
        keywords_index = keywords_index + 1
        
        print("Analizando tema ({}/{}) > keywords {}/{}.".format(topic_index, topics_number, keywords_index, keywords_number))

        google_search = search_engines.search_google_news(group)
        yahoo_search = search_engines.search_yahoo_news(group)
        results_number = google_search[1] + yahoo_search[1]

        topic_model.keyword_groups.append(KeywordsGroupModel(group, results_number, google_search[2], yahoo_search[2]))

    topic_objects.append(topic_model)

# Guardar resultados en archivo de salida
print("Guardando resultados")

file_manager.write_output_file(topic_objects)

print("Fin de la ejecución del programa")