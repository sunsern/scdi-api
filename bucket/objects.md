[Back to main](../README.md)

# List objects

List objects in a bucket.

**URL** : `/api/v1/{username}/{bucketname}?list`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : Owner

**Data constraints**

N/A

**Data examples**

```
GET /api/v1/admin/testtimeseriesbucket?meta
```

## Success Responses

**Condition** : valid APIKEY

**Code** : `200 OK`

**Content example** :

```json
[{u'status': u'PACKED', u'created': 1521545756290, u'name': u'random.txt', u'modified': 1521545756285}]
```

## Error Response

**Code** : `400 BAD REQUEST`

**Content example** :

``

## Notes
