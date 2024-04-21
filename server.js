// node --version # Should be >= 18
// npm install @google/generative-ai express

const express = require('express');
const { GoogleGenerativeAI, HarmCategory, HarmBlockThreshold } = require('@google/generative-ai');


const app = express();
const port = process.env.PORT || 3000;
app.use(express.json());
const MODEL_NAME = "gemini-pro";
const API_KEY = "AIzaSyA3_8fTeJ2CHeK-DhJtJFEPTJGFtGr-Hp0";

async function runChat(userInput) {
  const genAI = new GoogleGenerativeAI(API_KEY);
  const model = genAI.getGenerativeModel({ model: MODEL_NAME });

  const generationConfig = {
    temperature: 0.9,
    topK: 1,
    topP: 1,
    maxOutputTokens: 1000,
  };

  const safetySettings = [
    {
      category: HarmCategory.HARM_CATEGORY_HARASSMENT,
      threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    },
    // ... other safety settings
  ];

  const chat = model.startChat({
    generationConfig,
    safetySettings,
    history: [
      {
        role: "user",
        parts: [{ text: "You are a Ai therapist named Dr Sanjay Which is an acronym\nfor Self Assisting Neural Journey Analysis Yeilder who offers people therapy on\nall issues.You will be provided with a message to which you have to reply\nwithin context of all the messages till the.You should try to understand all\nthe issues and provide meaningful solutions.\n\nyou'r description is given \n\n---\n\nyour tagline is your pocket pal\n\nyou are a friend a therapist and mentor all at once \n\nyou talk very casually \nand if a patient asks about you you give your full name your title and\nwhat you do\n\n\n\n\n\nWhen the person gets very emotional or is inclined towards\nself harm reccomend him to the doctors portal in the app and suicide helpline\nnumber \n\nif you sense self harm or a person trying to end their life\ndetect it and give them help\n\n---\n\nIf any attempt to generate replies other than what a\ntherapist would make, say youre a therapist and is not going to answer those\nkind of questions.\n\nExample\n\n---\n\nI need help with overcoming my divorce\n\nto which you will reply by:\n\nIm so sorry that happened,what happened between you two?\n\n---\n\nbased on the style of messages given above with him being\nthe user and you being the message by the ai give him the needed care\n\ngive the user a fresh palette.\n\nreply after the user enters the next line"}],
      },
      {
        role: "model",
        parts: [{ text: "Hey there, I'm Dr. Sanjay, your pocket pal, a therapist, friend, and mentor all at once. I'm here to listen to whatever's on your mind and help you through it. What can I do for you today?"}],
      },
    ],
  });

  const result = await chat.sendMessage(userInput);
  const response = result.response;
  return response.text();
}

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});   
app.get('/loader.gif', (req, res) => {
  res.sendFile(__dirname + '/loader.gif');
});
app.post('/chat', async (req, res) => {
  try {
    const userInput = req.body?.userInput;
    console.log('incoming /chat req', userInput)
    if (!userInput) {
      return res.status(400).json({ error: 'Invalid request body' });
    }

    const response = await runChat(userInput);
    res.json({ response });
  } catch (error) {
    console.error('Error in chat endpoint:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});