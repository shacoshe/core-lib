---
id: main
title: Getting started
sidebar_label: Getting started
---

# What is Core-Lib

CoreLib provides basic simple classes for creating a WEB Application as a Library using the Onion Architecture. [1](https://www.codeguru.com/csharp/csharp/cs_misc/designtechniques/understanding-onion-architecture.html) [2](https://www.google.com/search?sxsrf=ACYBGNT0NhYbUZLnDQbC9b6uPBqjZmjwgw%3A1579104811273&ei=KzofXuOfEO3IgwfngLPwAg&q=onion+Architecture&oq=onion+Architecture&gs_l=psy-ab.12...0.0..109691...0.0..0.0.0.......0......gws-wiz.oEYi3afxy_c&ved=0ahUKEwij4drq_4XnAhVt5OAKHWfADC4Q4dUDCAs)   

# Why Core-Lib

The main reason is the Tight Coupling of our products to a third party application the WEB Framework.   
by taking this into account Core-Lib will not delegate any other framework classes.    
it will only provide basic tools to arrange our code more efficiently.

## Pros
* Easy to use
* Use dependencies directly (no third party delegation of third party libraries)
* Leverage Onion Architecture for fast expansion.
* Simple mechanisms   

## Cons
* Manage many vendors 


## Installing

    pip install core-lib

## Requirements

    python > 3.7

## Running tests

    python -m unittest discover

## The source

[https://github.com/shacoshe/core-lib](https://github.com/shacoshe/core-lib)
   
## Example project

[https://github.com/shacoshe/bigpipe-response-example](https://github.com/shacoshe/bigpipe-response-example)

## Pros:    
* no need to wait for javascript code to ajax and fetch data/code  
* more connection available by the browser for resources 
* no network time for opening more TCP/HTTP connections [1](https://www.cse.iitk.ac.in/users/dheeraj/cs425/lec14.html)

## Cons:    
* dismisses the browser cache mechanism for embedded results

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.


## Authors

**Shay Tessler**  - [github](https://github.com/shacoshe)


## License

This project is licensed under the MIT - see the [LICENSE](https://github.com/shacoshe/core-lib/blob/master/LICENSE) file for details
