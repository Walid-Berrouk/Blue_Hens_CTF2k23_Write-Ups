# Appetizers 

## Description

> https://gist.github.com/AndyNovo/7527b97a69b7ee31c89ea6789f609abf
>
> This one goes (NP) hard!

## Write-Up

From the given image and the description, it seems that we are dealing with an **NP-Hard** problem, and when checking the `knapsack.py` script, it tells us that it's a **Subset Sum Problem**.

<img src="./np_complete.png"
     alt="Markdown Monster icon"
     style="
     width: 80%;
     diplay: box;"
/>

> The SUBSET-SUM problem involves determining whether or not a subset from a list of integers can sum to a target value. For example, consider the list of nums = [1, 2, 3, 4] . If the target = 7 , there are two subsets that achieve this sum: {3, 4} and {1, 2, 4} . If target = 11 , there are no solutions.

From there, since the combination of subsets isn't that big (comb(30, 15)), let's try a brute force attack to find the winner numbers:

```
Combination:  [19728964, 30673077, 137289540, 195938621, 237735979, 302597011, 463977415, 603269308, 654758801, 670668388, 763314787, 806543382, 875651556, 918697500, 946831967]
```

From there, we reconstiture the flag:

```
UDCTF{19728964_30673077_137289540_195938621_237735979_302597011_463977415_603269308_654758801_670668388_763314787_806543382_875651556_918697500_946831967}
```


## Flag

UDCTF{19728964_30673077_137289540_195938621_237735979_302597011_463977415_603269308_654758801_670668388_763314787_806543382_875651556_918697500_946831967}

## More Information

- https://gist.github.com/okoye/168f5ae70e57043fb9b3
