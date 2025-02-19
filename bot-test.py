import requests
import json
import random
import time
import logging

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
]

def get_random_user_agent():
    """Return a random user-agent string."""
    return random.choice(USER_AGENTS)

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vYXV0aC5zaGFxYXBwLmlvL3YxL2VuL3VzZXJzL2F1dGgvc2lnbi1pbiIsImlhdCI6MTczOTk3NTIxMCwiZXhwIjoxNzM5OTc4ODEwLCJuYmYiOjE3Mzk5NzUyMTAsImp0aSI6ImtHa0p5TG9TdFhpaERYN2YiLCJzdWIiOiIyMjM2OSIsInBydiI6IjM0Y2VjN2VjMjk2NTZmNTRkMjM4ODAzNzAwY2IzZmE2MWE2MzI5OGEiLCJwcml2X3RhYmxlIjoiNWI3ZGNkMTRhNGZhYTJjZGQ1NGNmNmViOGQ0YmMzNWRhMzE5MTRhMSJ9.eqUK8YfnOi5lbezG1deFvIBsHJ6grAakN_0mUE6zse8"
headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Accept": "application/json", "Authorization": "Bearer {token}"}

def generate_and_post_reviews(user_id, product_ids, branch_ids, num_reviews=500):
    """Generates and posts reviews, using more varied content.

    Args:
        user_id: The ID of the user posting the reviews.
        product_ids: A list of product IDs.
        branch_ids: A list of branch IDs.
        num_reviews: The number of reviews to generate.

    Returns:
        A list of responses from the API, or None if an error occurs.
    """

    url = "http://prod.shaqapp.io/v1/en/users/reviews/"  # Or the correct endpoint

    responses = []

    token = '''eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vYXV0aC5zaGFxYXBwLmlvL3YxL2VuL3VzZXJzL2F1dGgvc2lnbi1pbiIsImlhdCI6MTczOTk2NjkzNiwiZXhwIjoxNzM5OTcwNTM2LCJuYmYiOjE3Mzk5NjY5MzYsImp0aSI6ImpENVVmMDJPNnA1a3pPMVMiLCJzdWIiOiIxOTk3MSIsInBydiI6IjM0Y2VjN2VjMjk2NTZmNTRkMjM4ODAzNzAwY2IzZmE2MWE2MzI5OGEiLCJwcml2X3RhYmxlIjoiNWI3ZGNkMTRhNGZhYTJjZGQ1NGNmNmViOGQ0YmMzNWRhMzE5MTRhMSJ9.NIARgoFoNQkuSE5pB9qicVwS4SH7Nu1HEQZpPE8NhUU'''


    # Logging setup
    logging.basicConfig(filename="bot1.log", level=logging.INFO, format="%(asctime)s - %(message)s")

    # More diverse and descriptive review templates
    review_templates = [
        {"rating": 5, "comments": "This product exceeded my expectations!  The quality is excellent, and it's exactly what I was looking for. Highly recommend!"},
        {"rating": 4, "comments": "I'm very happy with this purchase. It's well-made and performs as advertised.  A great value for the price."},
        {"rating": 3, "comments": "It's a decent product.  It does the job, but I have a few minor complaints.  Overall, I'm satisfied."},
        {"rating": 2, "comments": "I'm a bit disappointed with this product.  It didn't meet my expectations, and I experienced some issues.  I wouldn't recommend it."},
        {"rating": 1, "comments": "This is the worst product I've ever bought.  It's completely useless and broke after only a few uses.  Don't waste your money."},
        {"rating": 5, "comments": "The service at this branch was outstanding! The staff was friendly and helpful, and they went above and beyond to assist me.  I will definitely be back!"},
        {"rating": 4, "comments": "I had a positive experience at this branch. The service was efficient, and the staff was knowledgeable.  I would recommend it."},
        {"rating": 3, "comments": "The service was okay. It wasn't exceptional, but it wasn't bad either.  Just an average experience."},
        {"rating": 2, "comments": "I was not impressed with the service at this branch.  The staff was unhelpful, and I had to wait a long time.  I wouldn't go back."},
        {"rating": 1, "comments": "The service at this branch was absolutely terrible.  The staff was rude and unprofessional.  I would never recommend this place."},
        {"rating": 5, "comments": "Shaq's is my go-to place! The food is always delicious, and the service is top-notch. I highly recommend the [mention a specific item]."},
        {"rating": 4, "comments": "I enjoy eating at Shaq's. The food is good, and the prices are reasonable.  A great option for a casual meal."},
        {"rating": 3, "comments": "Shaq's is okay. The food is decent, but nothing special.  It's a convenient option if you're in the area."},
        {"rating": 2, "comments": "I've had better meals at other places. The food at Shaq's is average, and the service can be slow at times."},
        {"rating": 1, "comments": "I was very disappointed with my meal at Shaq's. The food was cold and tasteless, and the service was poor. I wouldn't go back."},
         # ... Add many more templates!  The more diverse, the better.
    ]


    for i in range(num_reviews):
        review_data = random.choice(review_templates)
        product_id = random.choice(product_ids)
        branch_id = random.choice(branch_ids)

        payload = {
            "user_id": user_id,
            "product_id": product_id,
            "branch_id": branch_id,
            "rating": review_data["rating"],
            "comments": review_data["comments"]
        }

        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            responses.append(response)

            if response.status_code == 200:
                print(f"Review {i+1} posted successfully!")
                logging.info(f"Review {i+1} posted successfully!")
            else:
                print(f"Error posting review {i+1}: {response.status_code} - {response.text}")
                logging.error(f"Error posting review {i+1}: {response.status_code} - {response.text}")
                # Optional: break  # Uncomment to stop on the first error

            time.sleep(0.2)  # Rate limiting (adjust as needed)

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    return responses

# Example usage (replace with your actual data):
user_id_to_post = "6"
product_ids_list = ["300"]
branch_ids_list = ["60"]

all_responses = generate_and_post_reviews(user_id_to_post, product_ids_list, branch_ids_list)

if all_responses:
    print(f"Finished posting {len(all_responses)} reviews.")
    logging.info(f"Finished posting {len(all_responses)} reviews.")
else:
    print("Review posting failed.")
    logging.error("Review posting failed.")