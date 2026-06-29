# Run SQL via REST API

Execute SQL statements directly against the Maximo database using an Automation Script.

Create an **Automation Script** named `runsql` with **no launch point**, then call it through the REST API:

```text
https://[MAXIMO_URL]/maximo/oslc/script/runsql?method=SELECT&sql=SELECT top 10 assetnum,description,status FROM asset WHERE status='OPERATING'
```

> ⚠️ **Warning:** This script executes SQL directly against the database. It can bypass Maximo business logic and security controls. Use it only in trusted environments and restrict access to authorized administrators. Avoid exposing this endpoint in production.
