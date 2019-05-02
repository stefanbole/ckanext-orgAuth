This repository is used as example extension for CKAN.

Example extension created here is the one explained in [CKAN Docs - Creating extension.](https://docs.ckan.org/en/2.8/extensions/tutorial.html#creating-a-new-extension)

## Logic part

### Testing

1. Register as new user under some random name
2. Open **Organizations** in Header as that new user
3. Button **Add Organization** is not present on the page
4. Login as admin user
5. Create group under the name **org-mods**
6. Add created user in group **org-mods** 
7. Open **Organizations** in Header as created user
8. Button **Add Organization** is now present on the page

#### Conclusion

Only users which are in the group **org-mods** can create new group.

 
## Template part

Html part is altered in a way that when you go to the Header tab About you will see a link to this github repository.