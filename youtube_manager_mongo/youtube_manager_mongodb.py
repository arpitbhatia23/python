from pymongo import MongoClient
from bson import ObjectId
MONGODB_URI="mongodb+srv://Aurpit:aurpit23@ecomerce.ja8or03.mongodb.net/"

# not a good idea to inducled id and password in code 
# 
try:
    client=MongoClient(MONGODB_URI,tlsAllowInvalidCertificates=True)
except Exception as e:
    print(str(e))

db=client["ytmanager"]
videos_collection=db["videos"]


def list_all_video():
    videos=videos_collection.find()
    videos=list(videos)
    if len(list(videos))==0:
        print("no video found")
    else:
        for video in videos:
            print('\n')
            print('*'*70)
            print(f"Id: {video["_id"]} name: {video["name"]} time: {video["time"]}")
            print('*'*70)
            print('\n')


def add_video(name,time):
    videos_collection.insert_one({"name":name,"time":time})
    print("video added successfully")


def update_video(video_id,name,time):
    videos_collection.update_one({"_id":ObjectId(video_id)},{"$set":{"name":name,"time":time}})
    print("video updated successfully")



def delete_video(video_id):
    delete= videos_collection.delete_one({"_id":ObjectId(video_id)})
    print("video deleted successfully")


def main():
    while True:
        print("\n youtube manager app with mongoDB")
        print("\n 1. list video ")
        print('\n 2. add video ')
        print('\n 3. update video')
        print('\n 4. delete video')
        print('\n 5. exit')

        choice=input("enter your choice : ")
        match choice:
            case '1':
                list_all_video()
            case '2':
                name=input("enter video name: ")
                time=input("enter video time: ")
                add_video(name,time)
            case '3':
                video_id=input("eneter the video id to update: ")
                name=input("enter updated video  name: ")
                time=input("enter updated video time: ")
                update_video(video_id,name,time)
            case '4':
                video_id=input("eneter the video id to delete: ")

                delete_video(video_id)
            case '5':
                print("exiting the program")
                break
            case _:
                print('invalid choice, please try again')


if __name__=="__main__":
    main()


