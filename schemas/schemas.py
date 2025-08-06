from langchain.output_parsers import ResponseSchema

tittle = ResponseSchema(
    name="tittle",
    description="The title of the document"
)
content = ResponseSchema(
    name="content",
    description="The content of the document"
)
response_schemas = [tittle, content]
