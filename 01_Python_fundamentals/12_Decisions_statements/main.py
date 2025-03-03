# ✅ Voting Eligibility Check
def check_voting_eligibility(age):
    if age >= 18:
        print("✔️ You are eligible to vote! Participate in shaping the future.")
    else:
        print("⛔ You are not old enough to vote yet. Stay informed for upcoming elections.")

# 🎫 Admission Fee Calculator
def calculate_admission_fee(age):
    if age < 4:
        price = 0
        message = "🎈 Free entry! Have a fantastic time!"
    elif 4 <= age < 18:
        price = 25
        message = "💵 Your admission fee is $25. Enjoy your visit!"
    else:
        price = 40
        message = "🎟️ Your admission fee is $40. Hope you have a great experience!"
    
    print(f"💰 Admission Cost: ${price}")
    print(message)

# 📊 Student Grade Evaluation System
def evaluate_student_grade(marks):
    if marks >= 90:
        grade = "A"
        feedback = "🏅 Outstanding performance! Keep up the excellent work!"
    elif 75 <= marks < 90:
        grade = "B"
        feedback = "📈 Good job! Keep pushing for even better results!"
    elif 60 <= marks < 75:
        grade = "C"
        feedback = "📚 Decent effort! A little more practice will make a big difference."
    else:
        grade = "F"
        feedback = "🚀 Keep learning! Focus on key areas to improve."

    print(f"📝 Your Grade: {grade}")
    print(feedback)

# 🎶 Mood-Based Music Recommendation
def recommend_music(mood):
    mood = mood.lower()
    if mood == "happy":
        suggestion = "🎷 Try some lively jazz to keep your mood lifted!"
    elif mood == "sad":
        suggestion = "🎻 Classical music might be a great way to relax."
    elif mood == "energetic":
        suggestion = "🥁 Drum beats and electronic tunes are perfect for your energy!"
    elif mood == "relaxed":
        suggestion = "🎵 Soft acoustic tracks will set a calming atmosphere."
    else:
        suggestion = "🎧 Explore some fresh sounds and new genres!"

    print(f"🎼 Music Suggestion: {suggestion}")

# 🚀 Execute Functions with Sample Inputs
if __name__ == "__main__":
    check_voting_eligibility(19)
    check_voting_eligibility(17)

    calculate_admission_fee(12)
    
    evaluate_student_grade(85)
    
    recommend_music("Energetic")
