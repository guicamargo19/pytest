import pytest

from django.urls import reverse

# Adicionar breakpoint na resposta http
# import json
# import pdb


@pytest.mark.django_db
def test_post_view(client):
    url = reverse('home')
    response = client.get(url)
    # pdb.set_trace()
    # response = json.loads(response.content)
    assert response.status_code == 200
    assert b'Backend Python' in response.content
