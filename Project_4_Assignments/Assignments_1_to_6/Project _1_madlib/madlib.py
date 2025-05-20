def mad_libs():
    print("Welcome to Mad Libs Game!")
    print("Please provide the following words:\n")

    # Get user input
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb (past tense): ")
    adverb1 = input("Enter an adverb: ")
    adjective2 = input("Enter another adjective: ")
    noun2 = input("Enter another noun: ")
    noun3 = input("Enter one more noun: ")
    verb2 = input("Enter a verb: ")
    adverb2 = input("Enter another adverb: ")

    # Create the story using formatted string
    story = f"""
    Today I went to the zoo. I saw a(n) {adjective1} {noun1} jumping up and down in its tree.
    It {verb1} {adverb1} through the large tunnel that led to its {adjective2} {noun2}.
    I got some peanuts and passed them through the cage to a gigantic {noun3}
    towering above my head. Feeding that animal made me hungry.
    I went to get a {verb2} and ate it {adverb2}.
    """

    # Display the story
    print("\nHere is your Mad Libs story:")
    print(story)

# Run the game
if __name__ == "__main__":
    mad_libs()