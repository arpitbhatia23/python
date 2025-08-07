import json 


def  load_data():
    try:
        with open('youtube.txt','r') as file:
            test=json.load(file)

            return  test
    except FileNotFoundError:
        return []
    

def save_data_helper(videos):
    with open('youtube.txt',"w") as file:
        json.dump(videos,file)



def list_all_video(videos):
    for index,video in enumerate(videos,start=1):
        print('\n')
        print('*'*70)
        print(f"{index}.name: {video["name"]} time:{video["time"]}") 
        print('*'*70)
        print('\n')


def add_video(videos):
    name=input("enter video name: ")
    time=input("enter video time ")
    videos.append({"name":name,"time":time})
    save_data_helper(videos)

def update_video(videos):
    list_all_video(videos)
    index=int(input("input enter the video number to update "))
    if 1<=index <= len(videos):
        name=input("enter new video name ")
        time=input("enter the new time")
        videos[index-1]={'name':name,"time":time}
        save_data_helper(videos)
    else:
        print('invalid  video index')




def delete_video(videos):
    list_all_video(videos)
    index=int(input("enter the video numver to delete "))
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("invalid video number")



def main():

    videos=load_data()

    while True :
        print("\n youtube manager | choose an option")
        print('\n 1. list all videos')
        print('\n 2. add a youtube video')
        print('\n 3. update a youtube video')
        print('\n 4. delete a youtube video')
        print('\n 5. exit')
        choice=input("enter your choice : ")
        # print(f"{videos}")


        match choice:
            case '1':
                list_all_video(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print("exiting the program")
                break
            case _:
                print('invalid choice, please try again')



if __name__ == "__main__":
    main()

