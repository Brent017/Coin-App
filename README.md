# Coin-App

Most coin collectors accumulate their collection for the enjoyment and history of the coins.  Many do not consider the overall value of their collection or catalogue every individual item.  Coin collecting is not just a hobby, it's also an investment.  Coin App contains a database of US coins which allows a user to view a variety of information about a specific coin and catalogue their own collection.  Users have access to coins' melt and numismatic value to understand what each item as well as their total collection is worth.

## User Story-
### MVP:
  * User will be able to login using unique username and hashed password.
  * User will be able to search coin database for a given coin.
  * User will be able to add (create) a coin to their personal collection database.
  * User will be able to add (read) information about a specific coin or their entire collection.
  * User will be able to add (update) information about a specific coin in their collection.
  * User will be able to add (delete) a specific coin from their collection.

### Stretch:
  * User can upload personal photo or use avatar.
  * User can upload photos of their collection.
  * Random coin fact will populate on screen load.
  * User can create a wishlist and view current value of items.
  * Wishlist will access 3rd party api selling those items (ebay).
  * App will be nicely styled.
  * Userwill be able to see value of individual coins in their collection based on values in the coin database.
  * User will be able to see the total value of their collection.
  * Integrate Express API.
  * Create a marketplace for users to buy and sell from their collection.
  * Currency implementation.

|URL        | HTTP Verb | Action | Description       |
|-----------|:---------:|:------:|:------------------|
|/coins/    | GET       | index  | Show all coins    |
|/coins/new | GET       | new    | Show new form     |
|/coins     | POST      | create | Create an item    |
|/coins/:id | GET       | show   | Show item with :id|
|/coins/:id/edit| GET   | edit   | Show edit form for item with :id|
|/coins/:id | PUT     | update | Update item with :id |
|/coins/:id | DELETE    | destroy| Delete item with :id|
