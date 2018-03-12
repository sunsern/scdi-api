[Back to main](../README.md)

# Add mutiple rows from an uploaded file

Add multiple entries to timeseries/geotemporal bucket where the data source comes from a uploaded file

**URL** : `/api/v1/{username}/{bucketname}?batch&copyFrom={objname}`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : Owner

**Data constraints**

N/A

**Data examples**

```
POST /api/v1/admin/testtimeseriesbucket?batch&copyFrom=test.json
```

Note that `test.json` must be uploaded prior to the request.

## Success Responses

**Condition** : valid APIKEY

**Code** : `200 OK`

**Content example** :

```
```

## Error Response

**Code** : `400 BAD REQUEST`

**Content example** :
```

```

## Notes
