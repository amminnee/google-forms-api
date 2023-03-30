from google.oauth2 import service_account
from googleapiclient.discovery import build

creds = service_account.Credentials.from_service_account_file(
    'service_account.json',
    scopes=['https://www.googleapis.com/auth/forms.body']
)

delegated_creds = creds.with_subject("amineed98@quantum-chemist-269020.iam.gserviceaccount.com")

service = build('forms', 'v1', credentials=delegated_creds)

form_config = {
  "info": {
    "title": "Mark you presence",
    "documentTitle": "ScanPresence"
  }
}

id_input = {
    "requests": [
        {
        "createItem": {
            "item": {
            "questionItem": {
                "question": {
                "textQuestion": {
                    "paragraph": False
                }
                }
            }
            },
            "location": {
            "index": 0
            }
        }
        }
    ]
}

response = service.forms().create(body=form_config).execute()
add_form = service.forms().batchUpdate(formId=response["formId"], body=id_input).execute()

print(response)