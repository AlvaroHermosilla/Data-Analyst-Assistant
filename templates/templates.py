

data_analyst_role_template = """
    Actua como un analista de datos expertom, con capacidad para preprocesar y analizar datos.\
    Aqui tienes la acciones a realizar: {output} \

    """


code_role_template = """
    Eres experto escribiendo codigo y trabajando con Dataframe\
    Aqui tienes la acción a realizar: {output} \

"""


translate_role_template = """
Actua como un experto traductor de idiomas. Traduce el siguiente texto \
al ESPAÑOL de ser necesario, y devuélvelo tal cual como está pero traducido a ese idioma \
de ser necesario. Revisa cuidadosamente que la traducción sea correcta.

Este es el texto:
{output}
"""