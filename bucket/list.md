[Back to main](../README.md)

# List buckets

List all buckets.

**URL** : `/api/v1/{username}`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : Owner

**Data constraints**

N/A

**Data examples**

```
GET /api/v1/admin
```

## Success Responses

**Condition** : valid APIKEY

**Code** : `200 OK`

**Content example** :

```json
[
  {u'created': 1518086830109,
   u'type': u'KEYVALUE_STORE',
   u'name': u'testbucket',
   u'modified': 1518086830109
  },
  {u'created': 1518086870035,
   u'type': u'TIMESERIES_STORE',
   u'name': u'testtimeseriesbucket',
   u'modified': 1518086870035
  },
  {u'created': 1521545756174,
   u'type': u'OBJECT_STORE',
   u'name': u'kws_demo',
   u'modified': 1521545756174
  }
]
```

## Error Response

**Code** : `400 BAD REQUEST`

**Content example** :

``

## Notes
