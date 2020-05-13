def getPet(activityLevel, time, size):
    if activityLevel.lower() == "low":
        if time.lower() == "low":
            if size.lower() == "small":
                #return "{"pet": "goldfish", "img_url": "/static/images/goldfish.jpg"}"
                return "goldfish"
            if size.lower() == "medium":
                return "turtle"
            if size.lower() == "large":
                return "bull mastiff"
        if time.lower() == "medium":
            if size.lower() == "small":
                return "lizard"
            if size.lower() == "medium":
                return "snake"
            if size.lower() == "large":
                return "horse"
        if time.lower() == "high":
            if size.lower() == "small":
                return "chihuahua"
            if size.lower() == "medium":
                return "chow chow"
            if size.lower() == "large":
                return "shih tzu"

    if activityLevel.lower() == "medium":
        if time.lower() == "low":
            if size.lower() == "small":
                return "hamster"
            if size.lower() == "medium":
                return "cat"
            if size.lower() == "large":
                return "cow"
        if time.lower() == "medium":
            if size.lower() == "small":
                return "bulldog"
            if size.lower() == "medium":
                return "tortoise"
            if size.lower() == "large":
                return "pig"
        if time.lower() == "high":
            if size.lower() == "small":
                return "rabbit"
            if size.lower() == "medium":
                return "chicken"
            if size.lower() == "large":
                return "sheep"

    if activityLevel.lower() == "high":
        if time.lower() == "low":
            if size.lower() == "small":
                return "ferret"
            if size.lower() == "medium":
                return "koala"
            if size.lower() == "large":
                return "chimpanzee"
        if time.lower() == "medium":
            if size.lower() == "small":
                return "parrot"
            if size.lower() == "medium":
                return "duck"
            if size.lower() == "large":
                return "otter"
        if time.lower() == "high":
            if size.lower() == "small":
                return "boston terrier"
            if size.lower() == "medium":
                return "cockerspaniel!"
            if size.lower() == "large":
                return "golden retriever!"

def getPetPic(activityLevel, time, size):
    if activityLevel.lower() == "low":
        if time.lower() == "low":
            if size.lower() == "small":
                return "/static/images/goldfish.jpg"
            if size.lower() == "medium":
                return "/static/images/turtlescanma.jpg"
    pass