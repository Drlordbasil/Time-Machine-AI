import os
import shutil
import random
import string
import requests


def generate_idea():
    """
    Generates a custom idea for the program.
    :return: A string representing the idea.
    """
    return "Create a program that can predict the weather accurately for the next 7 days."


def convert_to_prompt(idea):
    """
    Converts the idea into a detailed prompt.
    :param idea: The program idea.
    :return: A string representing the prompt.
    """
    prompt = """Create a Python program that predicts the weather accurately for the next 7 days.
    
Your program should:
- Use an API to fetch weather data for a specific location.
- Parse the JSON response to extract relevant information.
- Display the weather forecast for each day.

Bonus points for:
- Allowing users to input their desired location.
- Providing the option to display the forecast in different units (e.g., Celsius or Fahrenheit).
"""
    return prompt


def transform_prompt_to_code(prompt, api_key):
    """
    Transform the prompt into a functioning Python program.
    :param prompt: The program prompt.
    :param api_key: The API key for weather data.
    :return: A string representing the code.
    """
    code = f"""import requests

def fetch_weather_forecast(location):
    api_key = "{api_key}"
    url = f"https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&days=7"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            forecast = data['forecast']['forecastday']

            for day in forecast:
                date = day['date']
                condition = day['day']['condition']['text']
                temp_c = day['day']['avgtemp_c']
                temp_f = day['day']['avgtemp_f']
                print(f"Date: {date}")
                print(f"Condition: {condition}")
                print(f"Temperature: {temp_c}°C / {temp_f}°F")
                print()
        else:
            print("Failed to fetch weather forecast.")
    except requests.exceptions.RequestException as e:
        print(str(e))
    
location = input("Enter a location: ")
fetch_weather_forecast(location)
"""

    return code


def save_code_to_file(code, file_name):
    """
    Saves the code to a Python script file.
    :param code: The code.
    :param file_name: The name of the file.
    """
    with open(file_name, 'w') as file:
        file.write(code)


def upload_to_github(repository_url, file_name):
    """
    Uploads the script to a GitHub repository.
    :param repository_url: The URL of the GitHub repository.
    :param file_name: The name of the file.
    """
    destination_path = os.path.join("github_repo", file_name)
    shutil.copyfile(file_name, destination_path)
    os.chdir("github_repo")
    subprocess.run(["git", "add", file_name])
    subprocess.run(["git", "commit", "-m", "Added script"])
    subprocess.run(["git", "push", "origin", "master"])


def main():
    """
    Main function to generate the Python script and upload it to GitHub.
    """
    api_key = "YOUR_API_KEY"

    idea = generate_idea()
    prompt = convert_to_prompt(idea)
    code = transform_prompt_to_code(prompt, api_key)
    file_name = f"{ ''.join(random.choices(string.ascii_lowercase, k=10)) }.py"

    save_code_to_file(code, file_name)
    upload_to_github("https://github.com/your-username/repository", file_name)

    print("Python script generated and uploaded successfully.")


if __name__ == '__main__':
    main()