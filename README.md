Tornado Book API example
-----------------------------

@2021/07/19


## install tornado

```
% pip3 install tornado
```

## start server

```
% python3 api.py
```

## api routes

- get book: GET http://localhost:8888/v1/getbooks
- add book: POST http://localhost:8888/v1/addbook
- update book: PUT http://localhost:8888/v1/updatebook/{book id} , send with json body
- delete book: DELETE http://localhost:8888/v1/delbook/{book id}
