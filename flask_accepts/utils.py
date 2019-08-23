from typing import Optional, Type, Union
from flask_restplus import fields as fr
from marshmallow import fields as ma
from marshmallow.schema import Schema, SchemaMeta
import uuid


def unpack_list(val, api, model_name: str = None):
    model_name = model_name = get_default_model_name()
    return fr.List(map_type(val.inner, api, model_name))


def unpack_nested(val, api, model_name: str = None):
    model_name = model_name = get_default_model_name()
    return fr.Nested(map_type(val.nested, api, model_name))


def for_swagger(schema, api, model_name: str = None):
    """
    Convert a marshmallow schema to equivalent Flask-RESTplus model

    Args:
        schema (Marshmallow Schema): Schema defining the inputs
        api (Namespace): Flask-RESTplus namespace (necessary for context)
        model_name (str): Name of Flask-RESTplus model

    Returns:
        api.model: An equivalent api.model
    """

    model_name = model_name or get_default_model_name()
    fields = {
        k: map_type(v, api, model_name)
        for k, v in vars(schema).get("declared_fields", {}).items()
        if type(v) in type_map
    }
    return api.model(model_name, fields)


type_map = {
    ma.AwareDateTime: lambda val, api, model_name: fr.Raw(),
    ma.Bool: lambda val, api, model_name: fr.Boolean(),
    ma.Boolean: lambda val, api, model_name: fr.Boolean(),
    ma.Constant: lambda val, api, model_name: fr.Raw(),
    ma.Date: lambda val, api, model_name: fr.Date(),
    ma.DateTime: lambda val, api, model_name: fr.DateTime(),
    ma.Decimal: lambda val, api, model_name: fr.Decimal(),
    ma.Dict: lambda val, api, model_name: fr.Raw(),
    ma.Email: lambda val, api, model_name: fr.String(),
    ma.Float: lambda val, api, model_name: fr.Float(),
    ma.Function: lambda val, api, model_name: fr.Raw(),
    ma.Int: lambda val, api, model_name: fr.Integer(),
    ma.Integer: lambda val, api, model_name: fr.Integer(),
    ma.Length: lambda val, api, model_name: fr.Float(),
    ma.Mapping: lambda val, api, model_name: fr.Raw(),
    ma.NaiveDateTime: lambda val, api, model_name: fr.DateTime(),
    ma.Number: lambda val, api, model_name: fr.Float(),
    ma.Pluck: lambda val, api, model_name: fr.Raw(),
    ma.Raw: lambda val, api, model_name: fr.Raw(),
    ma.Str: lambda val, api, model_name: fr.String(),
    ma.String: lambda val, api, model_name: fr.String(),
    ma.Time: lambda val, api, model_name: fr.DateTime(),
    ma.Url: lambda val, api, model_name: fr.Url(),
    ma.URL: lambda val, api, model_name: fr.Url(),
    ma.UUID: lambda val, api, model_name: fr.String(),
    ma.List: unpack_list,
    ma.Nested: unpack_nested,
    Schema: for_swagger,
    SchemaMeta: for_swagger,
}

num_default_models = 0


def get_default_model_name(schema: Optional[Union[Schema, Type[Schema]]] = None) -> str:
    if schema:
        if isinstance(schema, Schema):
            return "".join(schema.__class__.__name__.rsplit("Schema", 1))
        else:
            # It is a type itself
            return "".join(schema.__name__.rsplit("Schema", 1))

    global num_default_models
    name = f"DefaultResponseModel_{num_default_models}"
    num_default_models += 1
    return name


def map_type(val, api, model_name):
    return type_map[type(val)](val, api, model_name)
