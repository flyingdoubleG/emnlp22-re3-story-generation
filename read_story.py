import pickle

with open('output/complete_story5.pkl.temp2', 'rb') as f:
    story = pickle.load(f)

print(story[0].story())