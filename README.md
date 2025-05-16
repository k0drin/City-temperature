# Weather Services

## Installation and launch

1. Clone repositories:

   With HTTP
   ```bash
   git clone https://github.com/k0drin/City-temperature.git
   ```

   With SSH
   ```bash
   git clone git@github.com:k0drin/City-temperature.git
   ```

2. Install the virtual environment and activate it:
   ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
    ```
3. Install all dependencies:
   ```bash
    pip install -r requirements.txt
    ```
4. Now you can make migrations:
   ```bash
    python manage.py makemigrations
    ```
5. Then simply apply the migrations:
   ```bash
    python manage.py migrate
    ```

5. For start run:
    ```bash
    python manage.py runserver
    ```

6. After launching, you can see something like this:

    ![alt text](media/runserver.png)

7. Also you can check unit test:
    ```bash
   python manage.py test city.tests.test_views    
   ```

8. To check the main functionality
* GET http://127.0.0.1:8000/city/ - return all cities

    ![alt text](media/all_cities.png)

* GET http://127.0.0.1:8000/city/{city_id} - return info about specific city by {city_id}

    ![alt text](media/specific_city.png)

* POST http://127.0.0.1:8000/city/ - create new city

    ![alt text](media/add_city.png)
    ![alt text](media/add_city_result.png)

* PUT http://127.0.0.1:8000/city{city_id} - update city info

    ![alt text](media/update_city.png)
    ![alt text](media/update_city_result.png)

* DELETE http://127.0.0.1:8000/city{city_id} - delete city

    ![alt text](media/delete_city.png)
    ![alt text](media/delete_city_result.png)

* POST http://127.0.0.1:8000/city/{city_id}/ setTemperature/ - create city temperature

    ![alt text](media/set_temperature.png)
    ![alt text](media/set_temperature_result.png)

* GET http://127.0.0.1:8000/stats/ - return average temperature from all cities
    ![alt text](media/average_temp_all_city.jpg)

* GET http://localhost:8000/stats/?city_city_id={city_city_id} - return average temperature from specific city
    ![alt text](media/average_temp_specific_city.png)
