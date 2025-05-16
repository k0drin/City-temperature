from rest_framework.test import APITestCase
from rest_framework import status
from city.models import City, CityTemperature


class CityTests(APITestCase):
    def test_create_city(self):
        data = {"name": "Kyiv", "description": "Capital of Ukraine"}
        response = self.client.post("/city/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_set_temperature(self):
        city = City.objects.create(name="Lviv", description="Western city")
        response = self.client.post(f"/city/{city.id}/setTemperature/", {"value": 23.5})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_stats(self):
        city = City.objects.create(name="Dnipro", description="Central city")
        CityTemperature.objects.create(city=city, value=20)
        CityTemperature.objects.create(city=city, value=30)
        response = self.client.get("/stats/", {"city_id": city.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertAlmostEqual(response.data["average"], 25.0)

