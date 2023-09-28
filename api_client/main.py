import api_client


def main():
    todo_list = api_client.get_todo_list([1,50,200])
    todo_list.append(api_client.read_todo_list('data.json'))
    for todo in todo_list:
        pass
        ## Include a field named 'user' with the value of the user
    print(todo_list)


if __name__ == '__main__':
    main()
