from . import ma
from ..models.meta import Dataset


class DatasetSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Dataset
        load_instance = True
        include_fk = True

    id = ma.auto_field(dump_only=True)


dataset_schema = DatasetSchema()
datasets_schema = DatasetSchema(many=True)
