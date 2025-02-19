import json
import random
import os


def generate_reviews_json(num_reviews=500, output_dir="home/african-god/Downloads", filename="reviews.json"):
    """Generates review data and saves it to a JSON file.

    Args:
        num_reviews: The number of reviews to generate.
        output_file: The name of the JSON file to save to.
    """

    reviews = []
    for _ in range(num_reviews):
        review = {
            "user_id": None,  # Nullable user_id
            "branch_id": random.randint(1, 1000),  # Replace with your actual branch ID range
            "product_id": random.randint(1, 1000),  # Replace with your actual product ID range
            "rating": random.randint(1, 5),  # Ratings from 1 to 5
            "comments": random.choice([  # Example comments - add more!
                "Great product!",
                "Good value.",
                "Excellent service.",
                "I'm satisfied.",
                "Highly recommend.",
                "Amazing!",
                "Love it!",
                "Perfect!",
                "Exceeded my expectations!",
                "Best purchase ever!",
                "I'm impressed!",
                "Highly recommend this product to everyone!",
                "This is a game changer!",
                "So glad I bought this!",
                "This is exactly what I was looking for!",
                "I can't live without this!",
                "This is the best thing since sliced bread!",
                "This product is a must-have!",
                "I'm in love with this product!",
                "This product is life-changing!",
                "I'm so happy with this purchase!",
                "This product is amazing and I would recommend it to anyone!",
                "This product is great and I would definitely buy it again!",
                "This product is fantastic and I would recommend it to a friend!",
                "This product is awesome and I would recommend it to a family member!",
                "This product is wonderful and I would recommend it to a colleague!",
                "This product is superb and I would recommend it to a client!",
                "This product is amazing! It's exactly what I needed.",
                "I'm so impressed with the quality of this product.",
                "This product is a great value for the price.",
                "I'm very satisfied with my purchase. It arrived quickly and in perfect condition.",
                "This product is so easy to use and it works great!",
                "I'm so happy I found this product! It's made my life so much easier.",
                "This product is a must-have for anyone who needs a reliable and efficient solution.",
                "I highly recommend this product to anyone looking for a high-quality and affordable option.",
                "This product is worth every penny!",
                "I'm so glad I decided to buy this product. It's exceeded all my expectations.",
                "This product is perfect for [daily use].",
                "I'm so happy with the results I've gotten from using this product.",
                "This product is a great investment.",
                "I'm so impressed with the customer service. They were very helpful and responsive.",
                "This product is a great addition to my [home office].",
                "I'm so happy I took a chance on this product. It's been a game changer.",
                "This product is everything I was hoping for and more.",
                "I'm so impressed with the attention to detail in this product.",
                "This product is a great way to save time.",
                "I'm so happy I finally found a product that solves my biggest problem.",
                "This product is so much better than anything else I've tried.",
                "I'm so glad I upgraded to this product. It's been a huge improvement.",
                "This product is a great gift for anyone who appreciates quality and value.",
                "I'm so happy I can finally accomplish my goals.",
                "This product is a great way to improve my life.",
                "I'm so impressed with the innovation in this product.",
                "This product is a great example of excellent design.",
                "I'm so happy I chose this product over the competition.",
                "This product is a great value for the price. I highly recommend it.",
                "I'm very satisfied with this purchase. The product is exactly as described and works perfectly.",
                "This product is amazing! It's so easy to use and the results are fantastic.",
                "I'm so glad I bought this product. It's made my life so much easier and more enjoyable.",
                "This product is a must-have for anyone who wants to simplify their routine.",
                "I highly recommend this product to anyone looking for a reliable and high-quality solution.",
                "This product is worth every penny! It's a great investment that I'll be using for years to come.",
                "I'm so happy I decided to buy this product. It's exceeded all my expectations and I couldn't be happier with my purchase.",
                "This product is perfect for specific tasks. It's exactly what I needed and I'm so glad I found it.",
                "I'm so happy with the results I've gotten from using this product. It's helped me to [become more efficient].",
                "This product is a great investment in my [future]. It's helped me to [achieve my goals].",
                "I'm so impressed with the customer service. They were incredibly helpful and responsive to my questions and concerns.",
                "This product is a great addition to my workspace. It's helped me to be more productive.",
                "I'm so happy I took a chance on this product. It's been a game changer in my daily life.",
                "This product is everything I was hoping for and more. It's exceeded all my expectations and I'm so happy with my purchase.",
                "I'm so impressed with the attention to detail in this product. It's clear that a lot of thought and care went into its design and development.",
                "This product is a great way to save time and money. It's helped me to streamline my processes.",
                "I'm so happy I finally found a product that solves my biggest challenge. It's made a huge difference in my overall well-being.",
                "This product is so much better than anything else on the market. It's more reliable and user-friendly",
                "I'm so glad I upgraded to this product. It's been a huge improvement over my old one and I'm so happy with the results.",
                "This product is a great gift for anyone who values quality and innovation It's something they'll use and appreciate for a long time.",
                "I'm so happy I can finally focus on what matters most This product has made it possible and I'm so grateful.",
                "This product is a great way to achieve my long-term goals It's helped me to [make significant progress.",
                "I'm so impressed with the innovation in this product. It's clear that the creators are passionate about making a difference",
                "This product is a great example of quality craftsmanship. It's a testament to the brand's commitment to excellence.",
                "I'm so happy I chose this product over the competition. It's the best solution I've ever used and I'm so happy with my decision.",
                "This product is a great value for the price. I highly recommend it to anyone looking for a product that's effective and affordable.",
                "I'm very satisfied with this purchase. The product is exactly as described and works perfectly. I would definitely buy it again.",
                "This product is amazing! It's so easy to use and the results are fantastic. I'm so happy with my purchase.",
                "I'm so glad I bought this product. It's made my life so much easier and more enjoyable. I highly recommend it to others.",
                "This product is a must-have for anyone who wants to simplify their life. It's a great investment that will pay off in the long run.",
                "I highly recommend this product to anyone looking for a reliable and high-quality product. It's a great value for the price and I'm very happy with my purchase.",
                "This product is worth every penny! It's a great investment that I'll be using for years to come. I'm so happy with its performance and durability.",
                "I'm so happy I decided to buy this product. It's exceeded all my expectations and I couldn't be happier with my purchase. I highly recommend it to anyone looking for a effective solution.",
                "This product is perfect for [everyday use]. It's exactly what I needed and I'm so glad I found it. It's made a huge difference in my daily routine.",
                "I'm so happy with the results I've gotten from using this product. It's helped me to improve my efficiency. I'm so grateful for its ease of use.",
                "This product is a great investment"

            ]),
        }
        reviews.append(review)
