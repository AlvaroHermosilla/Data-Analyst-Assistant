from templates.templates import data_analyst_role_template,code_role_template,translate_role_template

role_template = [
{
    "name": "data",
    "description": "Excelente para el analisis de datos",
    "prompt_templates": data_analyst_role_template,
    "input_variables": "output"
},
{
    "name": "code",
    "description": "Excelente para el analisis de datos",
    "prompt_templates": code_role_template,
    "input_variables": "output"
},
{
    "name": "translate",
    "description": "Excelente para el analisis de datos",
    "prompt_templates": translate_role_template,
    "input_variables": "output"
}
]