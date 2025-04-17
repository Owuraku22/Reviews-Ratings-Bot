import json
import random
import os


def generate_reviews_json(num_reviews=55, output_dir="home/Downloads", filename="shop_online.json"):
    """Generates review data and saves it to a JSON file.

    Args:
        num_reviews: The number of reviews to generate.
        output_file: The name of the JSON file to save to.
    """

    reviews = []
    for _ in range(num_reviews):
        review = {
            "user_id": None,  # Nullable user_id
            "branch_id": random.randint(1, 1000),  
            "product_id": random.randint(1, 1000),  
            "rating": random.randint(4, 5),  # Ratings from 1 to 5
            "comments": random.choice([  # Example comments - add more!
               "Great value for the price."
                "No complaints."
                "Pretty decent overall — would buy again."
                "Satisfied with the quality and performance."
                "Item arrived in good condition and on time."
                "Nothing extraordinary"
                "Solid product — meets my expectations."
                "Good packaging and fast delivery."
                "No major issues so far."
                "Reliable"
                "Fairly priced for what you get."
                "Decent, would recommend."
                "Not bad at all."
                "Fast Delivery."
                "It matches the description."
                "Great choice, highly recommend!",
                "Perfect addition to my order!",
                "So pleased",
                "A fantastic find online!",
                "Love how great this is!",
                "Definitely worth ordering!",
                "Super happy with this order",
                "A great pick every time!",
            ]),
        }
        reviews.append(review)
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    # Save to JSON file
    output_path = os.path.join(output_dir, filename)
    with open(output_path, "w") as f:
        json.dump(reviews, f, indent=4)
    print(f"Generated {num_reviews} reviews and saved to {output_path}")
