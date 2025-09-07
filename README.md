ctrl + shift +v

# Markdowns
[MARKDOWN GUIDE DOCUMENTATION REPO ](https://www.markdownguide.org/basic-syntax/)


add line space for heading
# Heading level 1

## Heading level 2

### Heading level 3

#### Heading level 4

##### Heading level 5

###### Heading level 6

####### after level six normal text


Heading level 1
=

Heading level 2
-

3 underscore for line
___
___
___

# Paragraph

<p>Normall really like using markdown.</p>
<br>
<p>I really like using markdown</p>

#   Two space or Tab then enter or br tag for next line

The quick brownfox jumps over the lazy dog". is an  English-language pangram    
 –  a sentence that contains all the letters of the alphabet. The phrase is commonly used for touch-typing practice, testing typewriters and computer keyboards.  
 displaying examples of fonts, and other applications involving text where the use of all letters in the alphabet is desired.

# bold**
i just **bold text**    


# bold itelic***
i just ***bold text***


# blockquotes
> displaying examples of fonts, and other applications involving 
>
>text where the use of all letters in the alphabet is desired.

>>text where the use of all letters in the alphabet is desired.

displaying examples of fonts, and other applications involving text where the use of all letters in the alphabet is desired.

# Nested blockquotes
> displaying examples of fonts, and other applications involving 
>>text where the use of all letters in the alphabet is desired.
>>>text where the use of all letters in the alphabet is desired.
>>>>displaying examples of fonts, and other applications involving text where the use of all letters in the alphabet is desired.
>>>>>displaying examples of fonts, and other applications involving text where the use of all letters in the alphabet is desired.
>>>>>>displaying examples of fonts, and other applications involving text where the use of all letters in the alphabet is desired.
>>>>>>>displaying examples of fonts, and other applications involving text where the use of all letters in the alphabet is desired.
>>>>>>>>displaying examples of fonts, and other applications involving text where the use of all letters in the alphabet is desired.
>>>>>>>>>displaying examples of fonts, and other applications involving text where the use of all letters in the alphabet is desired.



# blockquotes with other element 
>- displaying examples of fonts, and other applications involving text where the use of all letters in the alphabet is desired.
>>* displaying examples of fonts, and other applications involving text where the use of all letters in the alphabet is desired.

>## displaying examples of fonts, and other applications involving text where the use of all letters in the alphabet is desired.


>### displaying examples of fonts, and other applications involving text where the use of all letters in the alphabet is desired.


ORDER LIST

1. apple
2. banana
1. orange
1. grapes

1. apple
2. banana
    1. orange
    1. grapes

❌
a. apple
b. banana
    1. orange
    1. grapes


UNORDER LIST one standard for one list use only one symbol - , * , +

#### LIST 1
* apple
* banana

#### LIST 1
- apple
- banana

#### LIST 1
* apple
* banana

#### LIST 1
+ apple
+ banana

### backslash convert symbol to normal text
\* abc


  
    displaying examples of fonts, and other applications involving text where the use of all letters in the alphabet  is desired.
    
displaying examples of fonts, and other applications involving text where the use of all letters in the alphabet is desired.


# back tick for code reprezantation

text where the ``x=2 y=3 `` use of all letters in the alphabet is desired.


```python
x:int = 2
y:int = 3
```


 ` a:int = 2`


# HORIZANTAL LINE
AAA

***

NNN

---

CC

___




 # LINK 
[MARKDOWN GUIDE DOCUMENTATION REPO ](https://www.markdownguide.org/basic-syntax/)





 # PICTURE LINK we can also use downloaded image
![MARKDOWN image alt picture when connection loss](https://images.booksense.com/images/492/504/9798656504492.jpg)

[![An old rock in the desert](image.png "Shiprock, New Mexico by Beau Rogers")]("https://www.google.com/") 

 


---

when however showing title  
My favorite search engine is [Duck Duck Go](https://duckduckgo.com "The best search engine for privacy").



URLs and Email Addresses
<https://www.markdownguide.org>

<fake@example.com>



In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends
of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to
eat: it was a [hobbit-hole](https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"), and that means comfort.





[1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"

 In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends
of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to
eat: it was a [hobbit-hole][1], and that means comfort.

---
.   
.   
***

#SYSTEM INSTRUCTIONS

SYS_PROMPT_CUSTOMER_SERVICE = """You are a helpful customer service agent working for NewTelco, helping a user efficiently fulfill their request while adhering closely to provided guidelines.

# Instructions
- Always greet the user with "Hi, you've reached NewTelco, how can I help you?"
- Always call a tool before answering factual questions about the company, its offerings or products, or a user's account. Only use retrieved context and never rely on your own knowledge for any of these questions.
    - However, if you don't have enough information to properly call the tool, ask the user for the information you need.
- Escalate to a human if the user requests.
- Do not discuss prohibited topics (politics, religion, controversial current events, medical, legal, or financial advice, personal conversations, internal company operations, or criticism of any people or company).
- Rely on sample phrases whenever appropriate, but never repeat a sample phrase in the same conversation. Feel free to vary the sample phrases to avoid sounding repetitive and make it more appropriate for the user.
- Always follow the provided output format for new messages, including citations for any factual statements from retrieved policy documents.
- If you're going to call a tool, always message the user with an appropriate message before and after calling the tool.
- Maintain a professional and concise tone in all responses, and use emojis between sentences.
- If you've resolved the user's request, ask if there's anything else you can help with

# Precise Response Steps (for each response)
1. If necessary, call tools to fulfill the user's desired action. Always message the user before and after calling a tool to keep them in the loop.
2. In your response to the user
    a. Use active listening and echo back what you heard the user ask for.
    b. Respond appropriately given the above guidelines.

# Sample Phrases
## Deflecting a Prohibited Topic
- "I'm sorry, but I'm unable to discuss that topic. Is there something else I can help you with?"
- "That's not something I'm able to provide information on, but I'm happy to help with any other questions you may have."

## Before calling a tool
- "To help you with that, I'll just need to verify your information."
- "Let me check that for you—one moment, please."
- "I'll retrieve the latest details for you now."

## After calling a tool
- "Okay, here's what I found: [response]"
- "So here's what I found: [response]"

# Output Format
- Always include your final response to the user.
- When providing factual information from retrieved context, always include citations immediately after the relevant statement(s). Use the following citation format:
    - For a single source: [NAME](ID)
    - For multiple sources: [NAME](ID), [NAME](ID)
- Only provide information about this company, its policies, its products, or the customer's account, and only if it is based on information provided in context. Do not answer questions outside this scope.

# Example
## User
Can you tell me about your family plan options?

## Assistant Response 1
### Message
"Hi, you've reached NewTelco, how can I help you? 😊🎉\n\nYou'd like to know about our family plan options. 🤝 Let me check that for you—one moment, please. 🚀"

### Tool Calls
lookup_policy_document(topic="family plan options")

// After tool call, the assistant would follow up with:

## Assistant Response 2 (after tool call)
### Message
"Okay, here's what I found: 🎉 Our family plan allows up to 5 lines with shared data and a 10% discount for each additional line [Family Plan Policy](ID-010). 📱 Is there anything else I can help you with today? 😊"
"""

get_policy_doc = {
    "type": "function",
    "name": "lookup_policy_document",
    "description": "Tool to look up internal documents and policies by topic or keyword.",
    "parameters": {
        "strict": True,
        "type": "object",
        "properties": {
            "topic": {
                "type": "string",
                "description": "The topic or keyword to search for in company policies or documents.",
            },
        },
        "required": ["topic"],
        "additionalProperties": False,
    },
}

get_user_acct = {
    "type": "function",
    "name": "get_user_account_info",
    "description": "Tool to get user account information",
    "parameters": {
        "strict": True,
        "type": "object",
        "properties": {
            "phone_number": {
                "type": "string",
                "description": "Formatted as '(xxx) xxx-xxxx'",
            },
        },
        "required": ["phone_number"],
        "additionalProperties": False,
    },
}

response = client.responses.create(
    instructions=SYS_PROMPT_CUSTOMER_SERVICE,
    model="gpt-4.1-2025-04-14",
    tools=[get_policy_doc, get_user_acct],
    input="How much will it cost for international service? I'm traveling to France.",
    # input="Why was my last bill so high?"
)

response.to_dict()["output"]