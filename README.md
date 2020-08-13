# web_frameworks_benchmark
This repository has been created to compare different web frameworks


# Project models:
In this project we have two simple models(Database models):

```
OrderModel
  //fields or db columns
  order_number -> primary key, integer
  order_status -> an integer number 0 - initate, 1 - in progress, 2 - done
  created_at -> datetime
  order_item_list -> a list of orderitems
 
  // methods
  calculate_total_price()
  calculate_total_qty()

OrderItem
  //fields or db columns
  pk -> integer
  product_name -> string
  price -> decimal
  qty -> integer
  
  //order foriegn key
  order -> OrderModel
```

# APIs

In the first step, we use fake data to fill the database
Our first goal is: we need to get a list of orders(order by created_at)

result scheme must be look like this(json result):

```
[
  {
    "order_number": 121323,
    "order_status": 2,
    "created_at": "1999-01-08 04:05:06",
    "total_price": 54345.0,
    "total_qty": 43,
    "items": [
        {
          "product_name": "milk",
          "price": 230.0,
          "qty": 3
        },
        ...
    ] // items
  },
  ...
]
```

**Note: If you want to participate in this project, please create a new issue**

# Requirements

  * please **Don't** use raw sql
  * please use **docker**
  * please use **postgresql** for database

# Benchmark result

is under consideration
