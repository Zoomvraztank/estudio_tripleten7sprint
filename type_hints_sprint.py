def list_of_words(text:str,sep:str= " ")->list:
    """Devuelve una lista de palabras a partir de un texto dado, separando por el separador especificado.

    Args:
        text (str): El texto del cual se extraerán las palabras.
        sep (str, optional): El separador utilizado para dividir el texto en palabras. Por defecto es un espacio.

    Returns:
        list: Una lista de palabras extraídas del texto.
    """
    return text.split(sep)
result = list_of_words("Hola mundo, esta es una prueba de la función list_of_words.")

print(result)