# SCDI API

## Open Endpoints

## Endpoints that require Authentication

Closed endpoints require a valid API key to be included in the header of the request. An API key can be created via the web UI.

**HEADER** : `APIKEY: [a valid API key]`

- [Upload](upload/readme.md)

### Bucket related

- [Create Bucket](bucket/create.md): `POST /api/v1/{username}/{bucketname}?create`
- [Drop Bucket](bucket/drop.md): `DELETE /api/v1/{username}/{bucketname}?delete`

### Key-value related

- [Write key](keyvalue/add.md): `POST /api/v1/{username}/{bucketname}?key={keyvalue}`
- [Read key](keyvalue/add.md): `GET /api/v1/{username}/{bucketname}?key={keyvalue}`
