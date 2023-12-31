# Future Crypto 

## Description

> https://gist.github.com/AndyNovo/4268c517da1a72d57d6d8a2c34080817
> 
> The only tools you need for this one are: copy, paste, and the internet

## Write-Up

From the given repository, we have the flag encrypted represented as follow:

```
-----BEGIN AGE ENCRYPTED FILE-----
YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IHRsb2NrIDY5MTY5MDEgZGJkNTA2ZDZl
Zjc2ZTVmMzg2ZjQxYzY1MWRjYjgwOGM1YmNiZDc1NDcxY2M0ZWFmYTNmNGRmN2Fk
NGU0YzQ5Mwpvd3dpQ2szVTViRzh6dStyc1E1a2pHTWdxTVJZODJXS1dzYTZwUFlQ
bFF0Y0FNdEhMTWkwS3Zyb25QZmJySWQvCkdCSUQ5YzM1Qzd0ZExHd2VqODd0RXlx
Zys3ZHdaaXoxVlV5VCt5bXNNWTlvNWlUN2JMVVpCVHNOYlNaVjllQVUKWExkZ0Ft
a2JROFhBUWpySGNOOWRwd0VkWjg3US9zckN5bkd5em9RQTNHdwotLS0gT2l3U0Nj
cEplYUFJQk1qRmZXRFIvTkhXclg4L1lxN0MvQXRLR3dMaUtHOAqQGPAprak2MY6h
NnJYFEVD8VfHQThpIlMnffpZ9x5nRQsACp6mTMS5NWmCO7OAkyH1/NtHsj/uuCup
yA==
-----END AGE ENCRYPTED FILE-----
```

First thing to do is to try decode it as it is represented in `base64`:

```
age-encryption.org/v1
-> tlock 6916901 dbd506d6ef76e5f386f41c651dcb808c5bcbd75471cc4eafa3f4df7ad4e4c493
owwiCk3U5bG8zu+rsQ5kjGMgqMRY82WKWsa6pPYPlQtcAMtHLMi0KvronPfbrId/
GBID9c35C7tdLGwej87tEyqg+7dwZiz1VUyT+ymsMY9o5iT7bLUZBTsNbSZV9eAU
XLdgAmkbQ8XAQjrHcN9dpwEdZ87Q/srCynGyzoQA3Gw
--- OiwSCcpJeaAIBMjFfWDR/NHWrX8/Yq7C/AtKGwLiKG8
ð)­©61¡6rXECñWÇA8i"S'}úY÷gE 
¦LÄ¹5i;³!õüÛG²?î¸+©È
```

After looking for **Age Encryption**, we found the following:

> age is a simple, modern and secure file encryption tool, format, and Go library.
>
> It features small explicit keys, no config options, and UNIX-style composability.











Test here

<img src="./1.png"
     alt="Markdown Monster icon"
     style="
     width: 80%;
     diplay: box;"
/>


## Flag



## More Information

- https://github.com/FiloSottile/age
