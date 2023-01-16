# Covid-19 screening questions and suggestions based on input


def validator(t, f, d, h):
    # reference
    isvalid = ['Y', 'N']

    # comparator
    if t in isvalid and f in isvalid and d in isvalid and h in isvalid:
        # tiredness selector
        if t == "Y":
            t = True
        elif t == "N":
            t = False

        # fever selector
        if f == "Y":
            f = True
        elif f == "N":
            f = False

        # dry cough selector
        if d == "Y":
            d = True
        elif d == "N":
            d = False

        # high temperature selector
        if h == "Y":
            h = True
        elif h == "N":
            h = False

        # array of answers. i.e [tiredness, fever, dry_cough, high_temp]
        answer = [i for i in [t, f, d, h]]
        print('\n')
        return suggestions(answer[0], answer[1], answer[2], answer[3])

    else:
        print("Invalid inputs entered try again")
        print('\n')
        questionnaire()


# suggestion depending on input
def suggestions(tiredness, fever, dry_cough, high_temp):
    if tiredness and fever and dry_cough and high_temp:
        print("Warning, you have severe symptoms of COVID-19, Please test for COVID-19")
    elif tiredness and fever and dry_cough and not high_temp:
        print("Warning, you have multiple common symptoms of COVID-19, Please test for COVID-19 ASAP")
    elif tiredness and fever and not dry_cough and high_temp:
        print("Warning, you have multiple common symptoms of COVID-19, Please test for COVID-19")
    elif tiredness and not fever and dry_cough and high_temp:
        print("Warning, you have multiple common symptoms of COVID-19, Please test for COVID-19")
    elif fever and not tiredness and dry_cough and high_temp:
        print("Warning, you have multiple common symptoms of COVID-19, Please test for COVID-19")
    elif dry_cough and not tiredness and not fever and not high_temp:
        print("You don't have COVID-19 symptoms, Treat dry cough")
    elif tiredness and not dry_cough and not fever and not high_temp:
        print("You don't have COVID-19 symptoms")
    elif fever and not tiredness and not dry_cough and not high_temp:
        print("You don't have COVID-19 symptoms")
    elif not fever and not tiredness and not dry_cough and not high_temp:
        print("You don't have COVID-19 symptoms, take fever medication")
    elif high_temp and not tiredness and not fever and not dry_cough:
        print("Wear loose clothes, keep moderate room temperature, drink more fluid and avoid alcohol")
    elif high_temp and fever and not tiredness and not dry_cough:
        print("Wear loose clothes, keep moderate room temperature, drink more fluid and avoid alcohol. Take fever "
              "medication")
    else:
        print("You have symptoms of Covid_19, Please quarantine for approximately 14 days")


# inputs and calling comparator
def questionnaire():
    h = input("Are you feeling tired? Y = YES or N = NO?: ").upper()
    j = input("Do you have fever? Y = YES or N = NO?: ").upper()
    k = input("Do you have dry couch? Y = YES or N = NO?: ").upper()
    z = input("Is your body temperature high? Y = YES or N = NO?: ").upper()
    validator(h, j, k, z)


if __name__ == "__main__":
    questionnaire()
