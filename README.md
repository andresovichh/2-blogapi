
# Django RESTApi

This is a basic Django RESTApi built based on William S. Vincent's book called "Django for APIs".

In particular, the project showcases a Blog API with CRUD operations and user authentication.

The application is hosted on Heroku
## Acknowledgements

 - [William S. Vincent's Book](https://www.amazon.com/Django-APIs-Build-web-Python/dp/1735467227/ref=sr_1_1?crid=3LP7C20LPJP76&keywords=django+for+apis&qid=1663625128&sprefix=django+for+apis%2Caps%2C220&sr=8-1)

## API Reference

#### Get all items

```http
  GET /api/v1
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_version` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/v1/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |


