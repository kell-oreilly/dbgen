from playwright.sync_api import Playwright, APIRequestContext
from typing import Generator
<<<<<<< HEAD
import dbgen
=======
from databasegen import dbgen
from databasegen import apidbgen
>>>>>>> origin/dbgen_w_parameters
import pytest


@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url="http://127.0.0.1:5000/"
    )
    yield request_context
    request_context.dispose()


def test(api_request_context: APIRequestContext):
    #'Might have some setup, passing schema to API,
    # create json object representing schema
    response = api_request_context.get("schemas")  #RESTFULetc
    assert response.ok #200
    body = response.json()


def test_create_schema_success(api_request_context: APIRequestContext):
    #'/schemas/<string:schema_id>'
    test_schema = {
        "schema_name": "test",
        "fields": {
            "id": {"type": "id", "options": {}},
            "country": {"type": "country_code", "options": {}},
        }
    }
    schema_id = "test_id"
   # expected_response = 201
    schemas = {} # To ensure no duplicates
    response = api_request_context.post(f"/schemas/{schema_id}/schema", data=test_schema)
    assert response.status == 201

    
def test_create_schema_duplicate_id(api_request_context: APIRequestContext):
    test_schema = {
        "schema_name": "test",
        "fields": {
            "id": {"type": "id", "options": {}},
            "country": {"type": "country_code", "options": {}},
        }
    }
    schema_id = "test_id"
   # expected_response = 201
    schemas = {schema_id: test_schema} # new posted instance will be duplicate
    response = api_request_context.post(f"/schemas/{schema_id}/schema", data=test_schema)
    assert response.status == 400


def test_get_schemas(api_request_context: APIRequestContext):
    response = api_request_context.get('schemas')
    assert response.status == 200


#Working
def test_get_data_success(api_request_context: APIRequestContext):
    test_schema = {
        "schema_name": "test_id",
        "fields": {
            "id": {"type": "id", "options": {}},
            "country": {"type": "country_code", "options": {}},
        }
    }
    schema_id = "test_id"
    api_request_context.post(f"/schemas/{schema_id}/schema", data=test_schema)

    test_n_docs = 4
<<<<<<< HEAD
    response = api_request_context.get(f"/schemas/{schema_id}?{str(test_n_docs)}", data=test_schema)
   # response = client.get(f'/schemas/{schema_id}')
   # assert len(response.json()) == test_n_docs
=======
    response = api_request_context.get(f"/schemas/{schema_id}/schema?n_docs={test_n_docs}")

>>>>>>> origin/dbgen_w_parameters
    assert response.ok
    assert len(response.json()) == test_n_docs
    assert all(set(doc.keys()) == {"id", "country"} for doc in response.json())


def test_get_data_invalid_schema(api_request_context: APIRequestContext):
    response = api_request_context.get("/schemas/non_existent_schema/schema?n_docs=3")
    assert response.status == 404


def test_get_data_negative_docs(api_request_context: APIRequestContext):
    schema_id = "negative_docs"
    test_schema = {
        "schema_name": "test",
        "fields": {
            "id": {"type": "id", "options": {}},
            "country": {"type": "country_code", "options": {}},
        }
    }
    api_request_context.post(f"/schemas/{schema_id}/schema", data=test_schema)
    response = api_request_context.get(f"/schemas/{schema_id}/schema?n_docs=-5")
    assert response.status == 400
