from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from requests import Response
from rest_framework.decorators import api_view
import json
from ngos.models import NGO
from donations.models import Donation
from users.models import User

import requests

@csrf_exempt
@api_view(['POST'])
def initiate_payment(request):

    print("Received a request")
    print("Handling POST request")
    body = json.loads(request.body)
    card_number = body.get('card_number')
    cvv = body.get('cvv')
    amount = body.get('amount')
    expiry_date = body.get('expiry_date')
    name = body.get('name')
    ngo_id = body.get('ngo_id')
    user_email = body.get('user_email')

    print(ngo_id)
    print(user_email)

    processor_response = {}

    #get ngo id also from frontend. which ngo i want to give money to?
    #get into ngo table and retrieve it's account number

    try:
        # Decrypt the fields
        # card_number = decrypt_aes_data(encrypted_card_number)
        # cvv = decrypt_aes_data(encrypted_cvv)
        # amount = decrypt_aes_data(encrypted_amount)

        ngos = NGO.objects.filter(id=ngo_id)
        for ngo in ngos:
            account_number = ngo.account_number
        print(account_number)
        
        if card_number and cvv and amount and expiry_date and name and account_number:
            # Send the payment data to the mock payment processor
            
            try:
                processor_response = requests.post(
                    "http://localhost:5000/api/processor/initiate-payment/",
                    json={
                        'card_number': card_number,
                        'cvv': cvv,
                        'amount': amount,
                        'name' : name,
                        'expiry_date': expiry_date,
                        'ngo_account_number' : account_number
                    },
                    timeout=10  # Set a timeout for the request
                )

                # Log the response from the payment processor
                print(f"Payment Processor Response: {processor_response.json()}")

                if processor_response.status_code == 200:
                    # record the donation
                    user = User.objects.filter(email = user_email).first()
                    ngo = NGO.objects.filter(id = ngo_id).first()
                    Donation(ngo_id = ngo, user_id = user, amount = amount).save()

                    return JsonResponse(
                        {
                            'message': 'Payment successful!',
                            'details': processor_response.json()
                        },
                        status=200
                    )
                else:
                    return JsonResponse(
                        {
                            'message': 'Payment failed!',
                            'details': processor_response.json()
                        },
                        status=processor_response.status_code
                    )

            except requests.RequestException as e:
                print(f"Error communicating with the payment processor: {e}")
                return JsonResponse({'message': 'Payment processor error', 'error': str(e)}, status=500)

        else:
            return JsonResponse({'message': 'Invalid payment details'}, status=400)

    except json.JSONDecodeError:
        return JsonResponse({'message': 'Invalid JSON format'}, status=400)