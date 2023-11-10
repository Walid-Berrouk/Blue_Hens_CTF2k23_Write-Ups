# Why lie: Blind SQL 

## Description

> If someone breaks it all ping me and I'll redploy.
> 
> https://bluehens-blindsql.chals.io/ 


## Write-Up

When entering the web app, we receive the following code:

```php
    $dbhandle = new PDO("sqlite:blind.db") or die("Failed to open DB");
    if (!$dbhandle) die ($error);

    $guess = 3;
    if (isset($_GET["guess"])){
      $guess = $_GET["guess"];
    }
    $query = "select * from numbers where value=".$guess;
    $statement = $dbhandle->prepare($query);
    $statement->execute();
    $results = $statement->fetchAll(PDO::FETCH_ASSOC);

    //echo json_encode($results);
    echo highlight_file(__FILE__, true);
    if (count($results) > 0){
        echo "Good guess!";
    } else {
        echo "Nope";
    }
```

It also prints a result:

```
Nope
```

The website expect a query parameter `guess`, and it seems that it isn't sanitized. So, we can do a simple **SQLi** to try to bypass condition :

```
https://bluehens-blindsql.chals.io/?guess=3%20OR%201=1
```

We get :

```
Good guess!
```

As we don't have a way to output the resulsts, and knowing the db is `sqlite`, we should perform **Blind SQLi** on the db to get the tables, columns and eventually content to get the flag.

There are two types of Blind SQLi we can use: **Time Based** and **Error Based**

> Time-based SQL Injection is an inferential SQL Injection technique that relies on sending an SQL query to the database which forces the database to wait for a specified amount of time (in seconds) before responding. The response time will indicate to the attacker whether the result of the query is TRUE or FALSE.
>
> Error-based SQLi is an in-band SQL Injection technique that relies on error messages thrown by the database server to obtain information about the structure of the database. In some cases, error-based SQL injection alone is enough for an attacker to enumerate an entire database.
> 
> This attacks help us deduce names of tables and columns based on the time the request takes to execute.

For us, as we have two messages for whenever the sql query returns rows or not, we can use them in order to perform **Error BAsed** attack.

First, we need to know how to extract tables namesin sqlite:

> For tables, the type field will always be 'table' and the name field will be the name of the table. So to get a list of all tables in the database, use the following SELECT command:
>
>    SELECT name FROM sqlite_schema
>    WHERE type='table'
>    ORDER BY name;

You can check [Tables Script](./tables.py) for more detailes.

After that, comes the extraction of the columns names.

> ```SELECT name FROM PRAGMA_TABLE_INFO("table_name");```
> 
> Unlike the last command, this only returns the names of all the columns. Additionally, this command only works on a local database but not with attached schemas.

For solution, Checkout [Columns Script](./columns.py)

Finally, the flag, with a simple select statement. Checkout [Flag Script](./flag.py)

## Flag

UDCTF{l1k3_a_b4t}

## More Information

- https://beaglesecurity.com/blog/vulnerability/time-based-blind-sql-injection.html
- [SQLi For SQLite Apps](./41397-injecting-sqlite-database-based-applications.pdf)
- https://www.sqlinjection.net/time-based/
- https://www.sqlitetutorial.net/sqlite-functions/sqlite-substr/
- https://www.delftstack.com/howto/sqlite/sqlite-get-column-names/
