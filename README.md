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
     - I can confirm my cart and proceed to payment.
     - I receive a confirmation of my purchase and see my remaining balance.

5. **Managing Budget**
   - **As a customer**, I want to set my budget, so that I can manage my spending.
   - **Acceptance Criteria**:
     - I can input the amount of cash I have.
     - I am notified if I exceed my budget.

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






