# Digits Game

## Known

* target numbers are 2 or 3 digit integers, 50..999
* pool of numbers is always 6, unique counting numbers 1..99
* the number values in the pool are usually < 30
* it usually takes 4 terms to get to the solution
* more than likely the highest numbers should be multiplied by a lesser number

## Questions

* what would a graph of target and given values look like? a series of scatter graphs
* is the best approach to use product and addition, then subtraction and division?
* division is tricky because if the result isn't an integer, it's useless, right?

## Factors Algorithm

* get the factors for the target number
* match factors to the list of numbers
* on a match, get factors for that target
* most likely pattern is multiplying the top to numbers, subtract from the target, and run facors again

## Biggest factors First

* sort list of numbers in ascending order
* select the largest number from the array and multiply by all the others while getting factors for each product
* determine if the factors (and factors of factors) are in the list of numbers
* for each iteration see if there is a product that when combined with addition or subtraction resolves to the target
* use the remaining digits to see if there is a combination to get to the difference target
* repeat

## Brute Force Dictionary Algorithm

*Note: its unlikely that a simple addition would ever be possible for the digits game*

* create a dictionary of targets between 50..999
* determine every possible product/sum for each target given 6 unique digits 1..99

## References

[graph of game plays](https://www.desmos.com/calculator/gsozkpvp6o)

###### darryl.west | 2023.06.10a
