
class UserAPIActions:

    def __init__(self, api_context, logger):
        self.api_context = api_context
        self.logger = logger

    #Create User
    def create_user_account(self, payload):
        self.logger.info("Sending POST Request to Create User Account ---")
        response = self.api_context.post("createAccount", form=payload)
        self.logger.info(f"API Response Status Code: {response.status}")
        return response

    #Get User Details
    def get_user_details(self, email):
        self.logger.info(f"-------Sending Get Request For user:{email}")
        response = self.api_context.get("getUserDetailByEmail",params={"email": email})
        self.logger.info(f"API Response Status code:{response.status}")
        return response
    
    #Update User Account (PUT Request)
    def update_user_account(self, payload):
        self.logger.info(f"----Sending PUT Request to update User Account")
        response = self.api_context.put("updateAccount", form=payload)
        self.logger.info(f"API Response Satus Code: {response.status}")
        return response
    
    # Delete User Account (DELETE Request)
    def delete_user_account(self, email, password):
        self.logger.info(f"--- Sending DELETE Request for User: {email} ---")
        delete_payload = {"email": email, "password": password}
        response = self.api_context.delete("deleteAccount", form=delete_payload)
        self.logger.info(f"API Response Status Code: {response.status}")
        return response

    
    def verify_login(self, email=None, password=None, invalid_method=False):
        self.logger.info(f"Triggering Login Verification API for Email: {email}")
        payload = {}

        if email is not None:
            payload["email"] = email

        if password is not None:
            payload["password"] = password

        if invalid_method:
            response = self.api_context.delete("/verifyLogin", headers=self.headers)
            
        else:
            response = self.api_context.post("/verifyLogin", form=payload, headers=self.headers)
            
        return response

