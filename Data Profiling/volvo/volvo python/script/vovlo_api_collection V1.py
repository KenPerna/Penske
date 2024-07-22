import os
import requests
import json
import time
from requests.auth import HTTPBasicAuth
from datetime import datetime
from dotenv import load_dotenv
from urllib3.exceptions import InsecureRequestWarning

# Disable Request Warning in Log
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Load environment variables from the .env file (if present)
load_dotenv()

# Access environment variables as if they came from the actual environment
TOKEN_URL = os.getenv('token_url')
USERNAME = os.getenv('user_name')
PASSWORD = os.getenv('password')

VOLVO_LOCATION_URL = os.getenv('volvo_location_url')
VOLVO_VEST_URL = os.getenv('volvo_vest')
VOLVO_VEHICLE_STATUS_URL = os.getenv('volvo_vehicle_status')
VOLVO_FAULT_STATUS_URL = os.getenv('volvo_fault_status')
VOLVO_FAULT_ALARM_URL = os.getenv('volvo_fault_alarm')


def get_volvo_token():
    
    response = {}
    try:
        response = requests.get(TOKEN_URL, auth=HTTPBasicAuth(USERNAME, PASSWORD),verify=False)
    except Exception as e:
        print('Failed to retrieve Token. Status code:', response.status_code, 'Response:', response.text)
        
    return response

def get_location_data(token_response):
    
    # Check the response status and print the data
    if token_response.status_code == 200:
        data = token_response.json()
        api_key = data.get('accessToken')
        
        # Set up headers with the API key
        if api_key:
            headers = {
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            }
        else:
            print(f'can not create header for requesting location data as token is missing')
            result = {'Status code': 400, 'Reason': 'Failed to send request for location data'}

        # Make a GET request to the API endpoint
        volvo_location_response = requests.get(VOLVO_LOCATION_URL, headers=headers, verify=False)

        # Check the response status and print the data
        if volvo_location_response.status_code == 200:
            location_data = volvo_location_response.json()
            # print('volvo location data retrieved successfully:', location_data)

            if location_data.get('messageCount') != 0:
                # Specify the file path where you want to save the JSON data
                path = os.getcwd()
                sample_collection_path = '\\Data Profiling\\volvo\\volvo python\\volvo sample responses'
                location_api_path = '\\volvo-location\\'

                now = datetime.now()
                formatted_datetime = now.strftime("%Y-%m-%d_%H-%M-%S")
                filename = f"volvo-location_{formatted_datetime}.json"
                
                file_path = path + sample_collection_path + location_api_path + filename

                # Save the data to a JSON file
                with open(file_path, 'w') as json_file:
                    json.dump(location_data, json_file, indent=4)

                result = {'Status code': volvo_location_response.status_code, 'Reason': 'successfully received location data and saved in file'}
            else:
                result = {'Status code': volvo_location_response.status_code, 'Reason': 'Number of message count is 0'}
                print('Number of message is 0 so, not storing sample source message for location')
        else:
            print('Failed to retrieve location data. Status code:', volvo_location_response.status_code, 'Response:', volvo_location_response.text)
            result = {'Status code': volvo_location_response.status_code, 'Reason': 'Failed to retrieve location data'}
    return result

def get_vehicle_status_data(token_response):
    
    # Check the response status and print the data
    if token_response.status_code == 200:
        data = token_response.json()
        api_key = data.get('accessToken')
        
        # Set up headers with the API key
        if api_key:
            headers = {
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            }
        else:
            print(f'can not create header for requesting vehicle status data as token is missing')
            result = {'Status code': 400, 'Reason': 'Failed to send request for vehicle status data'}

        # Make a GET request to the API endpoint
        volvo_vehicle_status_response = requests.get(VOLVO_VEHICLE_STATUS_URL, headers=headers, verify=False)

        # Check the response status and print the data
        if volvo_vehicle_status_response.status_code == 200:
            vehicle_status_data = volvo_vehicle_status_response.json()
            
            # Specify the file path where you want to save the JSON data
            path = os.getcwd()
            sample_collection_path = '\\Data Profiling\\volvo\\volvo python\\volvo sample responses'
            vehiclestatus_path = '\\volvo-vehicleStatus\\'

            now = datetime.now()
            formatted_datetime = now.strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"volvo-vehicleStatus_{formatted_datetime}.json"
            
            file_path = path + sample_collection_path + vehiclestatus_path + filename

            # Save the data to a JSON file
            with open(file_path, 'w') as json_file:
                json.dump(vehicle_status_data, json_file, indent=4)

            result = {'Status code': volvo_vehicle_status_response.status_code, 'Reason': 'successfully received vehicleStatus data and saved in file'}
        else:
            print('Failed to retrieve vehicleStatus data. Status code:', volvo_vehicle_status_response.status_code, 'Response:', volvo_vehicle_status_response.text)
            result = {'Status code': volvo_vehicle_status_response.status_code, 'Reason': 'Failed to retrieve vehicleStatus data'}
    return result

def get_fault_status_data(token_response):
    
    # Check the response status and print the data
    if token_response.status_code == 200:
        data = token_response.json()
        api_key = data.get('accessToken')
        
        # Set up headers with the API key
        if api_key:
            headers = {
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            }
        else:
            print(f'can not create header for requesting vehicle status data as token is missing')
            result = {'Status code': 400, 'Reason': 'Failed to send request for vehicle status data'}

        # Make a GET request to the API endpoint
        volvo_fault_status_response = requests.get(VOLVO_FAULT_STATUS_URL, headers=headers, verify=False)

        # Check the response status and print the data
        if volvo_fault_status_response.status_code == 200:
            fault_status_data = volvo_fault_status_response.json()
            
            # Specify the file path where you want to save the JSON data
            path = os.getcwd()
            sample_collection_path = '\\Data Profiling\\volvo\\volvo python\\volvo sample responses'
            vehiclestatus_path = '\\volvo-faultStatus\\'

            now = datetime.now()
            formatted_datetime = now.strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"volvo-faultStatus_{formatted_datetime}.json"
            
            file_path = path + sample_collection_path + vehiclestatus_path + filename

            # Save the data to a JSON file
            with open(file_path, 'w') as json_file:
                json.dump(fault_status_data, json_file, indent=4)

            result = {'Status code': volvo_fault_status_response.status_code, 'Reason': 'successfully received vehicleStatus data and saved in file'}
        else:
            print('Failed to retrieve faultstatus data. Status code:', volvo_fault_status_response.status_code, 'Response:', volvo_fault_status_response.text)
            result = {'Status code': volvo_fault_status_response.status_code, 'Reason': 'Failed to retrieve faultStatus data'}
    return result


if __name__ == '__main__':
    
    for i in range(1,100):
    
        print(f"****************************************************")
        print(f"runniug call # {i}")
        if i % 2:
            # For odd Iteration
            token_response = get_volvo_token()
        
        if token_response != {}:     
            location_result = get_location_data(token_response)
            print(f"Location result status is {location_result}")

            faultstatus_result = get_fault_status_data(token_response)
            print(f"FaultStatus result status is {faultstatus_result}")

            # vehiclestatus_result = get_vehicle_status_data(token_response)
            # print(f"VehicleStatus result status is {vehiclestatus_result}")

        # wait for 5 mins before next call
        time.sleep(300)

