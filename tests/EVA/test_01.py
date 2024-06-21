import requests
import ast

def create_post():
    return {
        "UD": 1135, 
        "UR": 188, 
        "App": {
            "Name": "InfoBlox", 
            "Type":"Control" 
            }, 
            "jobInfo": [
                { 
                    "Search": [ 
                        { 
                            "SubNet": "10.130.148.0/22", 
                            "IP": "10.130.150.13" 
                        } 
                        ] 
                } 
                
            ] 
}


def test_create_post():

    # Replace with your actual endpoint and token
    url = 'https://jsonplaceholder.typicode.com/posts'
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiUmVzdFJ1biIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL2hhc2giOiI0MjI4MjIwMC03OWYzLTRmN2UtOGI3ZS1jYjgyNGFkZGU2YzEiLCJzdWIiOiJQb3dlclNoZWxsVW5pdmVyc2FsIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9yb2xlIjoiRXhlY3V0ZSIsIm5iZiI6MTY0OTM2NDk3NSwiZXhwIjoyMTA3Mjg0OTYwLCJpc3MiOiJJcm9ubWFuU29mdHdhcmUiLCJhdWQiOiJQb3dlclNoZWxsVW5pdmVyc2FsIn0.6Df6PZRdipuILPQRNCGy43_ZsBYtSmAHmwB0Vz-IS7s'

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'  # adjust content type as needed
    }

    # response = requests.post(url, json=create_post(), auth=api_token)
    response = requests.request("POST", url, headers=headers, json=create_post(), verify=False)

    if response.status_code == 201:  # Assuming the API returns 201 Created for successful POST
        # Verify response data
        response_data = response.json()  # Convert JSON response to Python dictionary

        # Example: Verify specific fields in the response data
        if 'id' in response_data:
            assert response.status_code == 201
            print(response.status_code == 201)
            assert isinstance(response.json()["id"], int) is True
            print(isinstance(response.json()["id"], int) is True)
        else:
            print('Unexpected response format. Missing "id" field.')

        # Additional verification based on your application logic

    else:
        print(f'Failed to create resource. Status code: {response.status_code}')
        print(f'Response Body: {response.text}')  # Print error response body if available




def search_item():
    return { 
        "UD": 1135,
        "UR": 188 
    } 



def test_get_body_response_with_value():

        # Replace with your actual endpoint and token
    url = 'https://vmcwnopas03.global.equinix.com/SearchJob'
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiUmVzdFJ1biIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL2hhc2giOiI0MjI4MjIwMC03OWYzLTRmN2UtOGI3ZS1jYjgyNGFkZGU2YzEiLCJzdWIiOiJQb3dlclNoZWxsVW5pdmVyc2FsIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9yb2xlIjoiRXhlY3V0ZSIsIm5iZiI6MTY0OTM2NDk3NSwiZXhwIjoyMTA3Mjg0OTYwLCJpc3MiOiJJcm9ubWFuU29mdHdhcmUiLCJhdWQiOiJQb3dlclNoZWxsVW5pdmVyc2FsIn0.6Df6PZRdipuILPQRNCGy43_ZsBYtSmAHmwB0Vz-IS7s'

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'  # adjust content type as needed
    }

    response = requests.request("GET", url, headers=headers, json=search_item(), verify=False)

    if response.status_code == 201:  # Assuming the API returns 201 Created for successful POST
    # Verify response data
        try:
            response_data = response.json()  # Convert JSON response to Python dictionary
            
            # Example: Verify specific fields in the response data
            if isinstance(response_data, dict):  # Ensure response_data is a dictionary
                print(f'Post created with ID: {response_data["id"]}')
                print(f'Title: {response_data["title"]}')
                print(f'Body: {response_data["body"]}')
                print(f'UserID: {response_data["userId"]}')
            else:
                print('Unexpected response format. Response data is not a dictionary.')

        except ValueError:
            print('Response content is not valid JSON.')
    else:
        print(f'Failed to create resource. Status code: {response.status_code}')
        print(f'Response Body: {response.text}')  # Print error response body if available


def search_item():
    return { 
        "_id": 81
        } 



def test_get_jobdata_by_ID():

        # Replace with your actual endpoint and token
    url = 'https://vmcwnopas03.global.equinix.com/JobData'
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiUmVzdFJ1biIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL2hhc2giOiI0MjI4MjIwMC03OWYzLTRmN2UtOGI3ZS1jYjgyNGFkZGU2YzEiLCJzdWIiOiJQb3dlclNoZWxsVW5pdmVyc2FsIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9yb2xlIjoiRXhlY3V0ZSIsIm5iZiI6MTY0OTM2NDk3NSwiZXhwIjoyMTA3Mjg0OTYwLCJpc3MiOiJJcm9ubWFuU29mdHdhcmUiLCJhdWQiOiJQb3dlclNoZWxsVW5pdmVyc2FsIn0.6Df6PZRdipuILPQRNCGy43_ZsBYtSmAHmwB0Vz-IS7s'

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'  # adjust content type as needed
    }

    response = requests.request("GET", url, headers=headers, json=search_item(), verify=False)

    if response.status_code == 201:  # Assuming the API returns 201 Created for successful POST
    # Verify response data
        try:
            response_data = response.json()  # Convert JSON response to Python dictionary
            
            # Example: Verify specific fields in the response data
            if isinstance(response_data, dict):  # Ensure response_data is a dictionary
                print(f'Post created with ID: {response_data["id"]}')
                print(f'Title: {response_data["title"]}')
                print(f'Body: {response_data["body"]}')
                print(f'UserID: {response_data["userId"]}')
            else:
                print('Unexpected response format. Response data is not a dictionary.')

        except ValueError:
            print('Response content is not valid JSON.')
    else:
        print(f'Failed to create resource. Status code: {response.status_code}')
        print(f'Response Body: {response.text}')  # Print error response body if available



def search_item_to_delete():
    return {  
        "_id": 81,
        "UD": 1135,
        "UR": 188,
        "App": "InfoBlox"
    } 




def test_remove_job():

        # Replace with your actual endpoint and token
    url = 'https://vmcwnopas03.global.equinix.com/RemoveJob'
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiUmVzdFJ1biIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL2hhc2giOiI0MjI4MjIwMC03OWYzLTRmN2UtOGI3ZS1jYjgyNGFkZGU2YzEiLCJzdWIiOiJQb3dlclNoZWxsVW5pdmVyc2FsIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9yb2xlIjoiRXhlY3V0ZSIsIm5iZiI6MTY0OTM2NDk3NSwiZXhwIjoyMTA3Mjg0OTYwLCJpc3MiOiJJcm9ubWFuU29mdHdhcmUiLCJhdWQiOiJQb3dlclNoZWxsVW5pdmVyc2FsIn0.6Df6PZRdipuILPQRNCGy43_ZsBYtSmAHmwB0Vz-IS7s'

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'  # adjust content type as needed
    }

    response = requests.request("DELETE", url, headers=headers, json=search_item_to_delete(), verify=False)
 
    if response.status_code == 200:  # Assuming the API returns 200 OK for successful DELETE

        print(response.text)
        response_data = '''response.text'''

    # Verify response data
        try:
            # Parse JSON string into a dictionary
            response_dict = json.loads(response_data)
            
            job_id = response_data['Job']['_id']
            application = response_data['Job']['App']

            print(f'Job ID: {job_id}')
            print(f'Application: {application}')

        except KeyError as e:
            print(f'Error: Key not found - {e}')
    else:
        print(f'Failed to create resource. Status code: {response.status_code}')
        print(f'Response Body: {response.text}')  # Print error response body if available
