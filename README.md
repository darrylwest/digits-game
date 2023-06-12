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

FastAPI is a modern web framework for building APIs with Python 3.7+ based on standard Python type hints. It is designed around open standards such as OpenAPI for API creation and JSON Schema for automatic data model documentation ². FastAPI fully supports asynchronous programming and can run on ASGI servers such as Uvicorn and Hypercorn ⁶.

FastAPI has quickly gained popularity among developers due to its ease of use, speed, and robustness ⁶. According to a Stack Overflow Developer Survey, FastAPI has the third ranking of the most loved web framework ⁷. Some big worldwide companies that currently use FastAPI include Uber, Microsoft, Netflix, Explosion AI, Payhere, Primer, yogiyo and others ⁷.


Source: Conversation with Bing, 6/12/2023
(1) Features - FastAPI - tiangolo. https://fastapi.tiangolo.com/features/.
(2) FastAPI - Wikipedia. https://en.wikipedia.org/wiki/FastAPI.
(3) Pros and Cons of FastAPI - LinkedIn. https://www.linkedin.com/pulse/pros-cons-fastapi-digi2world.
(4) FastAPI vs. Flask: Which of the Two is Right For You?. https://geekflare.com/fastapi-vs-flask/.
(5) FastAPI - tiangolo. https://fastapi.tiangolo.com/.
(6) fastapi · PyPI. https://pypi.org/project/fastapi/.
(7) The Most Popular Python Web Frameworks in 2021 - Scout APM. https://scoutapm.com/blog/the-most-popular-python-web-frameworks-in-2020.

* [FastAPI](https://fastapi.tiangolo.com/)
* [Animate.css](https://animate.style/)
* [Wiki](https://en.wikipedia.org/wiki/FastAPI)
* [Popularity](https://www.linkedin.com/pulse/pros-cons-fastapi-digi2world)
* [PyPi reference](https://www.linkedin.com/pulse/pros-cons-fastapi-digi2world)
* [Async Web Frameworks](https://geekflare.com/python-asynchronous-web-frameworks/)

## References

* [graph of game plays](https://www.desmos.com/calculator/gsozkpvp6o)
* [itertools](https://docs.python.org/3/library/itertools.html)
* [the game](https://www.nytimes.com/games/digits)

###### darryl.west | 2023.06.12
