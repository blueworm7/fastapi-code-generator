# generated by fastapi-codegen:
#   filename:  same_response_model_for_different_status_codes.yaml
#   timestamp: 2020-06-19T00:00:00+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Pet(BaseModel):
    id: int
    name: str
    tag: Optional[str] = None


class Pets(BaseModel):
    __root__: List[Pet] = Field(..., description='list of pet')


class Error(BaseModel):
    code: int
    message: str
