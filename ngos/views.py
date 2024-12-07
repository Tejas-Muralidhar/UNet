from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .models import NGO
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import NGO
from .utils import get_recommendations


@csrf_exempt
def login_ngo(request):
    """Logs in the NGO."""
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")

        try:
            ngo = NGO.objects.get(email=email)
            if ngo.password == password:  # Replace this with secure password hashing in production
                request.session['ngo_id'] = ngo.id
                return JsonResponse({"message": "Login successful", "ngo_id": ngo.id}, status=200)
            return JsonResponse({"error": "Invalid password"}, status=401)
        except NGO.DoesNotExist:
            return JsonResponse({"error": "NGO not found"}, status=404)
    return JsonResponse({"error": "Only POST requests are allowed"}, status=405)


@login_required
def logout_ngo(request):
    """Logs out the NGO."""
    if request.session.get('ngo_id'):
        del request.session['ngo_id']
        return JsonResponse({"message": "Logged out successfully"}, status=200)
    return JsonResponse({"error": "No NGO logged in"}, status=400)


@csrf_exempt
@login_required
def update_ngo(request):
    """Updates the profile of the logged-in NGO."""
    if request.method == "PUT":
        ngo_id = request.session.get('ngo_id')
        if not ngo_id:
            return JsonResponse({"error": "No NGO logged in"}, status=400)

        try:
            ngo = NGO.objects.get(id=ngo_id)
            data = json.loads(request.body)
            ngo.name = data.get("name", ngo.name)
            ngo.mobile_number = data.get("mobile_number", ngo.mobile_number)
            ngo.email = data.get("email", ngo.email)
            ngo.address = data.get("address", ngo.address)
            ngo.contact_person = data.get("contact_person", ngo.contact_person)
            ngo.purpose = data.get("purpose", ngo.purpose)
            ngo.save()
            return JsonResponse({"message": "NGO profile updated successfully"}, status=200)
        except NGO.DoesNotExist:
            return JsonResponse({"error": "NGO not found"}, status=404)
    return JsonResponse({"error": "Only PUT requests are allowed"}, status=405)


@csrf_exempt
def create_ngo(request):
    """Registers a new NGO."""
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        mobile_number = data.get("mobile_number")
        email = data.get("email")
        address = data.get("address")
        contact_person = data.get("contact_person")
        purpose = data.get("purpose")
        password = data.get("password")

        if not all([name, mobile_number, email, address, contact_person, purpose, password]):
            return JsonResponse({"error": "All fields are required"}, status=400)

        if NGO.objects.filter(email=email).exists():
            return JsonResponse({"error": "Email already exists"}, status=400)

        ngo = NGO.objects.create(
            name=name,
            mobile_number=mobile_number,
            email=email,
            address=address,
            contact_person=contact_person,
            purpose=purpose,
            password=password  # Replace this with secure password hashing in production
        )
        return JsonResponse({"message": "NGO created successfully", "ngo_id": ngo.id}, status=201)
    return JsonResponse({"error": "Only POST requests are allowed"}, status=405)


@login_required
def view_ngo(request):
    """Returns all details of the logged-in NGO."""
    if request.method == "GET":
        ngo_id = request.session.get('ngo_id')
        if not ngo_id:
            return JsonResponse({"error": "No NGO logged in"}, status=400)

        try:
            ngo = NGO.objects.get(id=ngo_id)
            ngo_data = {
                "id": ngo.id,
                "name": ngo.name,
                "mobile_number": ngo.mobile_number,
                "email": ngo.email,
                "address": ngo.address,
                "contact_person": ngo.contact_person,
                "purpose": ngo.purpose,
            }
            return JsonResponse(ngo_data, status=200)
        except NGO.DoesNotExist:
            return JsonResponse({"error": "NGO not found"}, status=404)
    return JsonResponse({"error": "Only GET requests are allowed"}, status=405)


@api_view(['GET'])
def recommend_ngos(request):
    ngo_name = request.query_params.get('ngo_name', None)
    total_ngos = NGO.objects.count()
    print(ngo_name)
    if ngo_name==None:
        ngos = NGO.objects.all()[:total_ngos-1]
        top_ngos = [{'id': ngo.id, 'name': ngo.name} for ngo in ngos]
        return Response(top_ngos)

    recommendations = get_recommendations(ngo_name)
    
    if not recommendations:
        ngos = NGO.objects.all()[:total_ngos-1]
        top_ngos = [{'id': ngo.id, 'name': ngo.name} for ngo in ngos]
        return Response(top_ngos)

    return Response(recommendations)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import NGO

@api_view(['GET'])
def ngo_details(request, ngo_id):
    try:
        ngo = NGO.objects.get(id=ngo_id)
        return Response({
            'name': ngo.name,
            'purpose': ngo.purpose,
            'address': ngo.address,
            'contact_person': ngo.contact_person,
            'email': ngo.email,
            'mobile_number': ngo.mobile_number,
            'completed_project': ngo.completed_project,
            'ongoing_project': ngo.ongoing_project,
        })
    except NGO.DoesNotExist:
        return Response({"error": "NGO not found."}, status=404)
