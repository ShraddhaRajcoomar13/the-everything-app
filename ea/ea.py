import random
import time
from datetime import datetime, timedelta

# Mock APIs (replace with real APIs)
def process_payment(amount: float, user_id: str) -> bool:
    """Simulate a payment processing API."""
    print(f"Processing payment of ${amount:.2f} for user {user_id}.")
    return random.choice([True, False])

def fetch_room_service_directory(location: str) -> list:
    """Simulate fetching a room service directory for the user's location."""
    return ["Restaurant A - +123456789", "Spa B - +987654321", "Laundry C - +192837465"]

def fetch_attractions(location: str) -> list:
    """Simulate fetching local attractions."""
    return ["Museum of Art", "City Park", "Historic Landmark"]

def fetch_videos_and_stories(attraction: str) -> dict:
    """Simulate fetching video links and stories for an attraction."""
    return {"videos": [f"https://videos.com/{attraction.replace(' ', '_')}"], "stories": [f"Amazing tale about {attraction}."]}

# User data
class User:
    def __init__(self, user_id: str, location: str):
        self.user_id = user_id
        self.location = location
        self.usage_log = []
        self.balance = 0.0
        self.load_shedding = False

    def log_usage(self, activity: str):
        self.usage_log.append({"activity": activity, "time": datetime.now()})
        # Trigger load shedding if usage exceeds limits
        if len(self.usage_log) > 10 and (datetime.now() - self.usage_log[-10]["time"]).seconds < 600:
            self.load_shedding = True

    def reset_load_shedding(self):
        self.load_shedding = False

# Core Game Logic
def game_prompt(user: User):
    print("\nWelcome to the Digital Vacation Game!")
    print("Earn rewards, explore attractions, and automate your tasks.")
    print("Beware of virtual load shedding based on your usage patterns!")
    while True:
        if user.load_shedding:
            print("\n⚠️ Load Shedding Activated! Please wait...")
            time.sleep(random.randint(10, 30))
            user.reset_load_shedding()
            print("Load Shedding Over. You may continue.")

        print("\nMenu:")
        print("1. Bet to win a vacation!")
        print("2. Explore room service options.")
        print("3. Discover local attractions.")
        print("4. Automate tasks (Daily Challenge).")
        print("5. Exit.")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount to bet (min $10): "))
            if amount < 10:
                print("Minimum bet is $10.")
            elif process_payment(amount, user.user_id):
                user.balance += amount * 2
                print(f"🎉 You won! Your new balance is ${user.balance:.2f}.")
            else:
                print("💔 You lost the bet. Better luck next time!")
            user.log_usage("Bet to win vacation")

        elif choice == "2":
            services = fetch_room_service_directory(user.location)
            print("\nRoom Service Options:")
            for service in services:
                print(f"- {service}")
            user.log_usage("Room service")

        elif choice == "3":
            attractions = fetch_attractions(user.location)
            print("\nLocal Attractions:")
            for attraction in attractions:
                print(f"- {attraction}")
            choice = input("Want details about an attraction? Enter name or 'no': ")
            if choice.lower() != "no" and choice in attractions:
                details = fetch_videos_and_stories(choice)
                print("\nDetails:")
                print(f"Videos: {details['videos']}")
                print(f"Stories: {details['stories']}")
            user.log_usage("Explore attractions")

        elif choice == "4":
            print("\n🎮 Daily Challenge: Complete a puzzle to automate a task!")
            task = input("Enter a mundane task you'd like automated: ")
            print(f"Congratulations! Your task '{task}' has been automated.")
            user.log_usage("Automate task")

        elif choice == "5":
            print("Thanks for playing! Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

# Main Program
if __name__ == "__main__":
    user_id = input("Enter your User ID: ")
    location = input("Enter your current location: ")
    user = User(user_id=user_id, location=location)
    game_prompt(user)
