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
PUT /{username}/{bucketName}/{objectName} HTTP/1.1
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
POST /{username}/{bucketName}/{objectName}?create HTTP/1.1
```

#### Request parameters

None

### 2.2 Upload parts

```
PUT /{username}/{bucketName}/{objectName}?partNumber=1 HTTP/1.1
Content-Length: {partSize:required}
Content-MD5: {partMd5:required}
```

#### Request parameters

`{partNumber}` can be anything between 1-10,000 inclusive. `{objectName}` is the name of the object. objectName is case sensitive. Internal structure of this object storage is flat, but you can use the delimiter (/) to build your own hierarchy structure in the objectName. For examples: objectName can be

documents/asd.txt Documents/asd.txt

#### Response body

```
{
  "md5": {xxxxx},
  "error": "LengthMismatched|SHA256Mismatched|PermissionDenied|InvalidPartNumber|InvalidUploadId|InvalidBucket|ExpiredUploadId"
}
```

### 2.3 Complete Multi-part upload

```
POST /{username}/{bucketName}/{objectName}?complete HTTP/1.1
```

#### Request parameters

`{partNumber}` anything between 1-10,000 inclusive.

### 2.4 Delete parts

```
DELETE /{username}/{bucketName}/{objectName}?partNumber=1 HTTP/1.1
```

#### Request parameters

`{partNumber}`anything between 1-10,000 inclusive.

### 2.5 Get parts information

```
GET /{username}/{bucketName}/{objectName}?partNumber=1&metadata HTTP/1.1
```

### 2.6 Get object information

```
GET /{username}/{bucketName}/{objectName}?metadata HTTP/1.1
```

### 2.6 Download object

```
GET /{username}/{bucketName}/{objectName} HTTP/1.1
```

### 2.6 Download part

```
GET /{username}/{bucketName}/{objectName}?partNumber=1 HTTP/1.1
```

### Possible Exceptions

1. If `{APIKEY}` is invalid, `401 Unauthenticated` is returned.
2. If `{APIKEY}` is NOT authorized to access `{BUCKET}`, `403 Forbidden` is returned.
3. If `{APIKEY}` is authorized to access `{BUCKET}`, status will be determined by controller.

command json:

{ "kind": "command", "jobId": ..., "command_data": query-json }

report json: { "kind": "report", "jobId": ..., "report_data": { "status": ["started" or "done"], (if done) "result": ... }
