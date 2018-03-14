def get_color(elev):
    """
    Function for deciding color of a marker according to elevation of volcanoes
    :param elev: int
    :return: str
    """
    if elev < 1000:
        return '#00BFFF'
    elif elev >= 1000 and elev < 3000:
        return '#FFA500'
    else:
        return '#A52A2A'

