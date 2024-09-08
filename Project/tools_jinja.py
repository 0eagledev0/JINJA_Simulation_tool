from jinja2 import Template
import yaml
import json


def read_file(file_path):
    """
    Reads the content of a file and returns it as a string.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def merge_templates(template1_content,template2_content):
    """
    Merges two template contents into one by concatenating them.
    """
    return template1_content +"\n"+ template2_content

def variable_jinja(variable, jinja):
    """
    Processes Jinja templates using the variable and template files.
    """
    template1_content = read_file(variable)
    template2_content = read_file(jinja)
    merged_content = merge_templates(template1_content,template2_content)
    config_in = Template(merged_content)
    config_out = config_in.render()
    return config_out

def variable_YAML(variable_path, jinja):
    """
    Processes a YAML variable file and a Jinja template file.
    """
    try:
        with open(variable_path, 'r', encoding='utf-8-sig') as yaml_file:
            variable=yaml.safe_load(yaml_file)
        template_content = read_file(jinja)
        template = Template(template_content)
        content = template.render(variable)
        return content
    except Exception as e:
        return str(e)

def variable_JSON(variable_path, jinja):
    """
    Processes a JSON variable file and a Jinja template file.
    """
    try:
        with open(variable_path, 'r', encoding='utf-8-sig') as json_file:
            variable=json.load(json_file)
        template_content = read_file(jinja)
        template = Template(template_content)
        content = template.render(variable)
        return content
    except Exception as e:
        return str(e)
