# Add row

Add a entry to timeseries/geotemporal bucket

**URL** : `/api/v1/{username}/{bucketname}`

**Method** : `PUT`

**Auth required** : YES

**Permissions required** : Owner

**Data constraints**

```
Content-Type: application/json
```

```
{
   [Column1] : [value],
   [Column2] : [value],
   [Column3] : [value],
   ...
}
```

All required columns must be present in the row. The required columns for timeseries buckets are:
1. `ts` -- timestamp in epoch

and for geotemporal buckets are:
1. `ts` -- timestamp in epoch
2. `lat` -- latitude
3. `lng` -- longitude


**Data examples**

```json
{
	"ts" : 1517125302,
	"rain" : 12.0,
	"temp": 20.0
}
```

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
