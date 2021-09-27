

def biggest_loss(pricesLst: list) -> int:
    """
    Given a list of sell/but price pairs, this function will determine
    the biggest loss a client made
    :param pricesLst: Contains sell/buy price pairs
    :return: The biggest loss a client made
    """
    big_loss = 0
    if not isinstance(pricesLst, list) or len(pricesLst) == 0:
        return big_loss
    if len(pricesLst) % 2 != 0:
        return big_loss
    for i in range(0, len(pricesLst), 2):
        if pricesLst[i + 1] > pricesLst[i]:
            loss = round(pricesLst[i + 1] - pricesLst[i], 2)
            big_loss = max(big_loss, loss)
        else:
            return 0
    return big_loss

