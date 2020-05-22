from assignment3 import validator


def main():
    html_validator = validator.HtmlValidator()
    result = html_validator.validate_html_string()
    if result:
        print("Valid")
    else:
        print("Invalid")
