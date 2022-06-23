def is_miscall(male_partner, female_partner, embryo):
    """
    QC to identify miscalls
    """
    is_miscall = False

    if male_partner == "AA" and female_partner == "AA" and embryo != "AA":
        is_miscall = True
    elif male_partner == "BB" and female_partner == "BB" and embryo != "BB":
        is_miscall = True
    elif male_partner == "AA" and female_partner == "BB" and embryo != "AB":
        is_miscall = True
    elif male_partner == "BB" and female_partner == "AB" and embryo != "AB":
        is_miscall = True
    elif (
        male_partner == "AA"
        and female_partner == "AB"
        and embryo
        not in [
            "AA",
            "AB",
        ]
    ):
        is_miscall = True
    elif (
        male_partner == "BB"
        and female_partner == "AB"
        and embryo
        not in [
            "BB",
            "AB",
        ]
    ):
        is_miscall = True
    elif (
        male_partner == "AB"
        and female_partner == "AA"
        and embryo
        not in [
            "AA",
            "AB",
        ]
    ):
        is_miscall = True
    elif (
        male_partner == "AB"
        and female_partner == "BB"
        and embryo
        not in [
            "BB",
            "AB",
        ]
    ):
        is_miscall = True
    return is_miscall


def check_df_for_miscalls(df):
    pass


is_miscall("AA", "BB", "BB")
