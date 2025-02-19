import time
import random
import requests
import logging
import psutil
import os

# Configuration
BASE_URL = "http://prod.shaqapp.io/v1/en/users/reviews/"
DELAYS = (1, 10)
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
]

TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vYXV0aC5zaGFxYXBwLmlvL3YxL2VuL3VzZXJzL2F1dGgvc2lnbi1pbiIsImlhdCI6MTczOTk3NTIxMCwiZXhwIjoxNzM5OTc4ODEwLCJuYmYiOjE3Mzk5NzUyMTAsImp0aSI6ImtHa0p5TG9TdFhpaERYN2YiLCJzdWIiOiIyMjM2OSIsInBydiI6IjM0Y2VjN2VjMjk2NTZmNTRkMjM4ODAzNzAwY2IzZmE2MWE2MzI5OGEiLCJwcml2X3RhYmxlIjoiNWI3ZGNkMTRhNGZhYTJjZGQ1NGNmNmViOGQ0YmMzNWRhMzE5MTRhMSJ9.eqUK8YfnOi5lbezG1deFvIBsHJ6grAakN_0mUE6zse8"

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
        # ... more varied comments
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
        import json
        try:
            json.dumps(payload)  # Try to serialize the payload manually
            print("Payload is JSON-serializable") # If this doesn't throw an error, payload is OK
        except TypeError as e:
            print(f"Payload is NOT JSON-serializable: {e}")
            print("Payload contents:") # Print the contents of the payload to see what's wrong
            print(payload)

            # Inspect the values in the payload:
            for key, value in payload.items():
                print(f"{key}: {type(value)}") # Print the type of each value

            raise # Re-raise the exception after printing information
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
    branch_id = 34
    product_ids = [48, 49, 50, 51, 52] # Example list of product IDs

    for product_id in product_ids:
        review_data = generate_review()
        if submit_review(''''user_id''''', product_id, branch_id, review_data):
            print(f"Review submitted for Product ID: {product_id}")
        else:
            print(f"Failed to submit review for Product ID: {product_id}")

        time.sleep(random.uniform(*DELAYS))

        if product_id % 10 == 0:
            memory_usage()

if __name__ == "__main__":
    main()