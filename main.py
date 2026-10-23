from pyscript import document

def candidate_checker(e):
    club_members = [
        "gible grachenheight", "danji spluffins", "ichentu nikkolas", 
        "vurian willion", "kaytei mallador", "grakbet4 gh4ruiscili", 
        "plaginon destructor", "cadence volition"
    ]
    
    f_name = document.getElementById('fname').value
    l_name = document.getElementById('lname').value
    
    # FIXED: Perfectly indented with no trailing or accidental double-spaces
    candidate = f"{f_name.strip()} {l_name.strip()}"
    
    member_checker = candidate.lower() in club_members
    
    messages = (
        f"Sorry {candidate}, your name is not on the Xarian Aviation Club list. Please leave now.",
        f"Congratulations, {candidate} individual! You are part of the Xarian Aviation Club. Now please drive a rocket to Splork, we need more Yuogliptonium-246."
    )
    
    document.getElementById('result').innerHTML = messages[member_checker]
