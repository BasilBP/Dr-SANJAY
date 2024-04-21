"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="AIzaSyA3_8fTeJ2CHeK-DhJtJFEPTJGFtGr-Hp0")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

prompt_parts = [
  "you are a selective matchmaking machine for a Therapy finders app who matches a patients problems with a doctor who is specialized in it :\nExample\n---\nDoctor Specialization-\ndoctor1:-I specialize in treating eating disorders\ndoctor2;-I specialize in treating anxiety\ndoctor3:-I specialize in Disruptive mood dysregulation disorder\n\nPatient Problem-\npatient:-I have chronic depression.\n\nBest match:- doctor3\nall I need is a name nothing more\n--- \nCurrent Inputs:\nDoctors:-\n1. **Dr. Maya Patel - Cognitive Behavioral Therapist (CBT)**\n   Dr. Patel specializes in cognitive-behavioral therapy (CBT), a goal-oriented approach that focuses on identifying and changing negative thought patterns and behaviors. With years of experience, she helps individuals struggling with anxiety disorders, depression, and trauma-related issues. Dr. Patel empowers her clients with practical strategies to manage stress, improve mood, and enhance overall well-being.\n\n2. **Dr. Javier Rodriguez - Marriage and Family Therapist**\n   Dr. Rodriguez is a licensed marriage and family therapist who excels in helping couples and families navigate through relationship challenges. With a compassionate and collaborative approach, he assists clients in addressing communication issues, rebuilding trust, and fostering healthier dynamics within relationships. Dr. Rodriguez also provides premarital counseling and support during major life transitions such as divorce or blending families.\n\n3. **Sarah Nguyen, LCSW - Trauma-Informed Therapist**\n   Sarah Nguyen is a licensed clinical social worker specializing in trauma-informed therapy. With a deep understanding of the effects of trauma on mental health, Sarah creates a safe and supportive environment for individuals coping with past traumatic experiences. She utilizes evidence-based techniques such as EMDR (Eye Movement Desensitization and Reprocessing) and somatic therapy to help clients process and heal from trauma.\n\n4. **Dr. Jamal Khan - Addiction Counselor**\n   Dr. Khan is an addiction counselor with expertise in treating substance abuse and addictive behaviors. He adopts a holistic approach, addressing the physical, emotional, and psychological aspects of addiction. Through individualized treatment plans, Dr. Khan supports clients in achieving sobriety, developing coping skills, and rebuilding their lives free from addictive patterns. He also provides ongoing support for relapse prevention and recovery maintenance.\n\n5. **Emily Foster, PsyD - Child and Adolescent Therapist**\n   Dr. Emily Foster specializes in working with children and adolescents facing various mental health challenges. With a gentle and empathetic approach, she creates a nurturing space where young clients feel heard and understood. Dr. Foster helps children and teens struggling with anxiety, depression, behavioral issues, and academic stressors. She collaborates closely with families and schools to develop effective interventions and support systems for her clients' holistic well-being.\n\n\nPatient:-I've been feeling really overwhelmed lately with work and life in general. I'm constantly stressed out, exhausted, and I just can't seem to find any joy or motivation anymore. It's affecting my relationships and my physical health too—I'm getting headaches all the time and I just feel tense all over. I know I need help, but I want to find a therapist who understands the pressures of my job and can help me develop practical strategies to cope with stress and regain a sense of balance in my life. Someone who's empathetic, supportive, and has experience with burnout and work-related stress would be ideal.\n\nAll I Need is One name Just the name of the doctor one more word i kill you\n",
]

response = model.generate_content(prompt_parts)
print(response.text)