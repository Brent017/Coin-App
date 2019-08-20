# Coin-App

Coin colleting is not just a hobby, it's an investment.  Coin App contains a database of US coins which allows a user to view a variety of information about a specific coin and catalogue their own collection.  Users have access to coins' melt and numismatic value to understand what their collection is worth.


## User Story-
### MVP:
  *User will be able to login using unique username and hashed password.
  *User will be able to search coin database for a given coin.
  *User will be able to create, read, update and delete information about their personal collection database.


### Stretch:
  *User (U) can upload personal photo or use avatar.
  *U can upload photos of their collection.
  *U can create a wishlist and view current value of items.
  *App will be nicely styled.
  *U will be able to see value of individual coins in their collection based on values in the coin database.
  *U will be able to see the total value of their collection.
  *Integrate Express API.
  *Create a marketplace for users to buy and sell from their collection.
  *Currency implementation.

|URL        | HTTP Verb | Action | Description       |
|-----------|:---------:|:------:|:------------------|
|/coins/    | GET       | index  | Show all coins    |
|/coins/new | GET       | new    | Show new form     |
|/coins     | POST      | create | Create an item    |
|/coins/:id | GET       | show   | Show item with :id|
|/coins/:id/edit| GET   | edit   | Show edit form for item with :id|
|/coins/:id | PATCH     | update | Update item with :id |
|/coins/:id | GET       | delete | Show delete form for item with :id|
|/coins/:id | DELETE    | destroy| Delete item with :id|
