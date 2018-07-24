# DB init

Initialising Fireclass Android app database  

## Files

* init-db.sh - bash script orchestrator
* fireclass.db - sqlite3 database file
* json_menus.php, json_pages.php - exported json data files
* menus-parse.py, pages-parse.py - parse and store data
* menus-show-data.py, pages-show-data.py - show stored data

## Procedure

With all files in same folder, run init-db.sh

```
$ . init-db.sh
```

This will create a fireclass.db file, which can then be used by
php scripts serving fireclass app data


