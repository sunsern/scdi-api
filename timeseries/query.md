[Back to main](../README.md)

# Query

Makes a query to timeseries/geotemporal bucket. 

**URL** : `/api/v1/{username}/{bucketname}?query`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : Owner

**Data constraints**

```
Content-Type: application/json
```

```
{
   "fromEpoch" : [from_epoch_timestamp], // Optional
   "toEpoch" : [to_epoch_timestamp], // Optional 
   "limit" : [limit], // Optional 
   "where" : [
      {
        "column" : [column_name],
        "op" : ["gt" | "lt" | "eq" | "gte" | "lte" ]
        "value : [value]
      },
      ... ], // Optional
   "aggregate" : [
      {
        "column" : [column_name],
        "op" : ["min" | "max" | "avg" | "sum" | "count"]
      },
      ...] // Optional
}
```

Where filters are conjuctions. If aggregation is present, the data returned will be aggregated before returning.

**Data examples**

```json
{
	"fromEpoch": 1517125310,
	"limit":1,
	"where": [
		{
			"column": "rain",
			"op": "gt",
			"value": 113
		}]
}
```

```json
{
	"fromEpoch": 1517125310,
	"aggregate" : [
			{
				"column": "rain",
				"op": "avg"
			},
			{
				"column": "temp",
				"op": "avg"
			}
		],
	"where": [
		{
			"column": "rain",
			"op": "gt",
			"value": 113
		}
		]
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
