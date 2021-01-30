
#  не е хубаво да се набивт много ретурни, но ако функ е достатъчно проста е ок да има няколко ретурна
#  след ретурн изпълнението на функ, приключва. даваме стойност на резулт
# защото ако имаме число извън обхвата дава еррор че ресулт не съществува


def evaluation(grade):
    result = None
    if 2 <= grade < 3:
        result = "Fail"
    elif 3 <= grade < 3.50:
        result = "Poor"
    elif 3.50 <= grade < 4.50:
        result = "Good"
    elif 4.50 <= grade < 5.50:
        result = "Very Good"
    elif 5.50 <= grade <= 6:
        result = "Excellent"
    return result


grade = float(input())
print(evaluation(grade))
