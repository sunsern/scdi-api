# SCDI API

The SCDI APIs are designed to allow access to features of the SCDI platform. The reference document can be found here: https://sunsern.github.io/scdi-api/.

## Open Endpoints

Currently all SCDI endpoints require authentication. 

## Endpoints that require authentication

Closed endpoints require a valid API key to be included in the header of the request. 
An API key can be created via the web UI. Here is an example header of a request.

**HEADER** : `APIKEY: [a valid API key]`

### Upload related 

- [Upload](upload/readme.md)

### Bucket related

- [Create bucket](bucket/create.md): `POST /api/v1/{username}/{bucketname}?create`
- [Drop bucket](bucket/drop.md): `DELETE /api/v1/{username}/{bucketname}?delete`
- [Get bucket info](bucket/meta.md): `GET /api/v1/{username}/{bucketname}?meta`

### Key-value related

- [Write key](keyvalue/write.md): `POST /api/v1/{username}/{bucketname}?key={keyvalue}`
- [Read key](keyvalue/read.md): `GET /api/v1/{username}/{bucketname}?key={keyvalue}`

### Timeseries/Geotemoporal related

- [Add row](timeseries/add.md): `PUT /api/v1/{username}/{bucketname}`
- [Add multiple rows](timeseries/add_multiple.md): `POST /api/v1/{username}/{bucketname}?batch`
- [Simple query](timeseries/query.md): `POST /api/v1/{username}/{bucketname}?query`
