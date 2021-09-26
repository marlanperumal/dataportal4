from typing import List
from ...models import db
from ...models.meta import Dataset
from ...schema.meta import dataset_schema, datasets_schema


def fetch_dataset(dataset_id) -> Dataset:
    dataset: Dataset = Dataset.query.get(dataset_id)
    return dataset


def fetch_datasets() -> List[Dataset]:
    datasets: List[Dataset] = Dataset.query.order_by("id").all()
    return datasets


def new_dataset(data) -> Dataset:
    dataset: Dataset = dataset_schema.load(data)
    db.session.add(dataset)
    db.session.flush()
    return dataset


def new_datasets(data) -> List[Dataset]:
    datasets: List[Dataset] = datasets_schema.load(data)
    db.session.add_all(datasets)
    db.session.flush()
    return datasets


def edit_dataset(dataset_id, data) -> Dataset:
    dataset: Dataset = Dataset.query.get(dataset_id)
    if dataset is None:
        raise Exception(f"Dataset {dataset_id} not found")

    dataset_schema.load(data, instance=dataset, partial=True)
    db.session.flush()
    return dataset


def remove_dataset(dataset_id) -> Dataset:
    dataset: Dataset = Dataset.query.get(dataset_id)
    if dataset is None:
        raise Exception(f"Dataset {dataset_id} not found")

    db.session.delete(dataset)
    db.session.flush()
    return dataset
