import api_client

def main():
    todo_list = api_client.get_todo_list([1, 50, 200])
    
    todos_from_file = api_client.read_todo_file('data.json')
    todo_list.extend(todos_from_file)
    
    for todo in todo_list:
        user_data = api_client.get_user(int(todo['userId']))
        todo['user'] = user_data
        
    print(todo_list)

if __name__ == '__main__':
    main()
