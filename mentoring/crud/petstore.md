## PetStore API Client Implementation

URL = https://petstore.swagger.io/#/

1. Install and import requests to you
2. Implements methods to get and parse response (id, name, status)
3. Implement test (feel free to use Pytest or unittest). Each method should be covered at least with one test
4. Handle errors

Optional tasks:

- Add loging
- On pet creation add pet to list or file
- On pet deletion delete pet from list or file

<details>
<summary>Step by step</summary>

**Step 1:**

- Define the PetStoreAPIClient Class
- Create a class named PetStoreAPIClient.
- This class will contain methods for interacting with the PetStore API, such as get_pet_by_id, add_pet, update_pet, and
  delete_pet.

**Step 2:**

- Implement the get_pet_by_id Method
- This method takes a pet_id as input and retrieves the details of the pet with the specified ID from the PetStore API.
- Use the requests.get() function to make a GET request to the appropriate endpoint of the PetStore API.
- Parse the JSON response and return the pet data in a dictionary format containing id, name, and status attributes.
- Handle any exceptions that may occur during the request, such as network errors or HTTP errors, and log them
  appropriately.

**Step 3:**

- Implement the add_pet Method
- This method takes pet_data as input, which is a dictionary containing the details of the pet to be added.
- Use the requests.post() function to make a POST request to the appropriate endpoint of the PetStore API, including the
  pet_data in JSON format in the request body.
- Parse the JSON response and return it.
- Handle any exceptions that may occur during the request and log them appropriately.

**Step 4:**

- Implement the update_pet Method
- This method takes pet_id and pet_data as input, where pet_data is a dictionary containing the updated details of the
  pet.
- Use the requests.put() function to make a PUT request to the appropriate endpoint of the PetStore API, including the
  pet_data in JSON format in the request body.
- Parse the JSON response and return it.
- Handle any exceptions that may occur during the request and log them appropriately.
 
**Step 5:** 

- Implement the delete_pet Method
- This method takes pet_id as input and deletes the pet with the specified ID from the PetStore API.
- Use the requests.delete() function to make a DELETE request to the appropriate endpoint of the PetStore API.
- Parse the JSON response and return it.
- Handle any exceptions that may occur during the request and log them appropriately.

</details>