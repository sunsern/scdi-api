[Back to main](../README.md)

# Read key

Retrieves a string value associated with a specific key.

**URL** : `/api/v1/{username}/{bucketname}?key={keyvalue}`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : Owner

**Data constraints**

N/A

**Data examples**

```
GET /api/v1/admin/kvbucket?key=testkey
```

## Success Responses

**Condition** : valid APIKEY

**Code** : `200 OK`

**Content example** : The value will be returned as response.

```
Test Value
```

## Error Response

**Code** : `400 BAD REQUEST`

**Content example** :

```
```

## Notes
