def subsetsum(numbers, target):
   size = 1
   subsets = []
   while size <= len(numbers):
      for combination in combinations(numbers, size):
         if sum(combination) == target:
            print("Combination: ", combination)
            subsets.append(combination)
      size += 1
   return subsets


def combinations(numbers, size):
   if len(numbers) <= 0 or size <= 0:
      yield []
   else:
      for index, number in enumerate(numbers):
         for combination in combinations(numbers[index+1:], size-1):
            yield [number]+combination

numbers = [19728964, 30673077, 137289540, 195938621, 207242611, 237735979, 298141799, 302597011, 387047012, 405520686, 424852916, 461998372, 463977415, 528505766, 557896298, 603269308, 613528675, 621228168, 654758801, 670668388, 741571487, 753993381, 763314787, 770263388, 806543382, 864409584, 875042623, 875651556, 918697500, 946831967]
size = 15
target = 7627676296

print(subsetsum(numbers, target))

# Combination:  [19728964, 30673077, 137289540, 195938621, 237735979, 302597011, 463977415, 603269308, 654758801, 670668388, 763314787, 806543382, 875651556, 918697500, 946831967]

winners = [19728964, 30673077, 137289540, 195938621, 237735979, 302597011, 463977415, 603269308, 654758801, 670668388, 763314787, 806543382, 875651556, 918697500, 946831967]

winners.sort()
flag = "UDCTF{%s}" % ("_".join(map(str,winners)))
print(flag)
