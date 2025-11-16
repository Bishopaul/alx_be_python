wh_cond = input("What's the weather like today? (sunny/rainy/cold): ").lower()
if wh_cond == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif wh_cond == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif wh_cond == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
