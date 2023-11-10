# Python Jail

## Description

> No ASCII letters are allowed.
> 
> Remote is running `Python 3.10.12 (main, Jun 11 2023, 05:26:28) [GCC 11.4.0]`
>
> `nc 0.cloud.chals.io 20483`

## Write-Up

First, we note that we can't use ascii chars, which can easily be bypassed using unicode chars (checkout: [nicode Pentester Cheatsheet](https://gosecure.github.io/unicode-pentester-cheatsheet/)), where any chars can be replaced with another char with same nature but different unicode.

Also, as there is no builtins, we will need to import our needs.


## Flag



## More Information

- https://gosecure.github.io/unicode-pentester-cheatsheet/
