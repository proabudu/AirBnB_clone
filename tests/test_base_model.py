#!/usr/bin/python3

from datetime import timedelta

from models.base_model import BaseModel


class TestBaseModel:
    def test_init(self):
        instance = BaseModel()
        assert isinstance(instance.id, str)
        assert isinstance(instance.created_at, datetime)
        assert isinstance(instance.updated_at, datetime)

    def test_str(self):
        instance = BaseModel(name="Alice", age=30)
        expected_str = f"[<class {instance.__class__.__name__}>] ({instance.id}) {instance.__dict__}"
