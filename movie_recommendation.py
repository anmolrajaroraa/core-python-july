import random

dataset = {
    "sci-fi": ["Star Wars", "Iron Man", "Avatar", "Guardians of the Galaxy", "Wonder Woman", "Hulk"],
    "horror": ["Annabelle", "Grudge", "Insidious", "Nightmare in the Elm Street", "Evil Dead"],
    "adventure": ["Jumanji", "Journey to the Center of Earth", "Harry Potter", "Life of Pie", "Lord of the Rings", "Black Water"],
    "comedy": ["Jumanji", "Fukrey", "Hera Pheri", "Dhamaal", "Thor: Ragnarok"],
    "action": ["Old Guard", "Gangs of Wasseypur", "Extraction", "Infinity War", "Civil War"]
}

user1 = ["Star Wars", "Annabelle", "Grudge", "Jumanji",
         "Journey to the Center of Earth", "Harry Potter"]
user2 = ["Iron Man", "Avatar", "Guardians of the Galaxy", "Evil Dead", "Harry Potter", "Life of Pie",
         "Lord of the Rings", "Dhamaal", "Thor: Ragnarok", "Old Guard", "Gangs of Wasseypur", "Extraction", "Fukrey"]

# find the fav category of user1
# find movies from that category that user2 has already watched
# find out those movies from the fav category that user2 has watched but user1 has not yet
# recommend these movies to user1

personToBeRecommeded = user2
personToBeReferenced = user1

categories = list(dataset.keys())
print("Categories - ", categories)

categoryOfWatchedMoviesCount = dict.fromkeys(categories, 0)

for movie in personToBeRecommeded:
    # print(movie)
    for category in categories:
        # print(category)
        if movie in dataset[category]:
            print(movie, " - ", category)
            categoryOfWatchedMoviesCount[category] += 1

print(categoryOfWatchedMoviesCount)

values = list(categoryOfWatchedMoviesCount.values())  # [2,3,1,3,1]
maxCount = max(values)  # 3
# print(maxCount)
# find index of max value
indexOfFavCategory = values.index(maxCount)  # 1
# find the name of category based on the index
favCategory = categories[indexOfFavCategory]
print("Fav category is ", favCategory)

user2WatchedMoviesInFavCategory = []

for movie in personToBeReferenced:
    if movie in dataset[favCategory]:
        user2WatchedMoviesInFavCategory.append(movie)

print(user2WatchedMoviesInFavCategory)

# find movies that user2 has watched but user1 has not yet
user1NotWatchedMoviesInFavCategory = list(
    set(user2WatchedMoviesInFavCategory) - set(personToBeRecommeded))

print(user1NotWatchedMoviesInFavCategory)

print("Recommended movie is", random.choice(
    user1NotWatchedMoviesInFavCategory))
