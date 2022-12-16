## Functional Requirements
1. Login (Joao)
2. Logout (Romuz)
3. Create New Account (Tan)
4. Delete Account (Choyee)
5. User Home Page (Joao)
6. Send Messages to Followers (Romuz)
7. Follow Users (Tan)
8. Search Users (Choyee)
9. Post Images with Message (Joao)
10. Connect with External API (Romuz)
11. Users Profile (Tan)
12. Authentication (verified) (Choyee)
## Non-functional Requirements
1. Using elements from Bootstrap
2. Date format shall follow month-day-year
3. Dark Mode
4. Responsive UI 

## Use Cases
1. Edit user profile 
- **Pre-condition:** 
  - Searching user has a registered account.
  - User has logged in  
- **Trigger:**
  - The user clicks on profile icon on home page 
- **Primary Sequence:**
  1. System directs the user to the profile page
  2. The user selects "Edit" option 
  3. The system prompts a form for updating information
  4. The user makes some changes
  5. The user selects "Save Profile" button
- **Primary Postconditions:**
  - The user successfully update the new information 
  OR
  - The user fails to update because of invalid changes
- **Alternate Sequence:** 
  - The user goes to a different page without clicking on "Update"
  - The system discards all the unsaved changes by clicking "Cancel" button

2. Send Messages to Followers
- **Pre-condition:** 
  - User has logged in
- **Trigger:**
  - User goes to the home page
- **Primary Sequence:**
  1. User starts typing the message inside the text box
  2. User clicks "chirp" button
- **Primary Postconditions:**
  - System shows "posted"
- **Alternate Sequence:** 
  - User cancel the message

3. Follow Users  
- **Pre-condition:**  
  -  User has logged in 
- **Trigger:**
  - User clicks “Follow” button
- **Primary Sequence:** 
  1. User search by the username
  2. User clicks on the other user's profile
  3. User clicks the "follow" button
- **Primary Postconditions:**
  - Button will change to “Following”
  - User can see what they post on their home page
- **Alternate Sequence:** 
  - User clicks “Follow” button twice or user wants to unfollow
  - “Following” button change to “Follow”
  - System will ask “Unfollow @username?” 
  - Choose “Unfollow” or “Cancel”

4. Search Users  
- **Pre-condition:**  
  - User has logged in 
- **Trigger:**
  - User clicks “search” button from drop-down menu
- **Primary Sequence:**
  1. Search bar will appear 
  2. User type inside the search bar
  3. Display all users with similar name(optional)
  4. User click on the profile
- **Primary Postconditions:**
  - Re-route to profile that user wants to look for 
- **Alternate Sequence:** 
  - If no username exits, display error message

5. Post Images with Message  
- **Pre-condition:**  
  - User has logged in 
  - User needs to be in home page
- **Trigger:**
 -  User goes to “what’s happening?” bar
- **Primary Sequence:**
  1. User types message inside the bar
  2. User clicks “image” button
  3. User selects up to 4 images
  4. User clicks “Chirp”
- **Primary Postconditions:** 
  - User’s chirp will appear on the homepage
- **Alternate Sequence:** 
  - User doen’t want to include the image and cross out the image before chirping

6. User Home Page 
- **Pre-condition:**  
  - User has logged in 
- **Trigger:**
  - After user clicks the “Sign In” button or “Home” button
- **Primary Sequence:**
  1. User can see follower’s chirp
  2. User can access to drop-down menu
- **Primary Postconditions:**
  - Re-route to other pages that user selects
- **Alternate Sequence:** 
  - User log out and re-route to Sign In page

