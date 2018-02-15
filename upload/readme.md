# Upload APIs

There are two ways to upload files to SCDI.

- Single-part upload - a full content of the file is uploaded to the server. This is suitable for small files.
- Multi-part upload - a file is split into small chunks (between 1MB and 2MB per chunk) and are uploaded to the server. You can split a file up to 2,048 chunks (total of 4GB per upload). This is suitable for large file upload.

  ```
  HOST: {api.server}
  APIKEY: {APIKEY:required}
  ```

## 1\. Single-part Upload

### Request

```
PUT /api/v1/{username}/{bucketName}/{objectName} HTTP/1.1
Content-Length: {partSize:required}
Content-MD5: {partMd5:required}
```

## 2\. Multi-part Upload

Multi-part upload contains three steps:

1. Create an uploading ticket - this operation initiates an uploading request and returns uploadId.
2. Upload file - file is uploaded using uploadId
3. Complete the uploads - this operations set server to package all the parts as a

### 2.1 Create Multi-part Upload

#### Request

```
POST /api/v1/{username}/{bucketName}/{objectName}?create HTTP/1.1
```

#### Request parameters

None

### 2.2 Upload parts

```
PUT /api/v1/{username}/{bucketName}/{objectName}?partNumber=1 HTTP/1.1
Content-Length: {partSize:required}
Content-MD5: {partMd5:required}
```

#### Request parameters

`{partNumber}` can be anything between 1-10,000 inclusive. `{objectName}` is the name of the object. objectName is case sensitive. Internal structure of this object storage is flat, but you can use the delimiter (/) to build your own hierarchy structure in the objectName. For examples: objectName can be

```
documents/asd.txt Documents/asd.txt
```

#### Response body

```
{
  "md5": {xxxxx},
  "error": "LengthMismatched|SHA256Mismatched|PermissionDenied|InvalidPartNumber|InvalidUploadId|InvalidBucket|ExpiredUploadId"
}
```

### 2.3 Complete Multi-part upload

```
POST /api/v1/{username}/{bucketName}/{objectName}?complete HTTP/1.1
Content-Length: {totalLength:required}
Content-MD5: {eTag:required}
```

We do not use regular MD5 hash To check the integrity of a file that was uploaded in multiple parts. Instead of calculating the hash of the entire file, we calculate the hash of each part and combines that into a single hash and, then, the number of parts is appended to the end of the md5 hash.

```
eTag = {md5 of {md5 of all parts in bytes}}-{numberOfPart}
```
For examples, if you have splitted a file in two 3 parts with the following MD5 respectively:

```
MD5 of part 1 = 9961bbe5d7c70a5f0e23d63bc7433b01
MD5 of part 2 = bfbd30c675df62d67f02d0efa72bc1ac
MD5 of part 3 = 92589dcb2dd1bcc29ab1ee6b8eb7f6aa

Cheksum of all parts is 1e2028574f9067f32990b8ac5cc8456c-3
```



#### Request parameters

`{partNumber}` anything between 1-10,000 inclusive.

### 2.4 Delete parts

```
DELETE /api/v1/{username}/{bucketName}/{objectName}?partNumber=1 HTTP/1.1
```

#### Request parameters

`{partNumber}`anything between 1-10,000 inclusive.

### 2.5 Get parts information

```
GET /api/v1/{username}/{bucketName}/{objectName}?partNumber=1&metadata HTTP/1.1
```

### 2.6 Get object information

```
GET /api/v1/{username}/{bucketName}/{objectName}?metadata HTTP/1.1
```

### 2.6 Download object

```
GET /api/v1/{username}/{bucketName}/{objectName} HTTP/1.1
```

### Possible Exceptions

1. If `{APIKEY}` is invalid, `401 Unauthenticated` is returned.
2. If `{APIKEY}` is NOT authorized to access `{BUCKET}`, `403 Forbidden` is returned.
3. If `{APIKEY}` is authorized to access `{BUCKET}`, status will be determined by controller.

command json:

{ "kind": "command", "jobId": ..., "command_data": query-json }

report json: { "kind": "report", "jobId": ..., "report_data": { "status": ["started" or "done"], (if done) "result": ... }
