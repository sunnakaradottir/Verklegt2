# Verklegt2

## superuser
### username: sunna
### password: Verklegt2

## user that created existing items
### username: verklegt2
### password: firesale

## Pip requirements are found in requirements.txt

## Extra requirements 
- Category sorting
- My listings both current and previous
- My orders
- Location of item
- Delete item (only for owner)
- View bids (only for owner)
- Comment on seller
- Able to cancel offer if it is accepted
- Order by both ascending and descending
- See reviews from each buyer
- Favorite items you like
- Favorite items are stored under favorites in your profile
- Information on seller in item details

## Authentication
- User can login by clicking on "log in" from the navigation bar
- User can register by clicking on "register" from the navigation bar

## Layout site
### Navigation bar
- Profile image is displayed on the right side of the navigation bar when user is logged in. By default, the navbar displays a profile picture indicating the user has not set one. 
- Average rating for the user is displayed in the dropdown menu of the navbar. By default, this will be N/A. Once the user recieves ratings, this will be updated. The user can click on this to view all the ratings he has recieved from other users.
- The user can log out by clicking on "log out" in the navigation bar.

## Edit profile
- The user can click on his username (dropdown menu), then "My account" - there he is provided with the option to create/edit his profile. He is able to edit Name, Profile image and bio.

## Catalog site
- On the catalog site (the landing page) the user can search for items in the search bar, order items by name and price. Each item displayed on the catalog site is clickable. Only available items are displayed here.

## Create an item
- On the navigation bar, the user can click on "New Listing" to create a new item. He fills out the form containing the relevant fields and submits, then a new item is created.

## Item detail site
- This site appears when the user clicks on an item. It contains all relevant information about the item.
- If you are the owner of the item you can: Delete the item, View bids for the item
- If you are not the owner you can: Bid on item, Add the item to favorites

## Placing an offer
- Offers are placed on the item detail site. Users can send multiple offers, until the owner accepts an offer.
- All users who placed an offer on the item recieve a message in their inbox if their offer was accepted/rejected. The user has the option to edit his notification settings, i.e. adding email notifications. This is done in the dropdown menu by clicking on "Notification Settings". The user always recieves a message in their inbox regardless of this.

## Checkout
- The user can see if his offer has been accepted in the inbox (also if it has been rejected)
- The user can click on "Go to checkout" if he wants to finish his purchase or "Cancel" if he wants to withdraw his offer. If the user withdraws his offer, the owner of the item recieves a message regarding this and an email if his notification settings are set to email notifications. The item is then set to available again.
- If he clicks "Got to checkout" the user must put in his contact information. He is presented with the option to navigate back if he wishes. If he presses next he will be redirected to a payment information form. On the top of this form the user is presented with the steps required to complete the checkout process and the status he is at.
- After the payment information form is filled out the user can again, either press back or next by his preference. He can choose to rate the seller on the scale from 0-5, and also leave a comment if he wishes.
- The user then gets a read-only review of his order before he clicks on "Confirm Checkout". On this page, the user can also navigate back to previous forms if he made errors. 

