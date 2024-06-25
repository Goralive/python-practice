from enum import Enum


class DocFormat(Enum):
    PDF = "pdf"
    TXT = "txt"
    MD = "MD"
    HTML = "html"


def convert_format(content, from_format, to_format):
    if from_format == DocFormat.MD and to_format == DocFormat.HTML:
        temp = content.lstrip("# ")
        return f"<h1>{temp}</h1>"
    if from_format == DocFormat.TXT and to_format == DocFormat.PDF:
        return f"[PDF] {content} [PDF]"
    if from_format == DocFormat.HTML and to_format == DocFormat.MD:
        temp = content.strip("<>/h1")
        return f"# {temp}"
    raise Exception("Invalid type")
