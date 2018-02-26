[Back to main](../README.md)

# Create bucket

Creates a data bucket.

**URL** : `/api/v1/{username}/{bucketname}?create`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : Owner

**Data constraints**

```
{
    "type": ["timeseries"|"geotemporal"|"keyvalue"|"kws"],
    "columns": [
      {
        "name": [column name],
        "type": ["varchar"|"int"|"bigint"|"double"|"text"|"timestamp"],
        "indexed": [true|false]
      },
      ...
    ]
}
```

**Data examples**

For key-value bucket, columns can be omitted.

```
POST /api/v1/admin/bucket1?create
```

```json
{
    "type": "keyvalue"
}
```

For timeseries,

```
POST /api/v1/admin/testtimeseriesbucket?create
```

```json
{
    "type": "timeseries",
    "columns" : [
            {
                "name": "ts",
                "type": "timestamp",
                "indexed": true
            },
            {
                "name": "rain",
                "type": "double",
                "indexed": true
            },
            {
                "name": "temp",
                "type": "double",
                "indexed": true
            },
            {
                "name": "remark",
                "type": "varchar",
                "indexed": false
            }
        ]
}
```

## Success Responses

**Condition** : valid APIKEY

**Code** : `200 OK`

**Content example** : The created bucket metadata will be returned.

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

## Notes
