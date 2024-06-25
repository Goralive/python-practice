import unittest
import requests
from crud import petstore_api


class TestPetStoreAPIClient(unittest.TestCase):
    def test_get_pet_by_id_success(self):
        pet_data = {"id": 932, "name": "Dog", "status": "available"}
        petstore_client = petstore_api.PetStoreAPIClient()
        pet_response = petstore_client.add_pet(pet_data)
        actual_get_response = petstore_client.get_pet_by_id(pet_response["id"])

        self.assertIsNotNone(pet_data)
        self.assertEqual(pet_data["id"], actual_get_response["id"])
        self.assertEqual(pet_data["name"], "Dog")
        self.assertEqual(pet_data["status"], "available")

    def test_add_pet_success(self):
        pet_data = {"id": 800, "name": "Dog", "status": "available"}
        petstore_client = petstore_api.PetStoreAPIClient()
        result = petstore_client.add_pet(pet_data)

        self.assertEqual(pet_data["id"], result["id"])
        self.assertEqual(pet_data["name"], result["name"])
        self.assertEqual(pet_data["status"], result["status"])

    def test_update_pet_success(self):
        create_pet = {"id": 800, "name": "Dog", "status": "available"}
        petstore_client = petstore_api.PetStoreAPIClient()
        created = petstore_client.add_pet(create_pet)

        pet_id = created["id"]
        update_pet = {"id": pet_id, "name": "Cat", "status": "sold"}
        result = petstore_client.update_pet(pet_id, update_pet)

        # Then
        self.assertEqual(update_pet["id"], result["id"])
        self.assertEqual(update_pet["name"], result["name"])
        self.assertEqual(update_pet["status"], result["status"])

    def test_delete_pet_success(self):
        # Given
        pet_id = "345"
        pet_data = {"id": pet_id, "name": "Cat", "status": "sold"}
        status_code_ok = 200
        petstore_client = petstore_api.PetStoreAPIClient()
        petstore_client.add_pet(pet_data)
        # When
        result = petstore_client.delete_pet(pet_id)
        # Then
        self.assertEqual(result["code"], status_code_ok)
        self.assertEqual(result["message"], pet_id)


if __name__ == "__main__":
    unittest.main()
