import time
import random
import requests
import logging
import psutil
import os
from itertools import product  # Generates combinations efficiently

# Configuration
BASE_URL = "https://prod.shaqapp.io/v1/en/users/reviews/"
DELAYS = [1, 10]
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
]

# Logging setup
logging.basicConfig(filename="bot.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def get_random_user_agent():
    """Return a random user-agent string."""
    return random.choice(USER_AGENTS)

def generate_review():
    """Generate random ratings (3-5 stars) and reviews."""
    return {
        "rating": random.randint(3, 5),
        "comments": random.choice([
            "Great product! Highly recommended.",
            "Good quality and value for money.",
            "Satisfied with the purchase.",
            "Excellent product, works perfectly.",
            "Very happy with this product."
        ])
    }

def submit_review(user_id, product_id, branch_id, review_data):
    """Submit a review to the API."""
    headers = {"User-Agent": get_random_user_agent()}
    payload = {
        "user_id": user_id,
        "product_id": product_id,
        "branch_id": branch_id,
        "rating": review_data["rating"],
        "comments": review_data["comments"]
    }

    try:
        response = requests.post(BASE_URL, headers=headers, json=payload)
        if response.status_code == 200:
            logging.info(f"Review submitted successfully for Product ID: {product_id}")
            return True
        else:
            logging.error(f"Failed to submit review for Product ID: {product_id}. Status Code: {response.status_code}")
            return False
    except requests.RequestException as e:
        logging.error(f"Error submitting review for Product ID: {product_id}. Error: {e}")
        return False

def memory_usage():
    """Logs the current memory usage."""
    process = psutil.Process(os.getpid())
    mem_usage = process.memory_info().rss / 1024 / 1024  # Convert to MB
    logging.info(f"Memory usage: {mem_usage:.2f} MB")

def main():
    """Main function to run the bot."""
    # Generate product combinations lazily using `product()` (low memory usage)
    for user_id, product_id, branch_id in product(range(3, 361), range(1, 301), range(1, 261)):
        review_data = generate_review()
        if submit_review(user_id, product_id, branch_id, review_data):
            print(f"Review submitted for Product ID: {product_id}")
        else:
            print(f"Failed to submit review for Product ID: {product_id}")

        # Sleep to avoid rate-limiting
        time.sleep(random.uniform(*DELAYS))

        # Log memory usage every 500 iterations
        if product_id % 500 == 0:
            memory_usage()

if __name__ == "__main__":
    main()
