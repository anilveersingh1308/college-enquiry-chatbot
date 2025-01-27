import sqlite3

responses = {
    "admissions eligibility": "Eligibility: UG requires 50% in 12th; PG requires a bachelor's degree.",
    "admissions process": "Apply online via our portal. Fill the form, upload documents, and pay the fee.",
    "admissions dates": "Admissions start April 1 and close June 30.",
    "admissions exams": "We accept JEE, CAT, and our entrance exam.",
    "programs undergraduate": "Available programs: B.Tech, B.Sc, BCA, BA.",
    "programs postgraduate": "Available programs: M.Tech, M.Sc, MCA, MA.",
    "programs diploma": "Diplomas in Digital Marketing, Data Science, etc.",
    "programs research": "Research areas include Computer Science, Physics, Management.",
    "fees structure": "Fees: UG starts at $10,000/year; PG starts at $15,000/year.",
    "fees payment": "Pay via Net Banking, Credit/Debit Card, or UPI.",
    "fees scholarships": "Merit-based and need-based scholarships available.",
    "fees refund": "Refunds allowed within 30 days with a 10% deduction.",
    "facilities library": "Library has 50,000+ books and e-resources.",
    "facilities hostel": "Separate hostels for boys and girls with modern amenities.",
    "facilities sports": "Facilities for cricket, football, gym, and more.",
    "facilities transport": "Bus services available across the city.",
    "placements statistics": "95% placement rate. Avg package: $50,000/year.",
    "placements recruiters": "Top recruiters: Google, Amazon, Infosys.",
    "placements internships": "Internships offered with industry leaders.",
    "placements alumni": "Alumni include top industry professionals and entrepreneurs.",
    "contact department": "Email: admissions@college.com; Phone: +123-456-7890.",
    "contact general": "Email: info@college.com; Phone: +123-456-0000.",
    "contact social": "Follow us on Facebook, Twitter, Instagram.",
    "greetings": "Hello! How can I assist you today? You can ask me about admissions, programs, fees, facilities, placements, or contact information.",
    "admissions all": "Eligibility criteria for the programs are : \nUG requires 50% in 12th \nPG requires a bachelor's degree. \nAdmission process is : \n1. Apply online via our portal. \n2. Fill the form, upload documents, and pay the fee. \nAdmissions starts from 1st April and closes on  30th June. \nWe accept JEE, CAT, and our entrance exam.",
    "programs all": "Available undergraduate are : \nB.Tech, B.Sc, BCA, BA, M.Tech, M.Sc, MCA, MA, Diplomas in Digital Marketing, Data Science, etc. Research areas include Computer Science, Physics, Management.",
    "fees all": "Fees structure : \n For UG starts at $10,000/year \nFor PG starts at $15,000/year. \n& Payment can be done via Net Banking, Credit/Debit Card, or UPI. \nMerit-based and need-based scholarships are also available. \nIn case of Refund, allowed within 30 days with a 10% deduction.",
    "placements all": "Placement statistics : \n95% placement rate. Avg package: $50,000/year. \nTop recruiters: Google, Amazon, Infosys. \nInternships offered with industry leaders. \nAlumni include top industry professionals and entrepreneurs.",
    "contact all": "Contact details are : \nEmail: admissions@college.com; Phone: +123-456-7890. \nEmail: info@college.com; Phone: +123-456-0000. \nFollow us on Facebook, Twitter, Instagram.",
    "facilities all": "Library has 50,000+ books and e-resources. Separate hostels for boys and girls with modern amenities. Facilities for cricket, football, gym, and more. Bus services available across the city."
}

def populate_db():
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()
    for key, value in responses.items():
        cursor.execute("INSERT INTO responses (keyword, response) VALUES (?, ?)", (key, value))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    populate_db()
