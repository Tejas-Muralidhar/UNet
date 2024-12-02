from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from ngos.models import NGO
from users.models import User
from .models import Donation
import json


@csrf_exempt
def show_form(request):
    """Returns a JSON response containing donation form details or Razorpay integration."""
    if request.method == "GET":
        # Example structure for a donation form. Modify as per Razorpay integration or requirements.
        form_details = {
            "fields": {
                "user_id": "integer",
                "ngo_id": "integer",
                "amount": "decimal",
            },
            "payment_gateway": "Razorpay",
            "instructions": "Fill out the form and proceed to payment.",
        }
        return JsonResponse(form_details, status=200)
    return JsonResponse({"error": "Only GET requests are allowed"}, status=405)


@login_required
def list_user_donations(request):
    """Returns all donations made by the logged-in user."""
    if request.method == "GET":
        user = request.user
        donations = Donation.objects.filter(user_id=user.id)
        donation_list = [
            {
                "id": donation.id,
                "ngo_id": donation.ngo_id,
                "ngo_name": donation.ngo.name,
                "date": donation.date,
                "amount": donation.amount,
            }
            for donation in donations
        ]
        return JsonResponse({"donations": donation_list}, status=200)
    return JsonResponse({"error": "Only GET requests are allowed"}, status=405)


@login_required
def list_ngo_donations(request, ngo_id):
    """Returns all donations made to a particular NGO."""
    if request.method == "GET":
        try:
            ngo = NGO.objects.get(id=ngo_id)
            donations = Donation.objects.filter(ngo_id=ngo.id)
            donation_list = [
                {
                    "id": donation.id,
                    "user_id": donation.user_id,
                    "user_name": donation.user.name,
                    "date": donation.date,
                    "amount": donation.amount,
                }
                for donation in donations
            ]
            return JsonResponse(
                {"ngo_name": ngo.name, "donations": donation_list}, status=200
            )
        except NGO.DoesNotExist:
            return JsonResponse({"error": "NGO not found"}, status=404)
    return JsonResponse({"error": "Only GET requests are allowed"}, status=405)
