from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from .models import User
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_user(request):
    """Logs in the user."""
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"message": "Login successful"}, status=200)
        return JsonResponse({"error": "Invalid credentials"}, status=401)
    return JsonResponse({"error": "Only POST requests are allowed"}, status=405)


@login_required
def logout_user(request):
    """Logs out the user."""
    logout(request)
    return JsonResponse({"message": "Logged out successfully"}, status=200)


@csrf_exempt
@login_required
def update_user(request):
    """Edits the profile of the logged-in user."""
    if request.method == "PUT":
        user = request.user
        data = json.loads(request.body)
        user.name = data.get("name", user.name)
        user.email = data.get("email", user.email)
        if data.get("password"):
            user.password = make_password(data.get("password"))
        user.save()
        return JsonResponse({"message": "Profile updated successfully"}, status=200)
    return JsonResponse({"error": "Only PUT requests are allowed"}, status=405)


@csrf_exempt
def create_user(request):
    """Registers a new user."""
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        if not name or not email or not password:
            return JsonResponse({"error": "All fields are required"}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({"error": "Email already exists"}, status=400)
        user = User.objects.create(
            name=name, email=email, password=make_password(password)
        )
        return JsonResponse({"message": "User created successfully", "user_id": user.id}, status=201)
    return JsonResponse({"error": "Only POST requests are allowed"}, status=405)


@login_required
def view_user(request):
    """Returns a detailed view of the profile of the logged-in user."""
    if request.method == "GET":
        user = request.user
        user_data = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "date_joined": user.date_joined,
            "last_login": user.last_login,
        }
        return JsonResponse(user_data, status=200)
    return JsonResponse({"error": "Only GET requests are allowed"}, status=405)
