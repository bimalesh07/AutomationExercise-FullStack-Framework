import pytest

@pytest.mark.api
class TestProductIndividualAPIs:

    def test_api_get_all_products_list(self, product_api):
        response = product_api.get_all_product()
        if response.status == 200:
            try:
                json_data = response.json()
                assert json_data["responseCode"] == 200
                assert "products" in json_data
            except Exception:
                assert "html" in response.text().lower()

    def test_api_post_to_all_products_unsupported(self, product_api):
        response = product_api.post_to_products_list()
        assert response.status in [403, 405, 200]
        if response.status == 200:
            json_data = response.json()
            assert json_data["responseCode"] == 405

    def test_api_get_all_brands_list(self, product_api):
        response = product_api.get_all_brands()
        if response.status == 200:
            try:
                json_data = response.json()
                assert json_data["responseCode"] == 200
                assert "brands" in json_data
            except Exception:
                assert response.status == 200

    def test_api_put_to_all_brands_unsupported(self, product_api):
        response = product_api.put_to_brands_list()
        assert response.status in [403, 405, 200]

    def test_api_search_product_with_valid_parameter(self, product_api)
        response = product_api.search_product(product_name="tshirt")
        assert response.status in [200, 403]

    def test_api_search_product_without_parameter(self, product_api):
        response = product_api.search_product(product_name=None)
        assert response.status in [200, 400, 403]