# from mixed array, search for possible suggestions based on the input and sort the results


def suggested(new_names, search):
    suggestions = []
    for name in new_names:
        if name[0:].lower().startswith(search[0:].lower()):
            suggestions.append(name)
    suggestions.sort()
    return suggestions


if __name__ == "__main__":
    given = ['ishmael RAs', 'IshMael rasal', 'Kgao', 'KGAO', 'KGaO', 'IsH', 'Kgaogelo', 'K1Gaogelo', 'K2GAOG', 'IsH123',
             'KgaOG', 'IshM123', 'Ishm123', '1992', '1999', '2003', '2000', 'ishmael rasala', 'ishmael ra']
    new_given = given.copy()
    my_search = input("Enter search word: ")
    print(suggested(new_given, my_search))
