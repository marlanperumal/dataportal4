# import pytest
# from typing import List
from flask.testing import FlaskClient

# from ...models import db
from ...models.meta import Dataset
from ...methods.meta.datasets import fetch_dataset

# from ...schema.meta import dataset_schema


def test_fetch_dataset(client: FlaskClient, default_dataset: Dataset):
    dataset: Dataset = fetch_dataset(default_dataset.id)

    assert dataset.id == default_dataset.id
    assert dataset.name == default_dataset.name
    assert dataset.collection == default_dataset.collection
    assert dataset.priority == default_dataset.priority
    assert dataset.is_hidden == default_dataset.is_hidden
    assert dataset.is_locked == default_dataset.is_locked
