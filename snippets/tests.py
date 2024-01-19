from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse
from snippets.models import Snippet


# Тесты для SnippetViewSet
class SnippetViewSetTests(APITestCase):
    def setUp(self):
        # Создание тестового пользователя
        self.user = get_user_model().objects.create_user(
            username="testuser", email="testuser@mail.com", password="testpass"
        )
        # Аутентификация пользователя в тестовом клиенте
        self.client.force_authenticate(user=self.user)
        # Данные для создания сниппета
        self.snippet_data = {"title": "Test Snippet", "code": 'print("Hello, World!")'}

    # Тест создания сниппета
    def test_create_snippet(self):
        url = reverse("snippet-list")
        response = self.client.post(url, self.snippet_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Snippet.objects.count(), 1)
        self.assertEqual(Snippet.objects.get().title, "Test Snippet")

    # Тест получения сниппета
    def test_retrieve_snippet(self):
        url = reverse("snippet-list")
        response = self.client.post(url, self.snippet_data, format="json")
        url = reverse("snippet-detail", args=[response.data["id"]])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Snippet")

    # Тест обновления сниппета
    def test_update_snippet(self):
        url = reverse("snippet-list")
        response = self.client.post(url, self.snippet_data, format="json")
        url = reverse("snippet-detail", args=[response.data["id"]])
        updated_data = {"title": "Updated Snippet", "code": 'print("Updated Hello, World!")'}
        response = self.client.put(url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Snippet.objects.get().title, "Updated Snippet")

    # Тест удаления сниппета
    def test_delete_snippet(self):
        url = reverse("snippet-list")
        response = self.client.post(url, self.snippet_data, format="json")
        url = reverse("snippet-detail", args=[response.data["id"]])
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Snippet.objects.count(), 0)

    # Тест получения подсвеченного кода сниппета
    def test_highlight_snippet(self):
        url = reverse("snippet-list")
        response = self.client.post(url, self.snippet_data, format="json")
        url = reverse("snippet-highlight", args=[response.data["id"]])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Hello, World!", response.data)


# Тесты для UserViewSet
class UserViewSetTests(APITestCase):
    def setUp(self):
        # Создание тестового пользователя
        self.user = get_user_model().objects.create_user(
            username="testuser", email="testuser@mail.com", password="testpass"
        )
        # Аутентификация пользователя в тестовом клиенте
        self.client.force_authenticate(user=self.user)

    # Тест получения информации о пользователе
    def test_retrieve_user(self):
        url = reverse("user-detail", args=[self.user.id])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "testuser")

    # Тест получения списка пользователей
    def test_list_users(self):
        url = reverse("user-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
