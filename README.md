# CLA Database

A database built for the Cazenovia Lake Association, Cazenovia NY

## Auth

Send a `POST` request to `http://localhost:8000/dj-rest-auth/login/` with username and password in Body in this format:

```
{
    "username": "",
    "password": ""
}
```

Response will be like:

```
{
    "key": "40 letters and numbers run together"
}
```

You can now make requests to other endpoints with Header _Authorization_ with a value of _Token whatever-40-character-key-the-auth-request-sent-back_

## CLA File Storage App

### Endpoints

**GET:**

- All files: `http://localhost:8000/file-api/files/`
- Specific file: add id to the end of the GET url like this `http://localhost:8000/file-api/files/1/`

**POST:**

To use the postman fields:

- Headers:

  - Content-Type: multipart/form-data

- Body:
  - set to form-data

  - Fill in as follows:
    - Click dropdown in KEY and set to File, fill in KEY as _document_, and under VALUE use the button to open file browser and select your file.

    - For the other fields: fill in KEY as text with json key, fill in VALUE as text with json value


Here's the json format you would use, but it doesn't actually upload the file and it sets the filepath incorrectly:

```
{
    "name": "",
    "document": "/home/USER/cla-db/cla_file_storage/storage/personal_computer/FILENAME.pdf",
    "display_name": "",
    "path": "/home/USER/cla-db/cla_file_storage/storage/FOLDERNAME/FILENAME.pdf",
    "document_format": "",
    "document_text": "",
    "category": "",
    "description": "",
    "orig_doc_date": "YYYY-MM-DD",
    "keyword": ["keyword-1", "keyword-2"]
}
```

- TO DO: on frontend make the request with `headers: {'Content-Type': 'multpart/form-data'}` and use `new FormData()` to create the request - see [FormData MDN](https://developer.mozilla.org/en-US/docs/Web/API/FormData). Figure out how to handle this on the backend without dividing the `"keyword": ["keyword-1", "keyword-2"]` value into a list of letters as keywords. (such as `"keyword": [{"id": 21, "associated_keyword": "["}, {"id": 22, "associated_keyword": "\""}, , {"id": 23, "associated_keyword": "k"}...]` etc.)

**PUT:**

Send requests to `http://localhost:8000/file-api/files/id/`, replacing `id` with the actual ID number of the file whose information you want to update, with Body in format:

```
{
    "name": "",
    "document": "/home/USER/cla-db/cla_file_storage/storage/personal_computer/FILENAME.pdf",
    "display_name": "",
    "path": "/home/USER/cla-db/cla_file_storage/storage/FOLDERNAME/FILENAME.pdf",
    "document_format": "",
    "document_text": "",
    "category": "",
    "description": "",
    "orig_doc_date": "YYYY-MM-DD",
    "keyword": ["keyword-1", "keyword-2"]
}
```

**PATCH:**

Send requests to `http://localhost:8000/file-api/files/id/`, replacing `id` with the actual ID number of the file whose information you want to update, with Body containing only the fields to update, in format:

```
{
    "name": "",
    "document": "/home/USER/cla-db/cla_file_storage/storage/personal_computer/FILENAME.pdf",
    "display_name": "",
    "path": "/home/USER/cla-db/cla_file_storage/storage/FOLDERNAME/FILENAME.pdf",
    "document_format": "",
    "document_text": "",
    "category": "",
    "description": "",
    "orig_doc_date": "YYYY-MM-DD",
    "keyword": ["keyword-1", "keyword-2"]
}
```

Examples of valid request bodies include `{"path": "updated filepath goes here"}` or `{"keyword": ["new keyword"]}` or more than one field in one request: `{"path": "updated filepath goes here", "keyword": ["new keyword"]}`

**DELETE:**

Send requests to `http://localhost:8000/file-api/files/id/`, replacing `id` with the actual ID number of the file you want to delete.
