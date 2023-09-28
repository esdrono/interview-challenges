# interview-challenges

The purpose of this repository is to provide coding challenges that require debuging and programming skills, please take in mind that the code here is not optimized and intentionally have multiple errors, please do not assume the code works as expected and solve the issues based on the requirements of each challenge. Read cearfully to really understand what is needed and make the programs work as expected. Don't hesitate to ask questions if something is unclear.

## Instructions

1. Setup a development environment in Linux with Python
2. Fork this repository into your own account
3. Clone the repository
4. Complete each challenge or the ones indicated by interviewer

## Challenge 1

### The Pyramid

#### Instructions

Go to pyramid folder and update pyramid.py to work with main.py.

A pyramid consists of multiple levels of blocks stacked where each subsequent level contains one block more than the previos one, starting from the top, the first level contains one block, the second level contains 2 blocks, the third level contains 3 blocks.

A visual representation of 10 numbered blocks in a pyramid goes as follow:

1

2 3

4 5 6

7 8 9 10

The pyramid.py file should contain the get_height function that receives N number of blocks used to build the pyramid, and outputs the height (or level) of the pyramid resulting from using N number of blocks.

For example, if the value 8 is passed to get_height, the output shoud be 4, because thats the height of the pyramid (see visual representation above) in other words the block number 8 is at level 4.

#### Bonus challenge (Optional)

Uncomment the rest of the assert evaluations in main.py and complete the code to work with the functions:

* get_max_blocks: gets the height (level) of a pyramid and returns the maximum number of blocks that can be used to build such pyramid.
* get_min_blocks: gets the height (level) of a pyramid and returns the minimum number of blocks that cam be used to build such pyramid.

## Challenge 2

### The API client

#### Instructions

Go to api_client folder and update api_client.py and main.py to work together

This challenge requires some python dependencies, install them by executing the command: `./install.sh`. If there are any issues during the installation, you will need to solve them.

The API client consist in 4 functions:

* get_todo: gets a "todo" data
* get_user: gets a "user" data
* get_todo_list: gets a list of "todo" data
* read_todo_data: parses a list of "todo" data from a file

The main.py should be executed to get a list of todos with IDs: [1, 50, 200], then read the 2 todo entries from data.json file and add them to the list.

After that, query the users from the todo list and add them to each todo dictionary in a field named 'user', then print the todo list.

