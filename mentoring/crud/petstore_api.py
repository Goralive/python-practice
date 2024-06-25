import requests
import logging

BASE_URL = "https://petstore.swagger.io/v2"

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class PetStoreAPIClient:
    def get_pet_by_id(self, pet_id):
        try:
            response = requests.get(f"{BASE_URL}/pet/{pet_id}")
            response.raise_for_status()
            pet_data = response.json()
            return {
                "id": pet_data["id"],
                "name": pet_data["name"],
                "status": pet_data["status"],
            }
        except requests.RequestException as e:
            logging.error(f"Error fetching pet data for ID {pet_id}: {e}")
            return None

    def add_pet(self, pet_data):
        try:
            response = requests.post(f"{BASE_URL}/pet", json=pet_data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error adding pet: {e}")
            return False

    def update_pet(self, pet_id, pet_data):
        try:
            response = requests.put(f"{BASE_URL}/pet", json=pet_data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error updating pet with ID {pet_id}: {e}")
            return False

    def delete_pet(self, pet_id):
        try:
            response = requests.delete(f"{BASE_URL}/pet/{pet_id}")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error deleting pet with ID {pet_id}: {e}")
            return False
