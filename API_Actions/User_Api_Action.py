# API_Actions/User_Api_Action.py

class UserAPIActions:
    def __init__(self, api_context, logger):
        self.api_context = api_context
        self.logger = logger

    def create_user_account(self, payload):
        self.logger.info("Sending POST Request to Create User Account ---")
    
        response = self.api_context.post("createAccount", form=payload)
        
        self.logger.info(f"API Response Status Code: {response.status}")
        return response