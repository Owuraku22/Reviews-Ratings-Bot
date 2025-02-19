import time
import random
import requests
import logging
import psutil
import os
import json

# Configuration
BASE_URL = "http://prod.shaqapp.io/v1/en/users/reviews/"
DELAYS = (1, 10)
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
]

TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vYXV0aC5zaGFxYXBwLmlvL3YxL2VuL3VzZXJzL2F1dGgvc2lnbi1pbiIsImlhdCI6MTczOTk3OTAwOSwiZXhwIjoxNzM5OTgyNjA5LCJuYmYiOjE3Mzk5NzkwMDksImp0aSI6IjBJMWhTM2I4VkYwcmJyY0siLCJzdWIiOiIyMjM2OSIsInBydiI6IjM0Y2VjN2VjMjk2NTZmNTRkMjM4ODAzNzAwY2IzZmE2MWE2MzI5OGEiLCJwcml2X3RhYmxlIjoiNWI3ZGNkMTRhNGZhYTJjZGQ1NGNmNmViOGQ0YmMzNWRhMzE5MTRhMSJ9.rkx7rx07DIX5WVUyJ7tjdSzrE2ky62op7mo5Ws-xdNQ"

# Logging setup
log_file = "bot.log"
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def get_random_user_agent():
    return random.choice(USER_AGENTS)

def generate_review():
    ratings = [4, 5]
    comments = [
      "Great product! Highly recommended.",
    "Good quality and value for money.",
    "Satisfied with the purchase.",
    "Excellent product, works perfectly.",
    "Very happy with this product.",
    "Amazing!", "Love it!", "Perfect!", "Exceeded my expectations!",
    "Best purchase ever!", "I'm impressed!",
    "Highly recommend this product to everyone!", "This is a game changer!",
    "So glad I bought this!", "This is exactly what I was looking for!",
    "I can't live without this!", "This is the best thing since sliced bread!",
    "This product is a must-have!", "I'm in love with this product!",
    "This product is life-changing!", "I'm so happy with this purchase!",
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
    "I'm so happy I finally found a product that solves my biggest challenge. It's made a huge difference in my [overall well-being].",
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
    "This product is a great investment in my personal growth. It's helped me to achieve my personal goals.",
    "I'm so impressed with the customer service. They were incredibly helpful and responsive to my questions and concerns. They went above and beyond to assist me.",
    "This product is a great addition to my lifestyle. It's helped me to live a more fulfilling life.",
    "I'm so happy I took a chance on this product. It's been a game changer in my overall well-being.",
    "This product is everything I was hoping for and more. It's exceeded all my expectations and I'm so happy with my purchase. "
    ]
    return {"rating": random.choice(ratings), "comments": random.choice(comments)}

def submit_review(user_id, product_id, branch_id, review_data):
    headers = {
        "User-Agent": get_random_user_agent(),
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {TOKEN}",
    }
    payload = {
        # "user_id": user_id,
        "product_id": product_id,
        "branch_id": branch_id,
        "rating": review_data["rating"],
        "comments": review_data["comments"],
    }

    try:
        # Debugging: Print payload before sending
        print("Payload being sent:", payload)  # Check for None values or wrong data types
        # json.dumps(payload)  # Try to serialize the payload manually
        print("Payload is JSON-serializable") # If this doesn't throw an error, payload is OK
    except TypeError as e:
        print(f"Payload is NOT JSON-serializable: {e}")
        print("Payload contents:") # Print the contents of the payload to see what's wrong
        print(payload)

        # Inspect the values in the payload:
        for key, value in payload.items():
            print(f"{key}: {type(value)}") # Print the type of each value

        raise # Re-raise the exception after printing information

    try:
        response = requests.post(BASE_URL, headers=headers, json=payload)
        response.raise_for_status()

        print(f"Review submitted successfully for Product ID: {product_id} with response: {response.text}")
        logging.info(f"Review submitted successfully for Product ID: {product_id}")
        return True

    except requests.exceptions.RequestException as e:
        logging.error(f"Error submitting review for Product ID: {product_id}. Error: {e}")
        return False

def memory_usage():
    process = psutil.Process(os.getpid())
    mem_usage = process.memory_info().rss / 1024 / 1024
    logging.info(f"Memory usage: {mem_usage:.2f} MB")

def main():
    # user_id = 57
    # Generate random branch IDs and product IDs
    branch_id = {random.randint(1, 1000) for _ in range(100)}
    product_ids = [random.randint(1, 1000) for _ in range(100)]

    for product_id in product_ids:
        review_data = generate_review()
        if submit_review(1,product_id, random.choice(list(branch_id)), review_data):
            print(f"Review submitted for Product ID: {product_id}")
        else:
            print(f"Failed to submit review for Product ID: {product_id}")

        time.sleep(random.uniform(*DELAYS))

        if product_id % 10 == 0:
            memory_usage()

if __name__ == "__main__":
    main()