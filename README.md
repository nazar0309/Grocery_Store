# Grocery Store

The grocery store is an online store simulator. By entering the program, we can choose a role: Client or admin. For the admin, we first need to enter the correct password. By entering it, we have a choice: add a new product to the store, update the number of existing product and show the whole list of goods from all departments. After each action we can leave the program or go back to the admin pannel.

After logging in for the client, we enter our name, after which we are shown an instruction, after which we need to enter the amount of cash we took with us. Than we select a department, and there is a choice to move to another department or add a product. After selecting the product and its quantity, it is added to the cart. After that, we can proceed to the payment, where we are shown the goods we have chosen and how much cash we have left. If we dont have enough cash, we will be informed about it. After payment, the quantity of goods is automatically updated.

After checkout, we can continue shopping or leave the store

![Home Screen](/readme_images/homepage.png)

[View Grocery Store live project here:](https://grocery-storee-12f87187c033.herokuapp.com/)
- - -

## Table of Contents
### [How to use](#how-to-use-1)
### [Logic Flowchart](#logic-flowchart-1)
### [User Experience (UX)](#user-experience-ux-1)
* [User Stories](#user-stories)
### [Features](#features-1)
* [Existing Features](#existing-features)
### [Features Left to Implement](#features-left-to-implement-1)
### [Design](#design-1)
### [Technologies Used](#technologies-used-1)
### [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used-1)
### [Testing](#testing-1)
### [Manual Testing](#manual-testing-1)
### [Input validation testing](#input-validation-testing-1)
### [Fixed Bugs](#fixed-bugs-1)
### [Deployment](#deployment-1)
* [Deployment to Heroku](#deployment-to-heroku)
* [Forking the GitHub Repository](#forking-the-github-repository)
* [Local Clone](#local-clone)
### [Credits](#credits-1)
* [Code](#code)
* [Content](#content)
### [Acknowledgements](#acknowledgements-1)

## How to Use

To use this program, we need to track the stock of products in our SpreadSheet, which is well organised 
in the tables. More information about the program you can find upon in the description.


## Logic flowchart

![Flowchart1](/readme_images/flowchart_1.png)
![Flowchart2](/readme_images/flowchart_2.png)
![Flowchart3](/readme_images/flowchart_3.png)
![Flowchart4](/readme_images/flowchart_4.png)



## User Experience (UX)

Our application is structured to ensure easy navigation, clear instructions, and efficient operations for all users. Below is an outline of the key aspects of the user experience:

### Navigation

- **Welcome Screen**: Users are greeted with a visually appealing welcome screen featuring a large, welcoming banner. 
- **User Type Selection**: Users can easily select whether they are a customer or an administrator.
- **Department Browsing**: Customers can browse products by selecting from different departments (Meat, Dairy, Vegetables, Fruits, Candies).
- **Product Interaction**: Users can view products, check their availability, add them to the cart, and proceed to checkout with ease.

### Instructions and Feedback

- **Clear Instructions**: Detailed instructions are provided at various stages to guide users through the process.
- **Real-time Feedback**: Users receive immediate feedback on their actions, such as adding products to the cart, updating quantities, or encountering errors.

### Cart and Checkout

- **Cart Management**: Users can easily add products to their cart, review their selections, and see the total price before proceeding to checkout.
- **Payment Processing**: Customers can confirm their purchase and see a summary of their payment.

### Admin Functions

- **Stock Management**: Administrators can add new products, update quantities, and view all stock efficiently.
- **Password Protection**: Access to admin functions is protected by a password to ensure security.

### Error Handling

- **Validation**: Input validations are in place to prevent errors, such as incorrect product numbers or invalid quantities.
- **Error Messages**: Users are informed of any issues with clear, descriptive error messages.

## User Stories

### As a Customer

1. **Browsing Products**
   - **As a customer**, I want to browse products by department, so that I can find what I need easily.
   - **Acceptance Criteria**:
     - Departments are clearly listed.
     - Products within each department are displayed with names, quantities, and prices.

2. **Adding Products to Cart**
   - **As a customer**, I want to add products to my cart, so that I can purchase them.
   - **Acceptance Criteria**:
     - I can select products and specify quantities.
     - The selected products are added to my cart with a running total of the cost.

3. **Viewing Cart**
   - **As a customer**, I want to view the items in my cart, so that I can see what I have selected and the total cost.
   - **Acceptance Criteria**:
     - I can see a list of all items in my cart.
     - The total price of the cart is displayed.

4. **Checking Out**
   - **As a customer**, I want to proceed to checkout, so that I can complete my purchase.
   - **Acceptance Criteria**:
     - If i have enough money, I proceed to payment.
     - I receive a confirmation of my purchase and see my remaining balance.

5. **Managing Budget**
   - **As a customer**, I want to set my budget, so that I can manage my spending.
   - **Acceptance Criteria**:
     - I can input the amount of cash I have.
     - I am notified if I set to much money.

### As an Administrator

1. **Adding New Products**
   - **As an administrator**, I want to add new products to the inventory, so that customers can purchase them.
   - **Acceptance Criteria**:
     - I can input product details such as name, quantity, and price.
     - The new product is added to the relevant department.

2. **Updating Product Quantities**
   - **As an administrator**, I want to update the quantity of existing products, so that the stock levels are accurate.
   - **Acceptance Criteria**:
     - I can select a product and update its quantity.
     - The updated quantity is reflected in the inventory.

3. **Viewing All Stock**
   - **As an administrator**, I want to view all products in the inventory, so that I can manage the store efficiently.
   - **Acceptance Criteria**:
     - I can see a list of all products across all departments with their quantities and prices.

4. **Securing Admin Access**
   - **As an administrator**, I want to protect admin functions with a password, so that unauthorized users cannot make changes.
   - **Acceptance Criteria**:
     - Admin functions are accessible only after entering a correct password.

---


## Features

My application comes packed with a range of features designed to enhance the user experience and streamline store management. Below is an outline of the key features:

### For Customers

1. **User-Friendly Interface**
   - Intuitive and easy-to-navigate interface designed for a smooth shopping experience.
   - Clear categorization of products into departments (Meat, Dairy, Vegetables, Fruits, Candies).

   ![Features1](/readme_images/features_1.png)

2. **Product Browsing**
   - Browse products by selecting specific departments.
   - View detailed product information including name, available quantity, and price.

   ![Features2](/readme_images/features_2.png)

3. **Shopping Cart**
   - Easily add products to the shopping cart with specified quantities.
   - Review cart contents.
   - See a running total of the cost of items in the cart.

   ![Features3](/readme_images/features_3.png)
    
4. **Budget Management**
   - Set a budget and keep track of spending.
   - Receive notifications if the total cart value exceeds the set budget.

    ![Features10](/readme_images/features_10.png)


5. **Seamless Checkout**
   - Confirm and finalize purchases.
   - Receive a summary of the transaction and remaining budget.

   ![Features4](/readme_images/features_4.png)

6. **Track the stock of products using Google Sheets**
   ![Spreadsheet](/readme_images/spreadsheet.png)



### For Administrators

1. **Inventory Management**
   - Add new products to the store with detailed information (name, quantity, price).
   - Update existing product quantities to reflect current stock levels.

   ![Features6](/readme_images/features_6.png)
   ![Features8](/readme_images/features_8.png)

2. **Comprehensive Stock View**
   - View a complete list of all products across all departments.
   - Quickly assess stock levels and identify low-stock items.

   ![Features9](/readme_images/features_9.png)

3. **Secure Access**
   - Protect administrative functions with a password to prevent unauthorized access.
   - Ensure only authorized personnel can manage the store inventory.

   ![Features5](/readme_images/features_5.png)

4. **Real-Time Updates**
   - Real-time updates to inventory and stock levels as products are added, updated, or removed.

    ![Features7](/readme_images/features_7.png)

### Error Handling and Validation

- **Input Validation**
  - Ensure accurate data entry with input validations for product details and quantities.
  - Prevent errors such as incorrect product numbers or invalid quantities.

- **Clear Error Messages**
  - Provide descriptive error messages to guide users in resolving issues.
  - Ensure users are informed of any problems with their actions or inputs.

  ![Features11](/readme_images/features_11.png)


---
## Features Left to Implement

While my Online Grocery Store application already offers a robust set of functionalities, there are several additional features planned to further enhance the user experience and operational efficiency. Below is a list of features currently under development or planned for future releases:

### For Customers

1. **Advanced Search and Filtering**
   - Develop advanced search options and filtering capabilities to help users find products more efficiently.
   - Include filters for price range, brand, dietary preferences, etc.

2. **Product Reviews and Ratings**
   - Enable customers to leave reviews and rate products to provide feedback and assist other shoppers.

### For Administrators

1. **Sales and Analytics Dashboard**
   - Develop a comprehensive dashboard to provide insights into sales trends, customer behavior, and inventory levels.

2. **Discounts and Promotions Management**
   - Implement tools for creating and managing discounts, promotional offers, and coupon codes.


---

## Design

* Colors
    * black
    * white

* Flowchart
    * [Draw.io](http://draw.io/)


---

## Technologies Used

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

---

## Frameworks, Libraries & Programs Used

* [Visual Studio Code](https://code.visualstudio.com/)
    * To write the code.
* [Git](https://git-scm.com/)
    * for version control.
* [Github](https://github.com/)
    * Deployment of the website and storing the files online.
* [Draw.io](http://draw.io/)
    * To create a logic flowchart of the hangman game.
* [Heroku](https://www.heroku.com/)
    * To deploy the project.
* [CI Python Linter](https://pep8ci.herokuapp.com/)
    * Check code for any issues.
* [Google Sheets](https://workspace.google.com/products/sheets/)
    * To track the stock in online-store

# Testing 


* CI Python Linter was used to test run.py:

    ![CI_Python](/readme_images/ci_python.png)

## Manual testing

The Grocery Store was manually tested extensively using Visual Stusio Code terminal, and once the website was deployed on Heroku it was manually tested again, during the creation of the code to the end.

[Here you can find tables that I had created while testing.](README.md)


## Fixed bugs

During the development and testing phases of the Grocery Store, several bugs were identified and resolved to ensure smooth functionality and an optimal user experience. 

[Here you can find tables that I had created while fixing them.](README.md)




# Deployment and local development

## Deploying to Heroku

To deploy with Heroku, Code Institute Python Essentials Template was used so the python code can be viewed in a terminal in a browser
1. Log in to Heroku or create a new account
2. On the main page click "New" and select "Create new app"
3. Choose your unique app name and select your region
4. Click "Create app"
5. On the next page find "settings" and locate "Config Vars"
6. Click "Reveal Config Vars" and add "PORT" key and value "8000", click "Add"
7. Scroll down, locate "Buildpack" and click "Add", select "Python"
8. Repeat step 7. only this time add "Node.js", make sure "Python" is first
9. Scroll to the top and select "Deploy" tab
10. Select GitHub as deployment method and search for your repository and link them together
11. Scroll down and select either "Enable Automatic Deploys" or "Manual Deploy"
12. Deployed site [Grocery Store](https://grocery-storee-12f87187c033.herokuapp.com/)



## How to deploy on GitHub
The website was deployed on GitHub Pages following these steps:

1.Go to GitHub, navigate through Repository/settings/pages.<br>
2.Select "main branch" in the source tab and click save.<br>
3.The page should look like this, which includes the webpages address:<br>

<img src="/assets/readme_images/deployment.png">


## How to Fork and Clone a Project

### Forking a Project

1. **Sign in to GitHub**:
   - Ensure you are logged into your GitHub account.

2. **Navigate to the Repository**:
   - Go to the repository you want to fork. You can use the search bar at the top of the GitHub homepage to find the repository.

3. **Fork the Repository**:
   - Click the "Fork" button in the top-right corner of the repository page.
   - GitHub will create a copy of the repository in your account.

### Cloning a Project

1. **Navigate to Your Forked Repository**:
   - Go to your GitHub profile and navigate to the forked repository.

2. **Get the Repository URL**:
   - Click the "Code" button on the repository page.
   - Copy the URL from the HTTPS tab. It should look something like `https://github.com/your-username/repository.git`.

3. **Open Your Terminal**:
   - Open your terminal or command prompt.

4. **Run the Git Clone Command**:
   ```bash
   git clone <repository-url>

   Replace <repository-url> with the URL you copied. For example:
   git clone https://github.com/your-username/repository.git
   Navigate to the Cloned Repository:
Once the cloning process is complete, navigate to the repository folder:
cd repository
Replace repository with the name of the cloned repository.




Difference between clone and fork: "Forking creates your own copy of a repository in a remote location (for example, GitHub). Your own copy means that you will be able to contribute changes to your copy of the repository without affecting the original repository. Cloning makes a local copy of a repository, not your own copy." <a href="https://www.educative.io/answers/what-is-the-difference-between-forking-and-cloning-in-git">Full explanation</a><br>

## Credits

### Code

* I gained understanding of python through code institute lessons.
* Python 3.11.3 documentation.


### Content

* All content was written by the developer.
* To create Grocery Store welcome message i have used <a href = 'https://en.wikipedia.org/wiki/ASCII_art'>ASCII art documentation</a>

## Acknowledgements

 * My mentor Mitko Bachvarov provided helpful feedback.
 * Slack community for encouragement.










