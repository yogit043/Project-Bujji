import re
import smtplib


def extract_yt_term(command):
    #Define a regular expression pattern to capture the name
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    
    match = re.search(pattern, command,re.IGNORECASE)
    
    return match.group(1) if match else None


def remove_words(input_string , words_to_remove):
    # split the input string into words
    words = input_string.split()
    #remove unwanted words
    filtered_words = [word for word in words if word.lower() not in words_to_remove]
    #join the remaining words back into a string
    result_string = ' '.join(filtered_words)
    return result_string

# Example Usage 
# input_string = "make a phone call to amma"
# words_to_remove = ['make','a','phone','call','to','send','message','whatsapp','can','you','please','',]
# result = remove_words(input_string,words_to_remove)
# print(result)

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("yogit.gani@gmail.com", "Yogit.gani@007")
    server.sendmail("yogit.gani@gmail.com", to, content)
    server.close()