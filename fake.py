#import the random module
import random
#creating subjects, actions and places
subjects = [
    "Shah Rukh Khan",
    "Virat Kohli",
    "Salman Khan",
    "Cristiano Ronaldo",
    "Mamata Banerjee",
    "Raju Dar Rocket Porota",
    "Elon Musk",
    "Modiji",
    "Sunny Leone",
    "Ranveer Singh",
    "Batman",
    "Doraemon",
    "Nobita",
    "Sasuke Uchiha",
    "Amit Shah",
    "Kanye West",
    "Messi",
    "Chhota Bheem",
    "Tarak Mehta",
    "Babu Rao from Hera Pheri",
    "Bob the Builder",
    "Tinder Auntie",
    "T-Series CEO",
    "Goku",
    "Tarak Mehta ka Ulta Chashma"
]


actions = [
    "cooks biryani in",
    "launches a rocket from",
    "eats 200 eggs in",
    "runs a marathon through",
    "slaps a goat in",
    "declares war on",
    "rides a unicorn in",
    "orders pizza from",
    "starts a new political party in",
    "buys 200 cows from",
    "sings karaoke in",
    "opens a gym in",
    "does 1000 pushups in",
    "buys Twitter again in",
    "starts dancing in",
    "turns invisible in",
    "launches an AI startup from",
    "teaches tabla in",
    "proposes marriage in",
    "eats jhalmuri in",
    "gets arrested in",
    "wins a lottery in",
    "challenges everyone to a rap battle in",
    "becomes a monk in",
    "buys all the chai in"
]


places = [
    "Kolkata",
    "Delhi",
    "Nadia",
    "Pasher Bari",
    "Dubai",
    "a swimming pool",
    "Mars",
    "Andromeda Galaxy",
    "Rajabazar",
    "a haunted mansion",
    "the Parliament",
    "Shonar Bangla",
    "Mumbai local train",
    "Tinder HQ",
    "the Moon",
    "Antarctica",
    "Khidirpur",
    "Chandni Chowk",
    "the Ganges",
    "Hogwarts",
    "Gariahat",
    "South City Mall",
    "inside a tea stall",
    "Sundarbans",
    "inside a Zoom call",
    "ED Office",
    "inside a dosa"
]

#making the logic
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)
    
    
    headline  = f"BREAKING NEWS: {subject} {action} {place}" 
    print ("\n" + headline)
    
    userinput = input("\n Do u wanna continue with another headline? (yes/no)").strip().lower()
    if userinput == "no":
        break
#if use chooses no then it will print this
print("\n tysm for using our app")