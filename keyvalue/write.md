# Write key

Assigns a string value to a specific key.

**URL** : `/api/v1/{username}/{bucketname}?key={keyvalue}`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : Owner

**Data constraints**

The entire request will be interpreted as value string.

```
[string of value]
```

**Data examples**

```
Test Value
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
