from playwright.sync_api import expect

class ProductAPIActions:
    def __init__(self, api_context, logger):
        self.api_context = api_context
        self.logger = logger

    def get_all_product(self):
        self.logger("*****Sending GET Request to fetch all products List******")
        response = self.api_context.get("productsList")
        self.logger.info(f"API Response Status Code: {response.status}")
        return response

    def post_to_products_list(self):
        self.logger.info("Sending unsupported POST request to products list")
        response = self.api_context.post("productList")
        self.logger.info(f"API Response Status Code: {response.status}")
        return response

    def get_all_brands(self):
        self.logger.info("Sending GET request to fetch all brands list")
        respone = self.api_context.get("brandsList")
        return respone
    
    def put_to_brands_list(self):
        self.logger.info("Sending unsupported PUT request to brands list")
        response = self.api_context.put("/brandsList")

    def search_product(self, product_name:str):
        self.logger.info(f"Triggering API 5: Searching product for keyword -> {product_name}")
        

    

    


        