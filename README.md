# Digits Game

## solve-digits

With help from itertools the implementation uses 

USE: `solve-digits -t target -n numbers`

## Bugs / Improvements

* [ ] if there is a result that starts with a negative number, switch it to be at the end of the equation (negative numbers not possible in the game)
* [ ] parse and group the result to ensure it works correctly with the game.
* [ ] should create a UI for this app
* [ ] should log all results to keep track of game plays

## Known

* large targets sometimes require three terms as products (see day 3 game 4)
* target numbers are 2 or 3 digit integers, 50..999
* pool of numbers is always 6, unique counting numbers 1..25
* it usually takes 4 terms to get to the solution
* more than likely the highest numbers should be multiplied by a lesser number

## Web Application(s) and API

* [ ] must support async, web sockets, http2
* [ ] enable separation between API backend and web, mobile, desktop front ends
* [ ] initial API should accept target/numbers and return result equation
* [ ] enhance to generate new games

[Async Web Frameworks](https://geekflare.com/python-asynchronous-web-frameworks/)
[FastAPI](https://fastapi.tiangolo.com/)

## References

[graph of game plays](https://www.desmos.com/calculator/gsozkpvp6o)
[itertools](https://docs.python.org/3/library/itertools.html)
[the game](https://www.nytimes.com/games/digits)

###### darryl.west | 2023.06.12
