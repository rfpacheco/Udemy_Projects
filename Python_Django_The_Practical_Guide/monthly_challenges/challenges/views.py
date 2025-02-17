from django.http import HttpResponse, HttpResponseNotFound

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Read one book throughout the month!",
    "may": "Practice meditation for 10 minutes a day!",
    "june": "Drink at least 8 glasses of water daily!",
    "july": "Try a new recipe every week!",
    "august": "Go to bed by 10 PM every night!",
    "september": "Write in a journal every day!",
    "october": "Declutter your space and donate unused items!",
    "november": "Exercise for 30 minutes every day!",
    "december": "Spend quality time with family and friends!"
}

def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


# noinspection PyBroadException
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("Sorry, that month is not available yet.")

    return HttpResponse(challenge_text)