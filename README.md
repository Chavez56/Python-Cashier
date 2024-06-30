# Python Project - Super Cashier

## 1. Background

Super Cashier is a simple program to help customer for doing transaction independently in the shop/supermarket. Customer can add bought items, item quantity and price per item and get discount if the transaction met the total price requirements.

## 2. Tools
Programming Languages and Software:
- Python
- Visual Studio Code

Library:
- Tabulate

## 3. Objective

#### Learning Objective:
- Create simple program cashier using Python
- Utilize OOP, Function, Exception Handling, and PEP8 principles to create Python Program
- Utilize modularization to create module script

#### Program Objective:
- Customer can add item name, item quantity, and price per item
- Customer can update item name/item quantity/price per item
- Customer can delete one item/more items
- Customer can reset their order
- Customer can check their order and total price

## 4. Flowchart

![Alt text](screenshot/Flowchart.png)

#### Description:
-  Transaction module imported and its class called by Consumer
-  Consumer can start their transaction
-  Consumer add item, quantity, and price with method **add_item**
-  Consumer can update their order with:
   (1) **update_item_name** for changing item name;
   (2) **update_item_quantity** for updating item quantity;
   (3) **update_item_price** for updating price of item.
- If they cancel to buy one item or more items, Consumer can use method **delete_item** with inserting item name
- If they cancel order, Consumer can use method **reset_transaction** and start order again
- If their order is done, Consumer can check order with method **check_order**
- Consumer get total price and discount if their total price is met the requirements with method **total_price**

## 5. Code Explanation

- **_main.py_**: The main script work as program simulation and import module transaction
- **_module_transaction.py_**: The module script that has class Transaction and its function methods

![Alt text](screenshot/class_table.png)

![Alt text](screenshot/function1.png)

![Alt text](screenshot/function2.png)


## 6. Test Case

Import module and assign its class in main script:

![Alt text](screenshot/Import_module.png)

#### 1. Customer add item name, item quantity, and price per item

- Code:

  ![Alt text](screenshot/code_test1.png)

- Result:

  ![Alt text](screenshot/test1.png)


#### 2. Customer delete item

- Code:

  ![Alt text](screenshot/code_test2.png)

- Result:

  ![Alt text](screenshot/test2.png)


#### 3. Customer reset their order

- Code:

  ![Alt text](screenshot/code_test3.png)

- Result:

  ![Alt text](screenshot/test3.png)

#### 4. Customer check their order and total price

- Code:

  ![Alt text](screenshot/code_test4.png)

- Result:

  ![Alt text](screenshot/test4.png)

#### 5. Customer update item name/item quantity/price per item

- Code:

  ![Alt text](screenshot/code_test5.png)

- Result:

  ![Alt text](screenshot/test5.png)

## 7. Special Test Case

Customer input empty item name

- Code:

  ![Alt text](screenshot/code_specialcase.png)

- Result:

  ![Alt text](screenshot/test_special.png)

## 8. Conclusion and Future Work

#### Conclusion:
With Super Cashier Program, Consumer can do their transaction independently. It is hoped that it can help business actors in optimizing their business processes.

#### Future Work:
- Can be added with the choice option for transaction
- Can be added with list of items in the shop/supermarket to identify whether the item is available or not
- Can be added with list of items that have been expired and give suggestion to customer




