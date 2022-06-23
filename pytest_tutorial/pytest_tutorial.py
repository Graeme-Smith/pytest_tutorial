def is_miscall(father, mother, child):
    """
    QC to identify miscalls

    This function takes three strings as args representing a haplotype for a trio of samples (father, mother, and child).
    The haplotypes can be "AA", "BB", or "AB".
    The function checks the parents haplotype and if the childs haplotype does not correspond reports it as a Miscall.
    For example, parents with aHaplotpe "AA" and "AA" cannot have a child with haplotype "BB".  This would suggest a technical issue with this result.
    """
    is_miscall = False

    if father == "AA" and mother == "AA" and child != "AA":
        is_miscall = True
    elif father == "BB" and mother == "BB" and child != "BB":
        is_miscall = True
    elif father == "AA" and mother == "BB" and child != "AB":
        is_miscall = True
    elif father == "BB" and mother == "AB" and child != "AB":
        is_miscall = True
    elif (
        father == "AA"
        and mother == "AB"
        and child
        not in [
            "AA",
            "AB",
        ]
    ):
        is_miscall = True
    elif (
        father == "BB"
        and mother == "AB"
        and child
        not in [
            "BB",
            "AB",
        ]
    ):
        is_miscall = True
    elif (
        father == "AB"
        and mother == "AA"
        and child
        not in [
            "AA",
            "AB",
        ]
    ):
        is_miscall = True
    elif (
        father == "AB"
        and mother == "BB"
        and child
        not in [
            "BB",
            "AB",
        ]
    ):
        is_miscall = True
    return is_miscall


print(is_miscall("AA", "BB", "BB"))
