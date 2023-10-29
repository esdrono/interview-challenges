import api_client

def main():
    # Get todos by ID
    todo_list = api_client.get_todo_list([1, 50, 200])

    # Read todos from file
    todos_from_file = api_client.read_todo_file('data.json')

    # Merge the two lists
    todo_list.extend(todos_from_file)

    # Add user data to todos
    for todo in todo_list:
        user_data = api_client.get_user(int(todo['userId']))
        todo['user'] = user_data

    # Print the complete todo list
    print(todo_list)

if __name__ == '__main__':
    main()
