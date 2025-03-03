
# 🗳️ Voting Eligibility Check
def check_voting_eligibility(age):
    if age >= 18:
        print("🗳️ You meet the legal voting age requirement! Exercise your right to vote responsibly.")
    else:
        print("🚫 Sorry, you are too young to vote. Stay informed and be ready for future elections.")

# 🎟️ Admission Fee Calculator
def calculate_admission_fee(age):
    if age < 4:
        price = 0
        message = "🎉 Enjoy free admission! Have a great time!"
    elif 4 <= age < 18:
        price = 25
        message = "💰 Your admission fee is $25. Don't forget to grab a snack!"
    else:
        price = 40
        message = "🎟️ Your admission fee is $40. Have an amazing experience!"
    
    print(f"🛎️ Admission Cost: ${price}")
    print(message)

# 📚 Student Grade Evaluation System
def evaluate_student_grade(marks):
    if marks >= 90:
        grade = "A"
        feedback = "🎉 Excellent performance! Keep up the outstanding work!"
    elif 75 <= marks < 90:
        grade = "B"
        feedback = "👍 Well done! A little more effort, and you’ll reach the top!"
    elif 60 <= marks < 75:
        grade = "C"
        feedback = "👌 Good job! Consider revising key concepts to improve further."
    else:
        grade = "F"
        feedback = "📚 You need improvement. Focus on practice and seek help if needed."
    
    print(f"📖 Your Grade: {grade}")
    print(feedback)

# 🎵 Mood-Based Music Recommendation
def recommend_music(mood):
    mood = mood.lower()
    if mood == "happy":
        suggestion = "🎤 How about some upbeat pop music to keep your spirits high?"
    elif mood == "sad":
        suggestion = "🎷 A dose of blues might help you embrace your emotions."
    elif mood == "energetic":
        suggestion = "🎸 Rock music is your perfect companion for that burst of energy!"
    elif mood == "relaxed":
        suggestion = "🎹 Smooth jazz will set the perfect calm vibe."
    else:
        suggestion = "🎧 Discover some new indie tracks and explore fresh sounds!"
    
    print(f"🎼 Mood-Based Recommendation: {suggestion}")

# 🚀 Function Calls with Sample Inputs
if __name__ == "__main__":
    check_voting_eligibility(19)
    check_voting_eligibility(17)

    calculate_admission_fee(12)
    
    evaluate_student_grade(85)
    
    recommend_music("Energetic")
