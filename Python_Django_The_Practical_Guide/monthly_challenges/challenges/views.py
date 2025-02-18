from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("monthly-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)



def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    redirect_path = reverse("monthly-challenge", args=[redirect_month])  # /challenge/january
    return HttpResponseRedirect(redirect_path)


# noinspection PyBroadException
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        return HttpResponseNotFound("<h1>Sorry, that month is not supported!</h1>")
