import sqlite3

conn=sqlite3.connect("youtube_video.db")

cursor=conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL  
    )
''')

def list_video():
    try:
        cursor.execute("SELECT * FROM videos")
        rows=cursor.fetchall()
        if not rows:
            print("video not found")
        else:
            for row in rows:
                print(f"{row[0] } {row[1]} {row[2]}")
    except FileNotFoundError:
        print(" videos not found")

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)",(name,time))
    conn.commit()
    print("\n video add succes fully")


def update_video(video_id,name,time):
    cursor.execute("UPDATE videos SET name=?, time=? WHERE id =?",(name,time,video_id))
    conn.commit()
    print("\n video update succesfully")

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id=?",(video_id,))
    conn.commit()
    print("\n video delete succes fully")


def main():
    while True:
        print("\n youtube manager app with DB")
        print("\n 1. list video ")
        print('\n 2. add video ')
        print('\n update video')
        print('\n delete video')
        print('\n exit')

        choice=input("enter your choice : ")
        if choice=="1":
            list_video()
        elif choice=="2":
           name= input("enter the video name ")
           time=input("enter  video time ")
           add_video(name,time)
        elif choice=='3':
           vidoe_id= input('enter video id to update ')
           name=input("enter new video name ")
           time=input('enter name video time ')
           update_video(vidoe_id,name,time)
        elif choice=="4":
            vidoe_id=input("enter video id ")
            delete_video(vidoe_id)
        elif choice=="5":
            print("program terminate")
            break
        else:
            print('invalid choice')

    conn.close()


if __name__=="__main__":
    main()