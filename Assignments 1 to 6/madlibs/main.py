import time
name = input("🤩 Enter your name: ")
superpower = input("⚡ Enter a superpower: ")
animal = input("🐵 Enter a funny animal: ")
place = input("🌍 Enter a place: ")
object = input("🎁 Enter a random object: ")
food = input("🍕 Enter your favorite food: ")
adjective = input("😆 Enter a silly word (e.g., wobbly, stinky): ")
verb = input("💃 Enter a crazy action (e.g., dance, explode): ")

story = f"""
🎭 **The Crazy Adventure of {name}!** 🎭

One day, {name} woke up and screamed, "OMG! I can {superpower}! 🤯"
Excited, {name} ran outside and saw a giant {animal} 🐻 in {place}.

The {animal} was wearing sunglasses 🕶️ and said,
"Hey {name}, if you give me a {object} 🎁, I'll tell you a BIG secret! 🤫"

Without thinking, {name} grabbed a {object} and threw it at the {animal}.
The {animal} took a deep breath and whispered...
"The best superheroes always eat {food} 🍕 before bed!" 😱

That night, {name} ate **10 plates** of {food} 🍽️ and felt super {adjective}!
The next morning, {name} stretched and accidentally {verb} through the roof! 🚀
Now, {name} is the coolest superhero in {place}!

🥳 THE END! 
"""

print("\n✨ Generating your CRAZY story... ✨\n")
time.sleep(2)

print(story)
