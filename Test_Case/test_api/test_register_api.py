import pytest
import random
from Utilities.Read_Env import ReadEnv

class TestUserRegistrationAPI:

    def test_success_user_registration(self, user_api):
        random_id = random.randint(1000, 9999)
        test_email = f"bimalesh_api_{random_id}@gmail.com"
        password = "Bimalesh@2026"

        #Get from env
        #test_email = ReadEnv.get_email()
        #password = ReadEnv.get_password()

        #CREATE USER (POST)
        payload = {
            "name": "Bimalesh Automation",
            "email": test_email,
            "password": password,
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

        #print("API Response JSON:", response_data) 
        assert response_data.get("responseCode") == 201, f"Expected API responseCode 201, got {response_data.get('responseCode')}"
        assert response_data.get("message") == "User created!", "Success message mismatch in API response!"
        print("\n: User Created Successfully!")


        #GET USER DETAILS (GET)
        get_res = user_api.get_user_details(test_email)
        assert get_res.status == 200
        assert get_res.json().get("responseCode") == 200
        assert get_res.json().get("user").get("name") == "Bimalesh Automation"
        print(" User Details Verified via GET API!")

        #UPDATE USER ACCOUNT (PUT)
        updated_payload = payload.copy()
        updated_payload["name"] = "Bimalesh Kumar Yadav"

        update_res = user_api.update_user_account(updated_payload)
        assert update_res.status == 200
        assert update_res.json().get("responseCode") == 200
        assert update_res.json().get("message") == "User updated!"
        print("User Details Updated via PUT API!")

        #DELETE USER ACCOUNT
        delete_res = user_api.delete_user_account(test_email, password)

        assert delete_res.status == 200
        assert delete_res.json().get("responseCode") == 200
        assert delete_res.json().get("message") == "Account deleted!"
        print(" User Account Deleted via DELETE API!")







