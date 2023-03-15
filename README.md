# Rock Paper Scissors Lizard Spock

RPSLS is an easy game designed for any type of audience, especially for fans of the serie "The Bigbang Theory", as this version of the game became popular because of it. To make it a bit more exciting, the game presents 3 possible variations:
- classic
- 5vs5
- random

![Responsice Mockup](assets/image/readmeimages/AmIResponsive.png)

# [Visit the game here](https://max9414.github.io/RPSLS/)

# All the titles bring back to the Table of Content

# Table of Content
1. [Project Goals](#project-goals)
   - [Site Owner Goals](#site-owner-goals)
   - [User Goals](#user-goals)
   - [Target Audience](#target-audience)
   - [User Stories](#user-stories)
     - [First time user](#first-time-user)
     - [Returning User](#returning-user)
2. [Features](#features)
3. [Existing Features](#existing-features)
4. [Features Left to Implement](#features-left-to-implement)
5. [Testing](#testing)
   - [Validator Testing](#validator-testing)
6. [Unfixed Bugs](#unfixed-bugs)
7. [Deployment](#deployment)
8. [Credits](#credits)
9. [Content](#content)
10. [Media](#media)


## [Project Goals](#table-of-content)

This Battleship project aims to let the player enjoy an easy and stressfree game that everyone played atleast once in their life, bringing back childhood memories in a nice and easy way

### [Site Owner Goals](#table-of-content) 
- Test User luck
- Create the pc logic to give the player an "enemy" to play against
- Provide entertainment
- Show both user and pc scores

### [User Goals](#table-of-content)
- Easily play the game
- Spot errors when I input something wrong
- Clear messages
- Enjoyable game

### [Target Audience](#table-of-content)
- Everyone who played the game in their childhood
- Anyone who wants to enjoy a simple game in a short freetime period.

### [User Stories](#table-of-content)

#### [First-time User](#table-of-content)
- As a first-time visitor I want to:
  - Get familiar with the game
  - Have a chance to play all different sizes
  - Be able to modify all the game options aka ship number, size and turns to play
#### [Returning User](#table-of-content)
- As a returning-user I want to:
  - Easily play the game
  - Play a fast paced game with clear indications

## [Features](#table-of-content) 

### [Existing Features](#table-of-content)

- Boards creation
- Ships creation
- Ships showcase
- Messages hit/not hit
- Score for both player and pc
- Turn showed

### [Features Left to Implement](#table-of-content)

- The game could be modified so to create more "Complicated" ships, as in longer ships taking 2 units instead of one or something similar

## [Testing](#table-of-content) 

Asked friends to test the game and play around with it to check that everything works smoothly.

I started this process pretty early in the creation as I thought it would have helped me improving the functions and it did!

One of the hardest errors I faced was with an if statement, where a small word as and/or completely changes the logic and is sometimes so hard to spot.


### [Validator Testing](#table-of-content) 

### [Unfixed Bugs](#table-of-content)

Debugging

- Found a bug which took me ages to debug where my while loop was never ending. It was really hard to find at the beginning, but mentor greatly helped me with debugging. 

- I had another bug on one of the last while loops I implemented, where if I was selecting more ships than rows/columns the program was just entering an infinite loop.
It was kind of hard debugging it, basically the problem was that my creation function was meant to have only 1 for every number from 0 to number of rows/cols without repetitions.
It took a little while to understand exactly what I've done wrong and then a little longer to understand how to create a function that was actually allowing repetitions and 
was checking for duplicates. The last problem was the "and" instead of "or". It was such a small thing that it took me a while to find.

## [Deployment](#table-of-content) 

These are the steps I followed to deploy the program

Created the repository on Github

Created these buildpacks:

heroku/python
heroku/nodejs

Created a Var with port and value of 8000

Connected my GitHub repository and deployed as normal.


### [Content](#table-of-content) 

- The game idea is taken from the given ideas for this exam, following the simplest rules with ships with no different sizes.


# The End.

