from pydantic import BaseModel, ConfigDict


class Base(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    def __str__(self):
        return str(self.model_dump_json(indent=2))
