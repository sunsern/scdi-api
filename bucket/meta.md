# Get bucket info

Get meta information of a bucket. The information includes bucket type and column definitions.

**URL** : `/api/v1/{username}/{bucketname}?delete`

**Method** : `DELETE`

**Auth required** : YES

**Permissions required** : Owner

**Data constraints**

**Data examples**

```
GET /api/v1/admin/testtimeseriesbucket?meta
```

## Success Responses

**Condition** : valid APIKEY

**Code** : `200 OK`

**Content example** : 

```json
{
    "id": 17,
    "created": 1517138542630,
    "createdBy": null,
    "modified": 1517138542630,
    "modifiedBy": null,
    "active": true,
    "type": "TIMESERIES_STORE",
    "owner": {
        "id": 1,
        "email": "admin@scdi.io",
        "username": "admin",
        "disabled": false,
        "locked": false,
        "expiry": null,
        "created": 1513735723190,
        "modified": 1513735723190,
        "roles": [
            "ROLE_ACTUATOR",
            "ROLE_USER",
            "ROLE_ADMIN"
        ],
        "defaultRole": "ROLE_USER"
    },
    "internalName": "BKT_d82e433ea9170fd3e6c435fb98f79ce0",
    "name": "testtimeseriesbucket",
    "bucketPermissions": null,
    "columnDefinitions": [
        {
            "id": 30,
            "created": 1517138542633,
            "createdBy": null,
            "modified": 1517138542633,
            "modifiedBy": null,
            "active": true,
            "name": "rain",
            "type": "DOUBLE",
            "indexed": true
        },
        {
            "id": 31,
            "created": 1517138542636,
            "createdBy": null,
            "modified": 1517138542636,
            "modifiedBy": null,
            "active": true,
            "name": "temp",
            "type": "DOUBLE",
            "indexed": true
        },
        {
            "id": 32,
            "created": 1517138542639,
            "createdBy": null,
            "modified": 1517138542639,
            "modifiedBy": null,
            "active": true,
            "name": "remark",
            "type": "VARCHAR",
            "indexed": false
        },
        {
            "id": 33,
            "created": 1517138542642,
            "createdBy": null,
            "modified": 1517138542642,
            "modifiedBy": null,
            "active": true,
            "name": "ts",
            "type": "TIMESTAMP",
            "indexed": true
        }
    ],
    "fullBucketName": "admin/testtimeseriesbucket"
}
```
## Error Response

**Code** : `400 BAD REQUEST`

**Content example** :

```
```

## Notes
