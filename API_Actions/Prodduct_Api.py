from playwright.sync_api import expect

class ProductAPIActions:
    def __init__(self, api_context, logger):
        self.api_context = api_context
        self.logger = logger
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "*/*"
        }

    def get_all_product(self):
        self.logger.info("***** Sending GET Request to fetch all products List ******")
        response = self.api_context.get("/productsList")
        self.logger.info(f"API Response Status Code: {response.status}")
        return response

    def post_to_products_list(self):
        self.logger.info("Sending unsupported POST request to products list")
        response = self.api_context.post("/productsList")
        self.logger.info(f"API Response Status Code: {response.status}")
        return response

    def get_all_brands(self):
        self.logger.info("Sending GET request to fetch all brands list")
        response = self.api_context.get("/brandsList")
        return response
    
    def put_to_brands_list(self):
        self.logger.info("Sending unsupported PUT request to brands list")
        response = self.api_context.put("/brandsList")
        return response

    def search_product(self, product_name: str):
        self.logger.info(f"Triggering API 5: Searching product for keyword -> {product_name}")
        payload = {}
        if product_name:
            payload = {"search_product": product_name}
        
        response = self.api_context.post("/searchProduct", form=payload)
        return response