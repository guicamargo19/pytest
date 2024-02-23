import pytest

from django.urls import reverse

# Adicionar breakpoint na resposta http
'''
import json
import pdb; pdb.set_trace()
response = json.loads(responde.content)
'''


@pytest.mark.django_db
def test_post_view(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200
    assert response.content == 'Hello World'
