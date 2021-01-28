import transcript_gen
import redis
import json

rc = redis.Redis(host="localhost", port=6379, db=0)

def add_users(n):
    startingID = int(rc.hlen("users")) + 1
    if n < 1 or startingID < 1:
        print("n and startingID must be >= 1")
    else:
        for i in range(n):
            user = transcript_gen.randscript(startingID+i)
            rc.hset("users", user["UID"], json.dumps(user))
            uni_college = str(user["Transcript"]["Degree"])
            rc.sadd("colleges", uni_college)
            rc.zadd(uni_college, {user["UID"]: user["Transcript"]["GPA"]})
            rc.geoadd("geos", user["geo_long"], user["geo_lat"], user["UID"])
            print("Added", (i+1), " of ", n, "|", short_info(user), sep=" ")

def get_user(id):
    return json.loads(rc.hget("users", id))

def get_users(ids):
    users = []
    for id in ids:
        users.append(json.loads(rc.hget("users", id)))
    return users

def top_students(college, n):
    return rc.zrange(college, 0, n, desc="true")

def dist_to_users(long, lat, radius):
    id_dists = rc.georadius("geos", long, lat, radius, unit="mi", withdist="true", sort="ASC")
    ids = []
    for idd in id_dists:
        ids.append(idd[0])
        print(short_info(get_user(idd[0])), "- Distance:", idd[1], "miles", sep=" ")
    return ids

def nearby_users(UID, radius):
    id_dists = rc.georadiusbymember("geos", UID, radius, unit="mi", withdist="true", sort="ASC")
    ids = []
    for idd in id_dists:
        ids.append(idd[0])
        print(short_info(get_user(idd[0])), "- Distance:", idd[1], "miles", sep=" ")
    return ids

def short_info(user):
    info = user["first_name"] + " " + user["last_name"] + " (ID:" + str(user["UID"]) + ") - "
    info += user["Transcript"]["Program"] + " (GPA:" + str(user["Transcript"]["GPA"]) + ") "
    info += user["Transcript"]["Grad_Season"] + " " + str(user["Transcript"]["Grad_Year"])
    return info

def full_info(user):
    classes = "\n"
    for c in user["Transcript"]["Classes"]:
        for d in c.values():
            classes += str(d) + " "
        classes += "\n"
    return short_info(user) + classes

def demo1():
    print("Randomly generated user example: ")
    duser = transcript_gen.randscript(10001)
    print(duser)
    print(full_info(duser))

def demo2():
    print("Adding 100 randomly generated users: ")
    add_users(100)

def demo3():
    print("Finding the top 20 students in Economics, Chemistry, and Law: ")
    teusers = get_users(top_students("Economics", 20))
    tcusers = get_users(top_students("Chemistry", 20))
    tlusers = get_users(top_students("Law", 20))
    for u in teusers + tcusers + tlusers:
        print(short_info(u))

def demo4():
    print("Finding all users who live within 3 miles of the top Business student: ")
    teng_id = top_students("Business", 1)[0]
    user_ids = nearby_users(teng_id, 3)
    print(user_ids)

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    #add_users(10000)
    print("Number of users in database: ", rc.hlen("users"))
    #print(full_info(get_user(3000)))
    #demo1()
    #demo2()
    #demo3()
    #demo4()
