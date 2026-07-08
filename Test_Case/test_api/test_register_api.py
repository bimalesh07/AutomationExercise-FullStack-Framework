import pytest
import random

class TestUserRegistrationAPI:

    def test_success_user_registration(self, user_api):
        random_id = random.randint(1000, 9999)
        test_email = f"bimalesh_api_{random_id}@gmail.com"
    
        payload = {
            "name": "Bimalesh Automation",
            "email": test_email,
            "password": "SecurePassword123",
            "title": "Mr",
            "birth_date": "15",
            "birth_month": "08",
            "birth_year": "1997",
            "firstname": "Bimalesh",
            "lastname": "Kumar",
            "company": "QA Tech",
            "address1": "123 Tech Park",
            "country": "India",
            "zipcode": "560001",
            "state": "Karnataka",
            "city": "Bangalore",
            "mobile_number": "9876543210"
        }

        response = user_api.create_user_account(payload)
        assert response.status == 200, f"Expected 200, but got {response.status}"
        response_data = response.json()


        print("API Response JSON:", response_data) 
        assert response_data.get("responseCode") == 201, f"Expected API responseCode 201, got {response_data.get('responseCode')}"
        assert response_data.get("message") == "User created!", "Success message mismatch in API response!"