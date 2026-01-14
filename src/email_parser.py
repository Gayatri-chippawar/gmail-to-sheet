import base64

def get_header(headers, name):
    for h in headers:
        if h['name'].lower() == name.lower():
            return h['value']
    return ""


def decode_body(payload):
    """
    Recursively extract and decode plain text email body
    """
    if 'parts' in payload:
        for part in payload['parts']:
            if part.get('mimeType') == 'text/plain':
                data = part['body'].get('data')
                if data:
                    return base64.urlsafe_b64decode(data).decode('utf-8', errors='ignore')
            elif part.get('mimeType', '').startswith('multipart'):
                text = decode_body(part)
                if text:
                    return text
    else:
        data = payload['body'].get('data')
        if data:
            return base64.urlsafe_b64decode(data).decode('utf-8', errors='ignore')

    return ""


def parse_email(message):
    payload = message['payload']
    headers = payload.get('headers', [])

    email_data = {
        "from": get_header(headers, "From"),
        "subject": get_header(headers, "Subject"),
        "date": get_header(headers, "Date"),
        "content": decode_body(payload)
    }

    return email_data
