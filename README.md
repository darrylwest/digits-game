# Digits Game

## What we know

* target numbers are 2 or 3 digit integers, 50..999
* pool of numbers is always 6, unique counting numbers 1..99
* it usually takes 4 terms to get to the solution
* more than likely the highest numbers should be multiplied by a lesser number

## Questions

* target is always larger than any one variable from the list?
* the sum of the list is always smaller than the target?
* what would a graph of target and given values look like? a series of graphs?
* are prime numbers more difficult to resolve?
* is the best approach to use product and addition, then subtraction and division?
* division is tricky because if the result isn't an integer, it's useless, right?

## Biggest factors First

* sort list of numbers in ascending order
* select the largest number from the array and multiply by all the others, starting with the first number (greater than 1)

* for each iteration see if there is a product that when combined with addition or subtraction resolves to the target
* use the remaining digits to see if there is a combination to get to the difference target
* repeat

## Division

* loop over all numbers and divide and truncate (modulus) into target number
* 

## Factors Algorithm

* get the factors for the target number
* try to match any of the factors to factors of the list of numbers
* remove any factors
* try to com

## Brute Force Dictionary Algorithm

* create a dictionary of targets between 50..999
* determine every possible product/sum for each target given 6 unique digits 1..99



###### darryl.west | 2023.06.10
